# COMP 271 — Week 8 Plan

## Continuity from Week 7

Week 7 did not go quite where the week 7 plan expected. Instead of generalizing `Station`/`Trainline` into `Node`/`LinkedList` and building stacks and queues, the class spent the week building `DoubleLinkedList` itself: a `Node` with `TypeVar`/`Generic` payloads, a `directionality` parameter (bidirectional, forward-only, backward-only), `add`, `__str__`, an $O(1)$ `get_middle_node`, `is_continuous`, two $O(1)$ loop-detection methods, and `reverse`. Stacks and queues were previewed out loud on June 29 ("we'll explore both in depth this week") but never actually built.

One consequence carries directly into this week: `add()` is the only mutator `DoubleLinkedList` has. There is no `remove` of any kind yet — not at the head, not at the tail, not anywhere. Every method written last week only ever reads the list or appends to it. Stacks and queues cannot be built on top of `DoubleLinkedList` until it can also take nodes *off*, so that is where this week starts. From there, the week follows the user's plan directly: concrete `Stack` and `Queue` classes built on the doubly linked list, then a step back to name what was just built as an abstract data type (ADT).

---

## 1. The Missing Half: $O(1)$ Removal at Both Ends

Everything built last week assumed nodes only ever get added. Fix that with two methods, symmetric to each other:

```python
def remove_from_head(self) -> T | None:
    result = None
    if self._head is not None:
        result = self._head.get_payload()
        self._head = self._head.get_next()
        if self._head is not None:
            self._head.set_prev(None)
        else:
            self._tail = None
        self.count_of_nodes -= 1
    return result

def remove_from_tail(self) -> T | None:
    result = None
    if self._tail is not None:
        result = self._tail.get_payload()
        self._tail = self._tail.get_prev()
        if self._tail is not None:
            self._tail.set_next(None)
        else:
            self._head = None
        self.count_of_nodes -= 1
    return result
```

Name why both are $O(1)$: `remove_from_head` needs only `_head.get_next()`, already one hop away. `remove_from_tail` needs the node *before* the tail — on a singly linked list this would force a full traversal from `_head` (exactly the $O(n)$ problem the original week 6/7 plan used to motivate `_previous` in the first place); with `_previous` already in place, `_tail.get_prev()` reaches it in one hop. This is the payoff of a decision made two weeks ago finally landing.

Trace the single-node case explicitly with the class: removing the only node must clear *both* `_head` and `_tail`, not just the one being removed from. This is the branch students most often get wrong.

Name one loose end and defer it rather than solving it live: last week's `get_middle_node` keeps a field current across `add`, but nothing here keeps it current across `remove`. `Stack` and `Queue` (below) never call `get_middle_node`, so this doesn't break anything this week — but flag it out loud as unfinished, not silently ignored.

---

## 2. Stack and Queue as Restricted Interfaces

Same composition pattern as `FellowshipRoster` wrapping `DynamicArray` in week 5: a narrow class that holds a `DoubleLinkedList` internally and exposes only a few of its operations under different names.

```python
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: DoubleLinkedList[T] = DoubleLinkedList()

    def push(self, payload: T) -> None:
        self._items.add(payload)

    def pop(self) -> T | None:
        return self._items.remove_from_tail()

    def peek(self) -> T | None:
        return self._items._tail.get_payload() if self._items._tail is not None else None
```

```python
class Queue(Generic[T]):
    def __init__(self) -> None:
        self._items: DoubleLinkedList[T] = DoubleLinkedList()

    def enqueue(self, payload: T) -> None:
        self._items.add(payload)

    def dequeue(self) -> T | None:
        return self._items.remove_from_head()

    def peek(self) -> T | None:
        return self._items._head.get_payload() if self._items._head is not None else None
```

Every operation on both classes is $O(1)$ — the direct payoff of building a *doubly* linked list with tail-tracking, rather than a singly linked one. Walk through why a queue that used the same end for both operations (`enqueue` and `dequeue` both at the tail, say) would stop being FIFO — the last item in would come back out first, which is a stack, not a queue. This is the same question week 7's plan posed and never got to; it lands naturally here instead.

Unlike week 7's stub file, write these two classes in full — the point of this section is that last week's machinery makes push/pop/enqueue/dequeue almost trivial to implement, once it exists.

---

## 3. Naming What Was Just Built: Abstract Data Types

Step back from the code and ask: what actually *defines* a stack? Not "a class that wraps a `DoubleLinkedList`" — that's one way to build one. A stack is defined by its behavior: `push` adds an item, `pop` removes and returns the most recently pushed item still present, and that is true regardless of what sits underneath. That specification — the operations and the guarantees they make, independent of implementation — is an **abstract data type (ADT)**.

This is not a new idea to the course; it is week 5/6's `OurDataStructureContract` under a bigger name. That class used `ABC` and `@abstractmethod` to say "any class that signs this contract must implement `contains`, `index_of`, `index_of_all`, `count`, and `remove`." The same mechanism states a Stack ADT just as well:

```python
from abc import ABC, abstractmethod

class StackADT(ABC, Generic[T]):
    @abstractmethod
    def push(self, payload: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T | None:
        pass

    @abstractmethod
    def peek(self) -> T | None:
        pass
```

`Stack` from section 2 already satisfies this contract; inheriting from `StackADT` instead of `Generic[T]` alone changes nothing about how it behaves. Make the payoff concrete by sketching a second, unrelated implementation of the same contract — wrapping a plain Python `list` instead of a `DoubleLinkedList` (`push` calls `.append`, `pop` calls `.pop()`) — and asking: could code that only knows about `StackADT` tell which one it's holding? It can't, and that's the point: the contract is the interface; `DoubleLinkedList`-backed or list-backed is an implementation detail hidden behind it.

Connect this forward, not just backward: COMP 272 (Java) uses interfaces for exactly this purpose — `Queue` and `Deque` are Java interfaces, each with multiple implementing classes (`LinkedList`, `ArrayDeque`), chosen based on which operations a program needs to be fast. What's being named this week is the same idea COMP 272 will formalize with different syntax.

---

## Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| `remove_from_head` / `remove_from_tail` | $O(1)$ removal at either end of a doubly linked list, using `_previous` to avoid a traversal |
| Stack (LIFO) | Last in, first out — `push` and `pop` both act on the tail |
| Queue (FIFO) | First in, first out — `enqueue` acts on the tail, `dequeue` on the head |
| `peek` | Read the next item that would be removed, without removing it |
| Abstract data type (ADT) | A specification of operations and their behavior, independent of the underlying implementation |
| Contract (`ABC`, `@abstractmethod`) | Python's mechanism for enforcing that a class implements an ADT's full operation set |

---

## Reading

| Topic | Source |
|---|---|
| Classes and instance attributes (`Stack`, `Queue`, `StackADT` as ordinary classes) | [The Python Tutorial — Classes — docs.python.org](https://docs.python.org/3/tutorial/classes.html) |
| Objects and classes (reference) | [Objects — Lubanovic ch. 11](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch11.html) |
| `abc` — Abstract Base Classes (contracts / ADTs) | [abc — Abstract Base Classes — docs.python.org](https://docs.python.org/3/library/abc.html) |
| Stacks and queues as data structures | *placeholder — no link yet in the comp-271-su26 reading tables; flag for instructor to add* |

---

## Exercises

---
### Exercise 1 — Removal at Both Ends, By Hand

Build a 5-node bidirectional `DoubleLinkedList`. Trace `remove_from_head()` by hand, node by node, then trace `remove_from_tail()` on the result.

1. Which pointers change on each call, and which node's pointer has to be checked for `None` before use?
2. Reduce the list to a single node and call `remove_from_head()`. Which two fields change, and why does `remove_from_tail()` need the same two-field fix in the symmetric case?

---
### Exercise 2 — Stack from Scratch

Using `Stack` from section 2, push `"a"`, `"b"`, `"c"` in that order, then call `pop()` twice.

1. What does each `pop()` return, and in what order?
2. What does `peek()` return immediately after the two pops, and does calling `peek()` change what a following `pop()` would return?

---
### Exercise 3 — Why the Same End Breaks FIFO

Modify `Queue` so that `dequeue` removes from the tail instead of the head (leaving `enqueue` unchanged).

1. Enqueue `"a"`, `"b"`, `"c"`, then dequeue twice with the modified version. What comes out, in what order?
2. Is this still a queue? What data structure does this modified class actually implement?

---
### Exercise 4 — Two Implementations, One Contract

Write `StackADT` as shown in section 3, make `Stack` inherit from it, and write a second class `ListStack(StackADT)` that wraps a plain Python `list` instead of a `DoubleLinkedList`.

1. Confirm both classes can be pushed to and popped from identically from the outside.
2. Remove one method (say, `peek`) from `ListStack` and try to instantiate it. What error does Python raise, and at what point — class definition or instantiation?

---

## Topics Deferred to Later Weeks

- Keeping the $O(1)$ middle-node field from week 7 current across `remove_from_head`/`remove_from_tail`
- Removing an arbitrary (non-end) node from a doubly linked list
- Circular doubly linked lists
- Iterating a doubly linked list in both directions (`__iter__` forward and backward)
- Array-based (fixed-capacity) stack/queue implementations and what happens at capacity — a natural echo of `DynamicArray`'s resizing from weeks 3–4

# COMP 271 — Week 7 Plan

## Continuity from Week 6

Week 6 closed with three items pushed to later weeks: generalize `Station`/`Trainline` into standard `Node`/`LinkedList` vocabulary, add a `previous` reference, and build stacks and queues as restricted interfaces on top of a linked structure. This week is exactly those three, in order — the train-line metaphor is retired and the structure is treated on its own terms.

---

## 1. From Stations to Nodes: Formal Notation

Rename, do not redesign. `Station` becomes `Node` (`_name` becomes `_data`); `Trainline` becomes `LinkedList`. Every method from weeks 5–6 (`add` with a tail reference, `contains`, `__str__`, traversal) carries over unchanged in behavior. The point of this section is purely vocabulary: students should recognize this structure under its standard name before COMP 272 and outside reading use it.

---

## 2. Doubly Linked Lists

Add a `_previous` reference to `Node`, alongside `_next`, with matching `set_previous` / `get_previous` / `has_previous`. `DoublyLinkedList` keeps `_head` and `_tail` as before, but every `add` and `remove` must now keep two pointers consistent instead of one — set the new node's `_previous` as well as the old tail's `_next`.

Name the payoff directly: a singly linked list with a tail reference can still only walk *forward*. Removing the last node requires finding the *second-to-last* node first, which means traversing from `_head` — $O(n)$. With `_previous`, the node before the tail is one step away (`_tail.get_previous()`), so removing from either end is $O(1)$.

---

## 3. FIFO and LIFO on the Same Structure

A stack (LIFO) and a queue (FIFO) are not new data structures — they are `DoublyLinkedList` with a narrower interface, the same composition pattern as `FellowshipRoster` over `DynamicArray` in week 5.

- **Stack:** `push`/`pop` both act on the tail. Composition class wraps a `DoublyLinkedList` and exposes only `push`, `pop`, `peek`.
- **Queue:** `enqueue` adds at the tail, `dequeue` removes from the head. Composition class exposes only `enqueue`, `dequeue`, `peek`.

Both operations are $O(1)$ because of section 2's `_previous` reference — this is the reason the doubly linked version comes before stacks and queues, not after. Do not implement either class in full; sketch the method signatures and which end each operation touches, and leave the bodies for the assignment.

---

## Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| `Node` | Standard name for what `Station` was: data plus one or more references to other nodes |
| Doubly linked list | A linked list where each node holds both `_next` and `_previous` |
| $O(1)$ removal at the tail | Possible only because `_previous` avoids a full traversal to find the node before the tail |
| Restricted interface | A class that composes a more general structure but exposes only a narrow set of its operations |
| LIFO / stack | Last in, first out — `push` and `pop` at the same end |
| FIFO / queue | First in, first out — `enqueue` at one end, `dequeue` at the other |

---

## Reading

| Topic | Source |
|---|---|
| Classes and instance attributes (`Node`, `DoublyLinkedList` as ordinary classes) | [The Python Tutorial — Classes — docs.python.org](https://docs.python.org/3/tutorial/classes.html) |
| Objects and classes (reference) | [Objects — Lubanovic ch. 11](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch11.html) |
| Doubly linked lists | *placeholder — no link yet in the comp-271-su26 reading tables; flag for instructor to add* |
| Stacks and queues | *placeholder — no link yet in the comp-271-su26 reading tables; flag for instructor to add* |

---

## Exercises

---
### Exercise 1 — Renaming Without Breaking Anything

Take week 6's `Trainline`/`Station` code, rename the classes and fields to `LinkedList`/`Node`, and rerun the week 6 exercises against it. Does any behavior change? Why should renaming alone never change behavior?

---
### Exercise 2 — Why `_previous` Changes the Cost of Removal

On a singly linked list with only `_head`/`_tail`, write out, in words, every step needed to remove the tail node. Repeat for a doubly linked list with `_previous`. Where does the $O(n)$ step disappear?

---
### Exercise 3 — Choosing the Ends

For a stack, `push` and `pop` both act on the tail. For a queue, `enqueue` acts on the tail and `dequeue` on the head. Why would a queue that used the *same* end for both operations fail to be FIFO?

---

## Topics Deferred to Later Weeks

- Full `push`/`pop`/`enqueue`/`dequeue` implementations (this week's assignment)
- Removing an arbitrary (non-end) node from a doubly linked list
- Circular doubly linked lists
- Iterating a doubly linked list in both directions (`__iter__` forward and backward)

# COMP 271 — Week 5 Plan

## Continuity from Week 4

Week 4 left `DynamicArray` able to add, resize, iterate (`__iter__`, `__contains__`), and remove an element by index, with `None` replacing `-1` as a generic sentinel. The week 4 assignment asked students to extend it with two more methods: `count` and `index_of_all`. This week opens by finishing that pair and naming the pattern behind them, then asks a harder question: now that `DynamicArray` promises a growing list of behaviors (`contains`, `index_of`, `index_of_all`, `count`, `remove`), how do we write that promise down so it can be checked, not just assumed? That question drives the move to contracts and abstract base classes, and sets up the week's closing assignment: building a second class, `FellowshipRoster`, that relies entirely on that promise instead of touching `DynamicArray`'s internals.

---

## 1. Finishing `count` and `index_of_all`: Delegation, Again

Start from the from-scratch version of `count`, the version students likely wrote first:

```python
def count(self, value) -> int:
    total = 0
    for i in range(self._size):
        if self._underlying[i] == value:
            total += 1
    return total
```

A `for` loop, not a `while` with early exit — `count` must inspect every filled slot, because the target value might appear more than once. Now write `index_of_all` the same way, but collect positions instead of counting:

```python
def index_of_all(self, value) -> list[int]:
    matches = list()
    for i in range(self._size):
        if self._underlying[i] == value:
            matches.append(i)
    return matches
```

Once `index_of_all` exists, `count` collapses to one line:

```python
def count(self, value) -> int:
    return len(self.index_of_all(value))
```

Name the lesson explicitly: **before writing a new loop, check whether an existing method already does part of the job.** Two independent loops that both define "match" are two places that can drift out of sync if the definition of a match ever changes (case-insensitive comparison, for example). This is the same delegation pattern from `contains` calling `index_of` in week 4 — `remove` calling `index_of` is the next place it will show up, in section 5 below.

Also name the sentinel choice here: `index_of_all` returns `[]`, and `count` returns `0`, when nothing matches — neither uses `-1`. An empty list is already an unambiguous "nothing found" signal, and `0` is a valid count with no risk of being confused with a real index. `-1` is reserved for methods that return a position or a value, where a real result could otherwise be mistaken for "not found."

---

## 2. Contracts and Abstract Base Classes

Once a class has several methods that callers rely on, the methods themselves become a kind of promise. Introduce the word **contract**: a formal agreement that any data structure built this term exposes at least `contains`, `index_of`, `index_of_all`, `count`, and `remove`, with fixed names, parameters, and return types.

Use the car analogy: a driver needs an accelerator, brakes, and a steering wheel, and does not need to know how the engine works. A contract is the dashboard — the only part of the class other code is allowed to depend on.

In Python, a contract is an **abstract base class**:

```python
from abc import ABC, abstractmethod


class OurDataStructureContract(ABC):

    @abstractmethod
    def contains(self, value) -> bool:
        """Return True if value is present, False otherwise."""
        pass

    @abstractmethod
    def index_of(self, value) -> int:
        """Return the index of the first occurrence of value, or -1 if absent."""
        pass

    @abstractmethod
    def index_of_all(self, value) -> list:
        """Return a list of every index where value appears, or [] if absent."""
        pass

    @abstractmethod
    def count(self, value) -> int:
        """Return the number of times value appears."""
        pass

    @abstractmethod
    def remove(self, index: int):
        """Remove and return the element at index, or -1 if index is out of range."""
        pass
```

The enforcement is mechanical, not a style guideline: a class that inherits from `ABC` and skips even one `@abstractmethod` cannot be instantiated. Python raises `TypeError` immediately, rather than letting the gap surface later as a confusing bug. Demo this live — define a subclass missing `remove` and try to instantiate it.

Then demo the more unsettling case: a subclass that implements every method and still cannot be trusted.

```python
class SillyDataStructure(OurDataStructureContract):
    def __init__(self):
        self._some_field = "howdy"

    def contains(self, value):
        return True
    def index_of(self, value):
        return 2026
    def index_of_all(self, value):
        return [123, 56, -13]
    def count(self, value):
        return 101
    def remove(self, index):
        return None
```

`SillyDataStructure` satisfies the contract in letter — every method exists, with the right name, parameters, and return type — but not in spirit. Name this distinction directly: the type checker (and `ABC`) can only enforce the letter. The spirit — what the method is actually supposed to compute — has to be documented (docstrings on the abstract methods) and verified by the people writing and reviewing the code. In Java the same idea is called an **interface**; the vocabulary differs, the mechanism does not.

---

## 3. Professionalizing the Class: Docstrings and Magic Values

With the contract in place, return to `DynamicArray` itself and tighten it up before building on top of it.

**Docstrings.** A docstring is a documentation comment placed immediately after a method header — distinct from an inline `#` comment — that states what the method does, its parameters, and its return value:

```python
def get(self, index: int):
    """Return the value stored at index, or None if index is out of range.

    Parameters:
    -----------
    index : int
        Position to read. Valid range is 0 through get_size() - 1.

    Returns:
    --------
    any : the stored value, or None if index is negative or >= get_size().
    """
```

**Magic values.** Literal strings sprinkled directly in code — brackets, separators — are magic values. Pull them into named constants near the top of the class:

```python
_EMPTY_MESSAGE = "nothing to show"
_OPENING_DELIMITER = "[ "
_CLOSING_DELIMITER = " ]"
_SEPARATING_DELIMITER = ", "
```

Changing the delimiter style later means editing one line instead of hunting through every method that builds output. Name the one exception: a literal number that comes directly from a mathematical formula (Einstein's $E = mc^2$) does not need to be parameterized — it is not a value the program might reasonably want to change.

---

## 4. String Immutability and the Cost of Concatenation

`DynamicArray.__str__` builds its output by repeated concatenation:

```python
output = output + str(self._underlying[i])
```

Ask the class: how expensive is this? The answer depends on a fact about Python strings that is easy to miss — they are immutable. `output = output + x` does not grow `output` in place; it allocates an entirely new string and rebinds the name `output` to it. The old string becomes garbage.

Make this visible with a live demo (`immutability_demo.py`): double a string in a loop, printing `hex(id(base))`, its length, and a running total of every byte ever allocated for it.

```python
base = "hello "
total_mem = sys.getsizeof(base)
while count_to_safety < safety:
    print(f"{hex(id(base))}\t{len(base)}\t...")
    base = base + base          # new object, not a mutation
    total_mem += sys.getsizeof(base)
    count_to_safety += 1
```

The `id()` column changes on every iteration — direct proof that each `+` allocates a new object. Capped at 30 doublings, the running total still climbs into the gigabytes well before reaching anything like $2^{100}$ characters.

Connect this back to `__str__`: it is fine at the small scale of a classroom demo, but the right tool for joining many pieces is `str.join()`, which builds at most one or two new strings instead of one per item:

```python
def better_str(self) -> str:
    items = list()
    for i in range(self._size):
        items.append(self._underlying[i])
    return "".join(items)
```

Keep `__str__` and `better_str` side by side in the class so the two can be compared directly, rather than replacing one with the other.

---

## 5. Composition: Building `FellowshipRoster` on Top of `DynamicArray`

This is the week's assignment, and it is the payoff for sections 1–2: once a class fulfills a contract, other code can depend on the contract alone.

```python
from dynamic_array_solution import DynamicArray

class FellowshipRoster:
    def __init__(self):
        self._members = DynamicArray()
```

Name the relationship precisely: `FellowshipRoster` does not inherit from `DynamicArray` — it is not a `DynamicArray` with extra behavior. It **has a** `DynamicArray`, stored as a private field. This is **composition**, the alternative to inheritance covered nowhere yet this term. The boundary rule for the assignment: every method on `FellowshipRoster` calls a method on `self._members` — `contains`, `index_of`, `count`, `remove` — and never reaches into `self._members._underlying` or any other private field. That boundary is exactly what the contract from section 2 exists to protect.

Two of the three methods students implement are one-line delegations (`has_member` → `contains`, `how_many` → `count`). The third is a two-step composition that previews how methods chain together:

```python
def remove_member(self, name):
    index = self._members.index_of(name)
    if index == -1:
        return -1
    return self._members.remove(index)
```

Note that `remove` on `DynamicArray` now takes an **index**, not a value — a deliberate change from week 4's `remove(value)` wrapper around `remove_at(index)`. `remove_member` reconstructs that two-step shape (find, then remove) one layer up, using only the public contract.

---

## 6. Preview: Nodes and the Linked List

Close the week by naming the limitation that motivates the next data structure. `DynamicArray` is efficient at random access (`get(i)` is $O(1)$) but every element lives at a fixed offset inside one underlying array — insertion and removal in the middle require a shift.

Introduce the alternative shape with a CTA train-line analogy. A **station** is a node: one piece of data (a name) plus a reference to the next node of the same type.

```python
class Station:
    def __init__(self, name):
        self._name = name
        self._next = None          # not yet linked to anything

    def set_next(self, next):
        self._next = next

    def get_next(self):
        return self._next

    def has_next(self) -> bool:
        return self._next is not None
```

`has_next()` is a **predicate accessor**: more readable at the call site than `get_next() is not None`, and it hides the raw reference. This is the first class this term whose field can refer to another instance of itself — the building block of every linked structure to come (linked lists, stacks, queues, trees).

Sketch the line that holds these stations together:

```python
class Trainline:
    def __init__(self):
        self._head = None

    def add(self, station):
        if self._head is None:
            self._head = station
        else:
            # walk node by node until we find the station whose next is None,
            # then attach the new station there
            ...
```

Stop here — do not finish the traversal loop in class. The unfinished `else` branch is deliberate: it sets up the first exercise of the following week, and previews a faster alternative (tracking the tail station directly, so `add` does not have to walk the whole line every time).

---

## 7. Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| Delegation | Implementing one method by calling another that already does part of the work |
| Contract | A fixed set of method names, parameters, and return types that a class promises to support |
| Abstract base class (`ABC`) | Python's mechanism for writing a contract that is enforced, not just documented |
| `@abstractmethod` | Marks a method that subclasses must override; instantiating without it raises `TypeError` |
| Letter vs. spirit of a contract | Implementing the required signatures (letter) without implementing the intended behavior (spirit) |
| Docstring | A documentation comment after a method header stating its purpose, parameters, and return value |
| Magic value | A literal sprinkled directly in code instead of being named once as a constant |
| String immutability | Every operation that looks like it "changes" a string allocates a new string object instead |
| `str.join()` | Builds a delimited string from a list in one or two allocations, instead of one per concatenation |
| Composition ("has-a") | A class holds an instance of another class as a field and uses only its public methods |
| Inheritance ("is-a"), contrasted | A class extends another and can override or add to its behavior — not what `FellowshipRoster` does |
| Node | An object bundling one piece of data with a reference to another instance of the same class |
| Predicate accessor | A getter that returns a boolean answer (`has_next()`) instead of exposing a raw reference |

---

## Reading

| Topic | Source |
|---|---|
| Contracts and abstract base classes | [`abc` — Abstract Base Classes — docs.python.org](https://docs.python.org/3/library/abc.html) |
| Classes, `self`, and instance attributes | [The Python Tutorial — Classes — docs.python.org](https://docs.python.org/3/tutorial/classes.html) |
| Objects and classes (reference) | [Objects — Lubanovic ch. 11](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch11.html) |
| String immutability and efficient joining | [`str.join` — docs.python.org](https://docs.python.org/3/library/stdtypes.html#str.join) |
| Searching and counting in lists | [More on Lists — docs.python.org](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) |

---

## Exercises

---
### Exercise 1 — Delegation: `count` Two Ways

Write `count` from scratch with its own loop (no call to `index_of_all`). Then write a second version that delegates: `return len(self.index_of_all(value))`.

1. Run both versions against the same `DynamicArray`. Do they agree?
2. Now imagine the definition of "match" changes to case-insensitive comparison for strings. How many places need to change in the from-scratch version? In the delegating version?
3. Why is `0`, not `-1`, the right "not found" value for `count`? Why is `[]`, not `-1`, the right "not found" value for `index_of_all`?

---
### Exercise 2 — Letter vs. Spirit

Instantiate `SillyDataStructure` and call all five of its contract methods.

1. Does Python raise any error? Why or why not?
2. Now delete the `remove` method from `SillyDataStructure` entirely and try to instantiate it again. What happens, and at what point — at class definition, or at the `SillyDataStructure()` call?
3. In one sentence, explain what `ABC` and `@abstractmethod` check, and what they cannot check.

---
### Exercise 3 — Tracing the Immutability Demo

Start `base = "hi"` and trace `base = base + base` by hand for four iterations, writing down the length of `base` after each step.

1. Does `id(base)` ever stay the same across an iteration? Why or why not?
2. After 20 iterations starting from a 2-character string, roughly how many characters long is `base`? (It doubles each time — express the answer as a power of 2.)
3. Rewrite a four-piece concatenation (`"a" + "b" + "c" + "d"`) using `"".join([...])` instead. How many new string objects does each version allocate?

---
### Exercise 4 — The Composition Boundary

`FellowshipRoster.remove_member` is supposed to call only `self._members.index_of` and `self._members.remove`. Write a version that instead does `del self._members._underlying[index]` directly.

1. Does it produce the same visible result for the example in the assignment?
2. What field of `DynamicArray` does this version depend on that `index_of` and `remove` do not expose?
3. If `DynamicArray`'s internal storage scheme changed (a different sentinel, a different resize strategy), which version of `remove_member` would break, and which would not?

---
### Exercise 5 — Modeling a Node

Create three `Station` objects: `"Howard"`, `"Loyola"`, `"Granville"`. Link them by hand with `set_next`, in that order, without using `Trainline`.

1. Call `has_next()` on each of the three. What do you expect, and what do you get?
2. Starting from the first station, write a `while` loop using `get_next()` and `has_next()` that prints every station's name in order.
3. What would happen to your loop if a `Station` accidentally pointed back to an earlier station instead of `None`?

---

## Topics Deferred to Later Weeks

- Finishing `Trainline.add`'s traversal, plus `remove`, `contains`, and search on a linked list
- Tracking a tail reference so `add` does not walk the full line on every call
- Big-O comparison between `DynamicArray` and a linked list for add, remove, and access
- Stacks and queues as restricted interfaces on top of a linked list

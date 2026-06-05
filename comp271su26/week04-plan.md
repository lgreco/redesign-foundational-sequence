# COMP 271 — Week 4 Plan

## Continuity from Week 3

Week 3 ended with students implementing five accessor methods on `DynamicArray`: `__len__`, `get_size`, `get_capacity`, `get(index)`, and `index_of(value)`. The class can now add elements, resize automatically, and answer read queries. The one thing it cannot do yet is remove an element. That gap drives this week.

The week 3 plan also named amortized cost as a preview topic. This week makes it precise.

---

## 1. Removing an Element: The Shift Problem

Adding to a dynamic array is cheap: store a value at `_underlying[_size]` and increment `_size`. Removing from the middle is not cheap: every element to the right of the removed slot must shift one position left to close the gap.

Walk through an example with the class. Start with:

```
_underlying = [10, 20, 30, 40, -1, -1, -1, -1]
_size = 4
```

Remove the element at index 1 (value `20`). The required steps:

```
index 1 ← index 2  (30 moves left)
index 2 ← index 3  (40 moves left)
index 3 ← -1       (sentinel restores the vacated slot)
_size -= 1
```

The loop is:

```python
def remove_at(self, index: int) -> bool:
    if index < 0 or index >= self._size:
        return False
    for i in range(index, self._size - 1):
        self._underlying[i] = self._underlying[i + 1]
    self._underlying[self._size - 1] = -1
    self._size -= 1
    return True
```

Two things to trace carefully with students:

1. **Why `range(index, self._size - 1)`?** The last real element is at `_size - 1`. That element shifts into `_size - 2`. The loop stops one slot before `_size - 1` — if it went all the way, the final step would copy a sentinel over a sentinel, which is harmless but confusing.
2. **Why restore the sentinel?** After shifting, `_underlying[_size - 1]` still holds the old last value. Leaving it there does not corrupt the array — `_size` was already decremented, so `get` will not reach it — but it is misleading when printing the full underlying structure. Restore it to `-1` to keep the invariant clean.

Once `remove_at` exists, `remove(value)` is a one-liner:

```python
def remove(self, value: int) -> bool:
    index = self.index_of(value)
    if index == -1:
        return False
    return self.remove_at(index)
```

This is a good moment to name the pattern: **build complex operations out of simpler ones you already have.** `remove` does not reimplement the search; it delegates to `index_of`.

---

## 2. Big-O Notation

Before comparing add and remove, students need a shared vocabulary for describing cost. Big-O notation is that vocabulary.

### The idea

When we ask "how long does this operation take?", we don't mean wall-clock seconds — those depend on the hardware, the load on the machine, and dozens of other factors outside our control. We want a measure that captures the *shape* of the cost: how does the time grow as the input gets larger?

Big-O describes an upper bound on that growth. We write $T(n) = O(f(n))$ to mean: the running time $T(n)$ grows no faster than $f(n)$ as $n \to \infty$, up to a constant factor. Formally, $T(n) = O(f(n))$ if there exist constants $c > 0$ and $n_0 \geq 1$ such that

$$T(n) \leq c \cdot f(n) \quad \text{for all } n \geq n_0.$$

Don't dwell on the formal definition — use it to anchor the intuition, then move to concrete examples.

### Common classes

| Class | Name | Example operation |
|---|---|---|
| $O(1)$ | constant | accessing `_underlying[i]` by index |
| $O(\log n)$ | logarithmic | binary search (not yet covered) |
| $O(n)$ | linear | scanning all $n$ elements with `index_of` |
| $O(n \log n)$ | linearithmic | efficient sorting (later) |
| $O(n^2)$ | quadratic | a loop inside a loop, each running $n$ times |

For this course the relevant classes are $O(1)$, $O(n)$, and eventually $O(n^2)$. The others are previews.

### Applying it to `index_of` and the shift loop

`index_of` scans from position 0 until it finds a match or exhausts the array. In the worst case — the value is not present — it touches every one of the $n$ stored elements. That is $O(n)$.

The shift loop inside `remove_at(index)` moves every element from position `index` to `_size - 1` one slot left. In the worst case (`index = 0`), that is $n - 1$ moves: $O(n)$.

### Add: amortized $O(1)$

`add` is more interesting. Most of the time it simply does:

```python
self._underlying[self._size] = value
self._size += 1
```

That is $O(1)$. But occasionally — when `_size == _capacity` — `_resize` runs and copies all $n$ current elements into a new array. That single call is $O(n)$.

The amortized argument shows the expensive calls are rare enough that the average cost per `add` is still $O(1)$. Starting from capacity 4 with a doubling policy, resize events occur after adds number 4, 8, 16, 32, …, copying 4, 8, 16, 32, … elements respectively. After $n$ total adds, the total copy work is at most

$$4 + 8 + 16 + \cdots + n \;\leq\; 2n,$$

because the geometric series $\sum_{k=0}^{\log_2 n} 2^k = 2n - 1$. So the total cost of $n$ adds is $O(n)$, and the average cost per add — the amortized cost — is $O(1)$.

### Add vs. Remove

| Operation | Worst case | Amortized |
|---|---|---|
| `add` | $O(n)$ (resize) | $O(1)$ |
| `remove_at(0)` | $O(n)$ (full shift) | $O(n)$ |
| `remove_at(_size - 1)` | $O(1)$ (no shift needed) | $O(1)$ |
| `index_of` | $O(n)$ (full scan) | $O(n)$ |
| `get(index)` | $O(1)$ (direct access) | $O(1)$ |

Removal from the middle is genuinely $O(n)$ every time — there is no amortization argument because the shift is always required. This is a real limitation of the array-based structure, and it motivates looking at alternative structures (linked lists) in a later week.

---

## 3. Making the Array Iterable

Students have used `for item in some_list:` since COMP 170. Implementing `__iter__` lets `DynamicArray` support the same syntax.

The simplest implementation uses a generator:

```python
def __iter__(self):
    for i in range(self._size):
        yield self._underlying[i]
```

After this, `for zip_code in da:` works exactly as it does for a plain list. Demo this in class — the payoff is visible immediately. Then add `__contains__`:

```python
def __contains__(self, value: int) -> bool:
    return self.index_of(value) != -1
```

Now `60647 in da` works too. These two dunders are what make an object feel like a native Python collection.

---

## 4. The Awkwardness of Integer-Only Storage

The current `DynamicArray` is hardcoded for integers: the sentinel is `-1`, the type hints say `int`. Ask the class: what if you wanted to store strings? Floats? Objects?

The sentinel is the root problem. `-1` is a valid integer, which means a `DynamicArray` can technically store `-1` as data — but `index_of` and `remove` would behave incorrectly (removing `-1` would erase the first sentinel slot, not the stored value).

Introduce `None` as a language-level sentinel that is not a valid value of any type:

```python
self._underlying: list = [None] * self._capacity
```

With `None` as the sentinel, the array can store integers, strings, or any object without ambiguity. Update `__str__` to hide `None` slots. Update `index_of` to compare against `None` for bounds checking.

This is also the moment to remove the `int` type hints from parameters and return values (or replace them with `Any` from `typing`) — the array is now truly generic.

Do not rush this. The goal is for students to see that a design decision made early (sentinel = `-1`) ripples through every method. Changing it requires touching the whole class. That is the lesson.

---

## 5. Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| Shift operation | Moving elements left or right to fill or create a gap |
| $O(f(n))$ | Running time grows no faster than $f(n)$, up to a constant factor |
| Amortized $O(1)$ | The average cost per operation over a long sequence, even if individual operations vary |
| `__iter__` / `yield` | Makes an object usable in a `for` loop |
| `__contains__` | Makes `in` operator work on a custom object |
| Sentinel value | A placeholder that signals "empty"; must not be a valid data value |

---

## Reading

| Topic | Source |
|---|---|
| Removal and list mutation | [More on Lists — docs.python.org](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) · [Lists — Lubanovic ch. 8](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch08.html) |
| Big-O notation | [Big O notation — Wikipedia](https://en.wikipedia.org/wiki/Big_O_notation) · [Time Complexity — Python wiki](https://wiki.python.org/moin/TimeComplexity) |
| Amortized analysis | [Amortized analysis — Wikipedia](https://en.wikipedia.org/wiki/Amortized_analysis) |
| Iterators and `__iter__` | [Iterators — docs.python.org](https://docs.python.org/3/tutorial/classes.html#iterators) |
| Generators and `yield` | [Generators — docs.python.org](https://docs.python.org/3/tutorial/classes.html#generators) |
| Emulating container types (`__contains__`) | [Emulating container types — docs.python.org](https://docs.python.org/3/reference/datamodel.html#emulating-container-types) |
| `None` and the type system | [Built-in Constants — docs.python.org](https://docs.python.org/3/library/constants.html#None) · [typing.Any — docs.python.org](https://docs.python.org/3/library/typing.html#typing.Any) |
| Objects and classes (reference) | [Objects — Lubanovic ch. 11](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch11.html) |

---

## Exercises

---
### Exercise 1 — Tracing `remove_at`

Start with: `_underlying = [10, 20, 30, 40, -1, -1, -1, -1]`, `_size = 4`.

Run `remove_at(0)` mentally, step by step.

1. What are the values in `_underlying` after each iteration of the shift loop?
2. What is `_size` after the call returns?
3. Now call `remove_at(3)` on the original array (before the first removal). Is the shift loop any shorter? Why?

---
### Exercise 2 — The Sentinel Problem

Create a `DynamicArray` with default settings. Add the value `-1` three times. Then call `remove(-1)`.

1. What do you expect `_size` to be after the removal?
2. Run it. What actually happens?
3. Replace the sentinel with `None` (as described in section 4). Does the same problem occur? Why or why not?

---
### Exercise 3 — Iteration

After implementing `__iter__`, write a short script that:
- Creates a `DynamicArray` and adds five zip codes
- Uses a `for` loop to print each one
- Uses `in` to check whether a specific zip code is in the array

Predict the output before running.

---
### Exercise 4 — Cost in Practice

Write a script that adds 1000 elements to a `DynamicArray` starting with capacity 4. Add a counter variable that increments inside `_resize` each time a resize occurs.

1. How many times did `_resize` run?
2. After how many adds did each resize occur? List the first five.
3. Compare those numbers to the powers of 2. What pattern do you see?

---

## Topics Deferred to Later Weeks

- Linked lists as an alternative to arrays for dynamic storage
- Formal Big-O notation and the master theorem
- Stacks and queues as restricted interfaces on top of a dynamic array

# COMP 271 — Week 3 Plan

## Continuity from Week 2

Week 2 ended with an open question in Exercise 4: given a four-element list, can you produce a new eight-element list with the originals in the first four slots and `-1` filling the rest — without using `def`, `class`, or `append`? That question is the entry point for week 3.

This week stays entirely in plain procedural code — no class, no methods. The goal is to understand the mechanics of a dynamic array as a sequence of statements before wrapping any of it in abstractions.

---

## 1. The Starting State

Pick up exactly where week 2 left off. We have a list pretending to be a fixed-size array and two variables tracking its state:

```python
CAPACITY = 4
data = [-1] * CAPACITY
size = 0
```

`CAPACITY` is a named constant — a module-level variable in ALL_CAPS that we treat as fixed. `data` is our array: four slots, all initialized to the sentinel value `-1`. `size` counts how many real values have been stored.

Adding an element is two lines:

```python
data[size] = 60611
size += 1
```

Do this four times and the array is full: `size == CAPACITY`.

---

## 2. The Doubling Operation

When `size == CAPACITY`, we cannot add another element without first making room. Here is the doubling code — the answer to Exercise 4:

```python
new_capacity = CAPACITY * 2
new_data = [-1] * new_capacity
for i in range(size):
    new_data[i] = data[i]
data = new_data
CAPACITY = new_capacity
```

Walk through each line:

- `new_capacity` is the target size — twice what we have now.
- `new_data` is a fresh list of that size, filled with sentinels.
- The `for` loop copies the real elements one by one. It runs `range(size)`, not `range(CAPACITY)` — we copy only what was actually stored, not the sentinels.
- `data = new_data` makes `data` point to the new list. The old list is discarded.
- `CAPACITY = new_capacity` updates the bound so the next check is correct.

After this block, `data` has eight slots, the first four hold the original values, and `size` is still 4 — nothing was added yet, we only made room.

---

## 3. A Complete Sequence

Put it together as a single script. Run it line by line in class, asking students to predict `data`, `size`, and `CAPACITY` at each step before executing.

```python
CAPACITY = 4
data = [-1] * CAPACITY
size = 0

# Add four zip codes
data[size] = 60611; size += 1
data[size] = 60614; size += 1
data[size] = 60647; size += 1
data[size] = 60660; size += 1

print(data)       # [-1, -1, -1, -1] gone; now [60611, 60614, 60647, 60660]
print(size)       # 4
print(CAPACITY)   # 4

# Array is full — double it
new_capacity = CAPACITY * 2
new_data = [-1] * new_capacity
for i in range(size):
    new_data[i] = data[i]
data = new_data
CAPACITY = new_capacity

print(data)       # [60611, 60614, 60647, 60660, -1, -1, -1, -1]
print(size)       # 4  (unchanged)
print(CAPACITY)   # 8

# Now add a fifth zip code
data[size] = 60601; size += 1

print(data[:size])   # [60611, 60614, 60647, 60660, 60601]
print(size)          # 5
print(CAPACITY)      # 8
```

After the doubling block, pause and ask: what does `data` look like in full right now — all eight slots? Then ask: why does `print(data[:size])` give a cleaner result than `print(data)`?

---

## 4. Wrapping the Operations in Functions

The flat script works but has a problem: the doubling block is just a chunk of code floating in the middle of the program. If we needed to double again, we would copy and paste it. That is the moment to introduce standalone functions — not methods, just plain `def` at module level.

```python
def resize(data, size, capacity):
    new_capacity = capacity * 2
    new_data = [-1] * new_capacity
    for i in range(size):
        new_data[i] = data[i]
    return new_data, new_capacity


def add(data, size, capacity, value):
    if size == capacity:
        data, capacity = resize(data, size, capacity)
    data[size] = value
    size += 1
    return data, size, capacity
```

Two things to notice:

1. **Both functions return the updated state.** In Python, a plain function cannot modify the caller's variable — it can only return a new value. So `resize` returns the new list and new capacity; `add` returns all three pieces of state. The caller must reassign: `data, size, capacity = add(data, size, capacity, 60601)`.

2. **`add` calls `resize` internally.** The decision to resize is not the caller's problem. This is already the key idea behind encapsulation — the caller says "add this value" and does not need to know whether a resize happened.

Rewrite the demo using these functions:

```python
CAPACITY = 4
data = [-1] * CAPACITY
size = 0

data, size, capacity = add(data, size, CAPACITY, 60611)
data, size, capacity = add(data, size, capacity, 60614)
data, size, capacity = add(data, size, capacity, 60647)
data, size, capacity = add(data, size, capacity, 60660)
data, size, capacity = add(data, size, capacity, 60601)   # resize happens here

print(data[:size])   # [60611, 60614, 60647, 60660, 60601]
print(capacity)      # 8
```

---

## 5. The Awkwardness to Name

Before moving on, point out the friction in this design:

- The caller must carry `data`, `size`, and `capacity` as three separate variables everywhere.
- Every call to `add` requires passing all three and reassigning all three.
- Nothing prevents the caller from passing mismatched values — `add(data, 99, 4, value)` would corrupt the array silently.

This is not a bug in the code; it is a limitation of the approach. Three variables that always travel together and must be kept consistent are a data structure waiting to be named. That is exactly what a class does: it bundles state and behavior into one thing so the caller cannot accidentally separate them.

That observation is the bridge to week 4.

---

## 6. Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| Named constant | A module-level variable in ALL_CAPS whose value is fixed by convention |
| Sentinel value | A placeholder (here `-1`) that marks an unoccupied slot |
| `size` vs `capacity` | `size` counts real elements; `capacity` is the total allocated space |
| Return multiple values | A Python function can return a tuple; the caller unpacks it with `a, b = f()` |
| Amortized cost | The resize is expensive but rare; spread across many additions, the average cost per element is constant |

Amortized cost is a preview — name it, give the intuition, do not press for formal analysis. It returns in a later week.

---

## Exercises

---
### Exercise 1 — Tracing the Doubling Block

Start with this state: `data = [10, 20, 30, 40]`, `size = 4`, `CAPACITY = 4`.

Run the doubling block mentally — do not execute it yet.

1. What are the values of `new_capacity`, `new_data`, and `data` after the block completes?
2. What is the value of `size` after the block? Why did it not change?
3. Now execute the block and verify your predictions. If anything was wrong, identify the specific line where your model diverged.

---
### Exercise 2 — Why `range(size)` and Not `range(capacity)`

The copy loop uses `range(size)`. Suppose you changed it to `range(capacity)`.

1. For the specific state above (`size = 4`, `CAPACITY = 4`), would the output change? Why or why not?
2. Now suppose `size = 2` and `CAPACITY = 4`. Run both versions mentally. What is different in `new_data` after each?
3. Which version is correct? Which is merely harmless in some cases?

---
### Exercise 3 — A Deliberate Bug: Forgetting to Update `CAPACITY`

Remove the last line of the doubling block — `CAPACITY = new_capacity` — and run the full demo script.

1. Does the program crash immediately? If not, where does it first behave incorrectly?
2. What is the value of `CAPACITY` when the sixth zip code is added? What does `add` decide to do with that value?
3. What kind of bug is this — one that raises an exception, one that produces wrong output, or one that silently corrupts state? Why is the third kind the most dangerous?

---
### Exercise 4 — The Three-Variable Problem

The `add` function signature is `add(data, size, capacity, value)`.

1. Write a call to `add` that passes mismatched values — for example, a `size` that is larger than the actual number of elements in `data`. What happens when you run it?
2. Is there any way, using only the three-variable design, to prevent a caller from passing mismatched state? Or is the problem fundamental to this approach?
3. In one sentence, describe what a class would do differently to prevent this problem.

---

## Topics Deferred to Later Weeks

- Wrapping `data`, `size`, and `capacity` into a class (week 4)
- `__len__` and `__getitem__` for natural Python syntax
- Linked lists as an alternative to arrays for dynamic storage
- Formal Big-O analysis of `add` (amortized constant time)

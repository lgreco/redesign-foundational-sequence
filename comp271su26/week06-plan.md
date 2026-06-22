# COMP 271 — Week 6 Plan

## Continuity from Week 5

Week 5 left the train-line metaphor half-built: `Station` is complete (`name`, `next`, `set_next`, `get_next`, `has_next`), but `Trainline.add` stops at the `else` branch — "walk node by node until we find the station whose `next` is `None`, then attach the new station there" is a comment, not code. This week finishes that traversal, then immediately replaces it with a faster version that tracks the tail directly, which was previewed at the end of week 5 as a "faster approach." From there the week uses the same traversal pattern to build `contains` and an `O(n)` `count`, and closes by posing — without yet answering — the question of what happens if a station ever points backward into the line it came from.

This is also the last week framed entirely by the train-line dressing. Starting next week the vocabulary generalizes: `Station` becomes `Node`, `Trainline` becomes `LinkedList`, and the structure is treated on its own terms rather than through the CTA analogy. Say this explicitly near the end of the week so students see the metaphor as scaffolding being removed, not abandoned.

---

## 1. Finishing the Traversal: Implementing `add()` in Full

Pick up exactly where week 5 stopped. The line already has a head; adding past the first station means walking forward until `has_next()` is `False`, then attaching there.

```python
def add(self, station):
    if self._head is None:
        self._head = station
    else:
        current = self._head
        while current.has_next():
            current = current.get_next()
        current.set_next(station)
```

Trace this with the class against a concrete line — three stations already linked, a fourth being added — before running it. Ask: why `while current.has_next()` and not `while current is not None`? Both terminate at the same station, but `has_next()` reads as "is this the last station," which is the question being asked, while `current is not None` reads as "does a station exist here," which is a different (and in this loop, always-true) question. Prefer the accessor that matches the intent.

Name the cost once `add` works: every call walks the entire line from `_head`. Adding the $n$-th station costs $O(n)$. Adding $n$ stations one at a time costs

$$1 + 2 + 3 + \cdots + n = O(n^2).$$

This is worse than `DynamicArray.add`, whose amortized cost is $O(1)$ even though it occasionally resizes. The train-line metaphor makes the reason vivid: there is no way to reach the last station except by riding through every station before it.

---

## 2. Tracking the Tail: A Faster `add()`

The fix does not require changing how stations link to each other — only what `Trainline` remembers. Add a second field, `_tail`, that always points at the last station:

```python
def __init__(self):
    self._head = None
    self._tail = None

def add(self, station):
    if self._head is None:
        self._head = station
    else:
        self._tail.set_next(station)
    self._tail = station
```

Walk through why this is correct in both branches: when the line is empty, the new station is both head and tail. When the line is non-empty, the *old* tail gets a new successor, and then `_tail` is reassigned to the new station — in that order. Ask the class what breaks if the two lines are swapped (`self._tail = station` before `self._tail.set_next(station)`): the station would try to attach itself to itself, and the rest of the line becomes unreachable from `_tail`.

Now `add` is $O(1)$ — no traversal at all. Update the running add/remove/access comparison table from week 4 to include the linked line:

| Operation | `DynamicArray` | `Trainline` (with `_tail`) |
|---|---|---|
| `add` (append) | $O(1)$ amortized | $O(1)$ |
| `get(i)` / direct access | $O(1)$ | $O(n)$ — no index, only traversal |
| search (`contains`, `index_of`) | $O(n)$ | $O(n)$ |
| remove from front | $O(n)$ (full shift) | $O(1)$ (move `_head`) |

This is the moment to name the actual trade-off, not just declare a winner: the linked line trades fast random access for fast insertion at the ends. Neither structure is strictly better — the right choice depends on which operation the program needs most.

---

## 3. Traversal as the General Tool: `contains`

`DynamicArray` had an underlying array to index into; `Trainline` has nothing but `_head` and a chain of `next` references. Every read operation on a linked structure is some shape of the same walk:

```python
def contains(self, name) -> bool:
    current = self._head
    while current is not None:
        if current.get_name() == name:
            return True
        current = current.get_next()
    return False
```

Note the loop condition here is `current is not None`, not `current.has_next()` — this loop is asking "does a station exist to examine," a different question from section 1's "is this the last station." Point out that this is the same linear-search shape as `DynamicArray.index_of` from week 3, just walking pointers instead of incrementing an index. The underlying idea — visit each element once, in order, until you find what you are looking for or run out of elements — does not change when the storage mechanism changes.

Build `__str__` the same way, accumulating a string in forward order as the line is walked:

```python
def __str__(self) -> str:
    if self._head is None:
        return "(empty line)"
    output = str(self._head)
    current = self._head.get_next()
    while current is not None:
        output = output + " -> " + str(current)
        current = current.get_next()
    return output
```

Keep this version forward-only — front to back, in the order the stations were added. Do not demonstrate building the string in reverse order here; that exact technique, run in the opposite direction, is the subject of this week's assignment.

---

## 4. Counting the Naive Way

Demo a `count` that answers "how many stations are on this line" by walking the whole thing:

```python
def count(self) -> int:
    current = self._head
    total = 0
    while current is not None:
        total += 1
        current = current.get_next()
    return total
```

Run it against a line with a known number of stations to confirm it works, then name the cost directly: this is $O(n)$, and — unlike `DynamicArray.count`, which at least has to scan to find matches — this version recomputes the same answer from scratch on every call, even if nothing on the line has changed since the last call.

Pose the question without answering it: `DynamicArray` tracks `_size` as a field, updated incrementally by `add` and `remove`, so `get_size()` never has to count anything. Could `Trainline` do the same? Leave this open — it is the first item in this week's assignment, and the point is for students to notice the parallel to `_size` themselves rather than be handed it.

---

## 5. When a Line Doesn't End: A Glimpse of Loops

Close with a problem, not a solution. Every traversal so far — `add`, `contains`, `__str__`, `count` — assumes the chain of `next` references eventually reaches a station whose `next` is `None`. Ask: what if it doesn't?

Build a small cyclic structure live, by hand, without going through `Trainline.add`:

```python
a = Station("Howard")
b = Station("Loyola")
c = Station("Granville")
a.set_next(b)
b.set_next(c)
c.set_next(a)        # points back to the start
```

Ask the class to predict what `count()` does on this structure *before* running it — most will correctly guess it never returns. If you run it, cap it first (a loop counter with a safety limit, the same defensive technique from the immutability demo in week 5) so the demo doesn't actually hang. The CTA Loop downtown is the obvious hook for why this matters: a real transit line can loop back on itself by design, but a data structure that is supposed to terminate cannot assume it will.

Do not introduce cycle detection here — no two-pointer technique, no visited set. Name only the problem: a traversal that assumes termination will spin forever on a line that doesn't terminate, and detecting that *in general*, without already knowing the line is cyclic, is harder than it looks. That problem is `has_loop()`, the second item in this week's assignment.

---

## 6. Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| Traversal | Walking a linked structure one `next` reference at a time, from a starting node to a stopping condition |
| `has_next()` vs. `is not None` | Two traversal stop conditions that read differently: "is this the last node" vs. "does a node exist here" |
| Tail reference | A field that always points at the last node, avoiding a full traversal to find it |
| Random access vs. sequential access | Direct indexing ($O(1)$ on an array) vs. walking node by node ($O(n)$ on a linked structure) |
| Cycle | A chain of `next` references that loops back on itself instead of ending at `None` |
| Defensive loop cap | A counter with an upper bound used to demo a structure that would otherwise loop forever |

---

## Reading

| Topic | Source |
|---|---|
| Classes, `self`, and instance attributes (`Station`, `Trainline` as ordinary classes) | [The Python Tutorial — Classes — docs.python.org](https://docs.python.org/3/tutorial/classes.html) |
| Objects and classes (reference) | [Objects — Lubanovic ch. 11](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch11.html) |
| Linked lists and node-based traversal | *placeholder — no link yet in the comp-271-su26 reading tables; flag for instructor to add* |
| Cycle detection in linked structures | *placeholder — no link yet in the comp-271-su26 reading tables; flag for instructor to add* |

---

## Exercises

---
### Exercise 1 — Tracing `add` Before and After the Tail

Build a line with three stations using the week-5, head-only version of `add` (section 1). Add a fourth station and count how many `get_next()` calls the traversal makes.

1. Now switch to the tail-tracking version (section 2) and add a fifth station. How many `get_next()` calls does this `add` make?
2. If you added 100 stations one at a time, roughly how many total `get_next()` calls would the head-only version make? The tail-tracking version?
3. What field changed to make this possible? Did anything about `Station` itself have to change?

---
### Exercise 2 — `has_next()` vs. `is not None`

Section 1's loop uses `while current.has_next()`. Section 3's loop uses `while current is not None`.

1. Rewrite `add`'s traversal using `while current is not None` instead. Does it still work? What has to change about what happens after the loop?
2. Rewrite `contains`'s traversal using `while current.has_next()` instead. Trace it against a line where the target name is on the *last* station. Does it find it?
3. Based on exercise 2.2, state in one sentence which loop condition is correct for a search that must be able to inspect every station, including the last one.

---
### Exercise 3 — Counting by Hand vs. Counting in Code

Build a line with six stations. Before calling `count()`, count the stations yourself by reading the code that built the line.

1. Does `count()` agree with your manual count?
2. Add a seventh station and call `count()` again without re-reading any code. What had to happen inside `Trainline` for this second call to be correct?
3. Suppose `Trainline` already had a `_size` field, incremented inside `add`. Rewrite `count` to use it instead of traversing. What is the new cost, in Big-O terms?

---
### Exercise 4 — Building and Surviving a Cycle

Build the three-station cycle from section 5 by hand (`a -> b -> c -> a`).

1. Add a loop counter with a cap of, say, 20 to a copy of `count()`. Run it against the cycle. What does it print?
2. Run the same capped version against a normal, non-cyclic three-station line. Does it behave any differently?
3. Without writing the detection algorithm, describe in your own words what information a traversal would need to remember in order to notice it is revisiting a station it has already seen.

---

## Topics Deferred to Later Weeks

- `has_loop()` — detecting a cycle in a linked structure without assuming it (this week's assignment)
- `count()` in $O(1)$ via a maintained field, mirroring `DynamicArray._size` (this week's assignment)
- `last_to_first()` — producing a reversed listing in a single front-to-back traversal (this week's assignment)
- `remove()` on a linked line, including the special case of removing the head or the tail
- Generalizing `Station`/`Trainline` into `Node`/`LinkedList` vocabulary
- Doubly linked structures (a `previous` reference alongside `next`)
- Stacks and queues as restricted interfaces on top of a linked structure

# COMP 271 -- Week 7: `has_loop_bidirectional` in O(1)

Private answer-key note. Not for `comp-271-su26` or any student-facing material -- `week07-assignment.md` and `double_linked_list.py` only pose the problem; this is the reasoning behind the chosen check.

## The candidates

Three ways to test, in $O(1)$, whether a bidirectional `DoubleLinkedList` has been wired into a closed ring (no `None` anywhere) were on the table:

- **s1 -- self-reference at both ends:** `tail._next == tail and head._prev == head`. Each endpoint loops back on itself.
- **s2 -- cross-reference between ends:** `tail._next == head and head._prev == tail`. The two endpoints point at each other, forming one cycle through all nodes.
- **not-None:** `tail._next is not None and head._prev is not None`, regardless of what those pointers actually target.

## s1 and s2 are both real, and neither is exhaustive

s1 and s2 are distinct, buildable fixtures, and both satisfy "no `None` anywhere":

- Under s1, the structure is not one unified ring. Walking forward from `head` reaches `tail` and then spins on `tail` forever, without ever revisiting the earlier nodes. It is a normal chain with both ends clamped shut, not a single cycle.
- Under s2, the whole list is one cycle: walking forward from any node eventually visits every other node and returns to the start.

`s1 or s2` catches both of these. It does **not** catch a third case: `tail._next` wired to some node in the *middle* of the chain (a "lollipop" -- a tail leading into a cycle that does not include the whole list). That configuration also has no `None` at the tail, so it is just as broken by the "never terminates" definition, but it matches neither s1 nor s2.

## Why `not None` is the right check

`add()` is the only method that ever sets pointers on nodes it creates, and it sets both pointers on every node except the two ends: every node except the head gets its `_prev` set (to the old tail) at the time it is added, and every node except the tail gets its `_next` set (to the new node) at the same time. So in a chain built purely by `add()`, the *only* two pointers that can possibly be `None` are `head._prev` and `tail._next`.

Given that invariant, checking whether those two specific pointers are `None` is not an approximation of "is this list fully terminated" -- it is the exact condition, for any chain whose interior was never tampered with directly (which is true of every fixture in this assignment; only `main()`'s test fixtures reach into `Node` objects directly, and only at the two ends). It does not matter what `tail._next` and `head._prev` point to -- self, each other, or some interior node -- only whether they are `None`. That is a strict superset of `s1 or s2`, and it costs the same $O(1)$: two attribute reads.

```python
def has_loop_bidirectional(self) -> bool:
    result = False
    if self._head is not None:
        result = (
            self._tail.get_next() is not None
            and self._head.get_prev() is not None
        )
    return result
```

## Decision

Use the `not None` check. `s1 or s2` is not wrong, but it is narrower than necessary and adds no benefit over the simpler, more general form -- it just special-cases two specific rewirings instead of testing the actual invariant.

The same reasoning underlies `has_loop_unidirectional` in Part 3: `tail._next is not None` is correct there for the identical reason (a forward-only chain built by `add()` can only ever have `tail._next` as `None`), and it was the version already used, unmodified, in that part.

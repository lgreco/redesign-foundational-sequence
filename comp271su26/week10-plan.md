# COMP 271 — Week 10 Plan (Proposed)

*Drafted before any week 10 class session notes exist. Week 10 opens with an async Monday (`monday-async.md`, already posted in the student-facing repo, shared with COMP 170) — students work independently on LeetCode problems (Shift 2D Grid, Add Two Numbers, Two Sum, Reverse String, Palindrome Number, Roman to Integer) plus a non-LeetCode design question: could a queue or stack be built using file operations only, no in-memory lists or arrays. That leaves two live sessions this week, Tuesday and Wednesday. This plan covers those two sessions.*

## Continuity from Week 9

Week 9 finished the circular stack/queue pair, connected pointer wraparound to periodic boundary conditions, and then pivoted into graphs: adjacency lists, adjacency matrices, and `naive_reachability` — a hand-traced BFS-shaped search that visits every reachable vertex before ever checking whether the target was among them. The week 9 assignment asked students to fix exactly that in `better_reachability`, stopping the moment the answer is known, plus a reflection comparing their own week 8 `BoundedCollection`/`Stack`/`Queue` work against the posted solutions.

Several threads from `week08-plan.md`'s deferred list are still fully open and unaddressed by anything in week 9: keeping the $O(1)$ `middle_node` field current across removal, removing an arbitrary (non-end) node from a doubly linked list, circular doubly linked lists, bidirectional iteration, and array-based stack/queue behavior at capacity. None of those get resolved this week either — this plan is a deliberate pivot, not a continuation of the graph thread or a return to that backlog, at the instructor's direction: **week 10 turns back toward object design**, using everything built so far (nodes, generics, contracts via `ABC`, `Stack`/`Queue`, time-complexity comparisons) as raw material for a single applied problem: capturing and ranking search-autocomplete suggestions.

The motivating scenario: type "how is east" into a search box, and the service returns several candidate completions before you finish typing — "how is easter computed," "how is eastern time calculated," and so on. Each keystroke effectively reissues the question and gets back a fresh, ranked list of guesses. The question for this week is deliberately not "how does Google build that list" (out of scope) but the question that starts the moment the list arrives in your program: how do you *capture* it as data, *store* it, and *find the best hit* — and how much of that is just the OOP vocabulary already built over the last nine weeks, pointed at a new problem?

---

## 1. Modeling a Suggestion (Tuesday)

Start from what actually arrives from a service like this: an ordered list of candidate strings, where position in the list already encodes relevance — the first suggestion is (supposedly) the best guess, the last is the weakest. Ask: right now, in this course, what would we do with a plain list of strings like that? (Nothing wrong with a `list[str]` — but nothing in a plain string says "and I was ranked #2," either. That information is currently only implicit in list position, which is fragile the moment the list gets reordered, filtered, or stored somewhere else.)

Introduce a small class that makes the rank explicit data instead of implicit position:

```python
from __future__ import annotations

class Suggestion:
    def __init__(self, text: str, rank: int) -> None:
        self._text = text
        self._rank = rank

    def get_text(self) -> str:
        return self._text

    def get_rank(self) -> int:
        return self._rank

    def __str__(self) -> str:
        return f"#{self._rank}: {self._text}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Suggestion) and self._rank == other._rank

    def __lt__(self, other: Suggestion) -> bool:
        return self._rank < other._rank
```

Name what's genuinely new here and what isn't. `__str__` is not new — `Node` has had one since week 3 or 4, delegating to whatever payload it holds. `isinstance` as a dispatch check isn't new either — it's the same mechanism `add()`'s auto-wrapping used earlier in the course. What's new is `__eq__` and `__lt__`: Python already knows how to compare two `int`s or two `str`s with `<`, because `int` and `str` define what `<` means for their own values. `Suggestion` didn't come with a `<` built in — nothing does, for a class you write yourself — so without `__lt__`, `suggestion_a < suggestion_b` would raise a `TypeError`. Writing `__lt__` is what makes `<` mean something for this class at all, and it's free to mean *anything* the class wants — here, "lower rank number wins."

Trace it live: construct two or three `Suggestion` objects by hand, confirm `<` works between them, and confirm it raises `TypeError` on a `Suggestion` compared against a plain string.

---

## 2. Finding the Best Hit Without Sorting (Tuesday, continued)

Given a list of `Suggestion` objects, the immediate question is: which one is best? Two ways to answer, both worth building so the class can compare them:

```python
def best_by_sorting(suggestions: list[Suggestion]) -> Suggestion:
    return sorted(suggestions)[0]

def best_by_scanning(suggestions: list[Suggestion]) -> Suggestion:
    best = suggestions[0]
    for candidate in suggestions[1:]:
        if candidate < best:
            best = candidate
    return best
```

Both work, and both work *only* because `__lt__` is defined — `sorted()` calls it under the hood exactly as many times as it needs to, and `best_by_scanning`'s `if candidate < best:` calls it once per remaining element. Ask the class to name the cost difference before running anything: sorting the whole list to read off the first element is $\mathcal O(n \log n)$; a single left-to-right scan that keeps only the best-seen-so-far is $\mathcal O(n)$. Naming the smaller cost is the same instinct as week 9's array-vs-circular-buffer complexity table — do only the work the question actually requires.

This is also a direct payoff of section 1's design choice: once `Suggestion` knows how to compare itself, *every* piece of code that ever needs "the best one" — a sort, a scan, a `min()` call — gets to ask the same simple question (`<`) instead of reaching back into `._rank` by hand each time. Show `min(suggestions)` as a third option that also works, for the same reason.

---

## 3. Refining "Best": More Than One Signal (Wednesday)

Google's own rank is one signal, but it isn't the only one worth having. Suppose the user's actual intended query, once they finish typing, is "how is easter computed" — some candidates in the mid-typing suggestion list will turn out to share more of that final text than others, independent of where Google happened to rank them at the time.

Add a second, simple signal — not full edit distance, just a character-by-character prefix match against a known target:

```python
def prefix_match_length(candidate: str, target: str) -> int:
    length = 0
    for i in range(min(len(candidate), len(target))):
        if candidate[i] != target[i]:
            break
        length += 1
    return length
```

Extend `Suggestion` to hold this second score and fold both signals into one comparison:

```python
class Suggestion:
    def __init__(self, text: str, rank: int, match_length: int) -> None:
        self._text = text
        self._rank = rank
        self._match_length = match_length

    def __lt__(self, other: Suggestion) -> bool:
        # Prefer a longer prefix match first; break ties by Google's own rank.
        if self._match_length != other._match_length:
            return self._match_length > other._match_length
        return self._rank < other._rank
```

Name the point directly: nothing about `best_by_scanning` from section 2 had to change at all. It only ever asked `candidate < best` — every bit of the new, two-part decision logic is hidden entirely behind that one operator, inside `Suggestion` itself. This is encapsulation earning its keep: the *caller* of `<` never needs to know whether "better" means one thing or three things combined.

Flag explicitly what this is not doing: real search-relevance ranking blends many more signals (click-through history, personalization, typo tolerance) and true edit distance (Levenshtein) would let "eastr" match "easter" even with a letter dropped — neither is in scope this week. `prefix_match_length` is intentionally the simplest possible second signal, chosen to demonstrate *that* composite comparisons are possible, not to be a realistic ranking function.

---

## 4. Naming the Bigger Structure, Briefly (Wednesday, continued)

Close by asking: everything this week assumed the list of suggestions just *arrives*, already computed. In a real system, something has to generate that list, fast, every time a user presses a key — scanning every known phrase in the world on every keystroke clearly doesn't scale. Name, without building, the structure real autocomplete systems use for this: a **trie** (prefix tree) — a tree where each node represents one character, and following a path from the root spells out a prefix, so every phrase sharing that prefix is reachable from the same branch. It's the same node-and-pointer instinct behind every linked structure built so far this course, just branching by character instead of chaining by "next." This is a preview, not an assignment — the course has not yet built a tree of any kind, and a full trie implementation is a natural candidate for a later week or for COMP 272.

---

## Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| `__eq__` / `__lt__` | Dunder methods that give a user-defined class a meaning for `==` and `<`; without them, comparing two instances raises `TypeError` |
| Operator overloading for ranking | The same `<` syntax used for numbers can mean "is a better search suggestion than," once a class defines it that way |
| Scan-for-best vs. sort-then-take-first | Both correctly find the minimum of a comparable sequence; scanning is $\mathcal O(n)$, sorting first is $\mathcal O(n \log n)$ for the same answer |
| Composite comparison key | Folding more than one signal (match length, then rank as a tiebreaker) into a single `__lt__`, hidden behind one operator |
| Encapsulation payoff | A caller writing `a < b` never needs to know how many signals, or what logic, decide the answer inside `__lt__` |
| Trie (preview only) | A tree that branches by character rather than chaining by "next" -- the structure real autocomplete systems use to generate suggestions quickly; not built this week |

---

## Reading

| Topic | Source |
|---|---|
| Classes, instance methods, `self` (background for `Suggestion`) | [The Python Tutorial — Classes — docs.python.org](https://docs.python.org/3/tutorial/classes.html) |
| Objects and classes (reference) | [Objects — Lubanovic ch. 11](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch11.html) |
| Dunder / special methods (`__eq__`, `__lt__`) and operator overloading | *placeholder — no dedicated docs.python.org or Lubanovic entry yet in the comp-271-su26 reading tables; flag for instructor to add (likely docs.python.org's "Data Model" special-methods reference)* |
| Time complexity of sorting vs. a single scan | *placeholder — no existing entry in the comp-271-su26 reading tables covers Big-O of sorting; flag for instructor to add* |

---

## Exercises

---
### Exercise 1 — Why `<` Fails Without `__lt__`

Given `class Point: def __init__(self, x): self.x = x`, with no `__lt__` defined, what happens when you evaluate `Point(1) < Point(2)`? Name the exact exception, and explain in one sentence why Python has no way to guess what "less than" should mean for an arbitrary class.

---
### Exercise 2 — Tracing the Scan

Given `suggestions = [Suggestion("a", 3), Suggestion("b", 1), Suggestion("c", 2)]` and the rank-only `__lt__` from section 1, trace `best_by_scanning(suggestions)` by hand, one comparison at a time.

1. What is `best` after each iteration of the loop?
2. How many total calls to `__lt__` does this trace make? How many would `best_by_sorting` make on the same list (you don't need Python's exact sort algorithm -- just reason about whether it's more or fewer than the scan)?

---
### Exercise 3 — Building the Composite `__lt__`

Given the two-signal `Suggestion` from section 3, construct `Suggestion("how is easter computed", 4, 20)` and `Suggestion("how is eastern time", 0, 12)`.

1. Which one is `<` the other? Walk through exactly which branch of `__lt__` decides it.
2. Construct a third `Suggestion` with the same `match_length` as one of the two above but a different `rank`. Which comparison branch resolves that case?

---
### Exercise 4 — Where Would a Stack or Queue Fit?

Suppose suggestions arrive one keystroke at a time -- "how i", then "how is", then "how is e" -- each producing its own fresh list of `Suggestion` objects.

1. If you wanted to keep a history of the last five keystrokes' suggestion lists so a user could "undo" back to an earlier one, would a `Stack` or a `Queue` from week 8 fit better? Why?
2. Does anything about `Suggestion`'s `__lt__` need to change to support that history feature? Why or why not?

---
### Exercise 5 — The Trie Preview

Without writing code, sketch (in words or a drawing) how the phrases "cat," "car," and "cart" would share structure in a trie, character by character.

1. At what point do the three phrases stop sharing the same path from the root?
2. How is this similar to, and different from, the `Node`-and-pointer structures already built this course (e.g., a linked list)?

---

## Topics Deferred to Later Weeks

- Keeping the $O(1)$ middle-node field from week 7 current across `remove_from_head`/`remove_from_tail` -- carried forward unchanged from `week08-plan.md`, still open
- Removing an arbitrary (non-end) node from a doubly linked list -- carried forward unchanged, still open
- Circular doubly linked lists -- carried forward unchanged, still open
- Iterating a doubly linked list in both directions (`__iter__` forward and backward) -- carried forward unchanged, still open
- Array-based (fixed-capacity) stack/queue implementations at capacity -- carried forward unchanged, still open
- Tries (prefix trees) -- previewed in section 4, not built
- True edit distance (Levenshtein) as a more realistic third ranking signal
- Generalizing composite comparison keys into a reusable "sort key function" pattern, rather than hard-coding tiebreak order inside `__lt__`
- Returning to the week 9 graph/reachability thread, and to `better_reachability`'s BFS-vs-DFS shape specifically

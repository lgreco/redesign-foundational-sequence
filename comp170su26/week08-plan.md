# COMP 170 — Week 8 Plan

## Continuity from Week 7

Week 7 turned week 6's single-character pseudocode into working code: `find.py` (`find_char`, mirroring the `str.find()`/`str.index()` failure-mode contrast), `demo_contains.py` (`contains`/`index_of` on a list), and `occurrences.py` (counting matches, with a guard clause for missing input). Along the way it introduced definite vs. indefinite loops and Boolean `and` conditions inside `while` guards. The week 7 assignment then pushed one step further, but only as far as pseudocode: Problem 1 asks for `positions`, a method that returns *every* position where a letter appears in a string, as a list; Problem 2 asks for substring search — finding where one whole string begins inside another, mirroring `str.find()` when it is given a multi-character argument instead of a single character.

Week 8 does to week 7's pseudocode what week 7 did to week 6's: turns it into real Python, and in doing so introduces the two pieces of machinery each problem actually needs. `positions` needs a method that builds and returns a list — reconnecting to week 5's `result = []` / `.append()` pattern, but for the first time doing so inside a `def` with a `return`, not a bare script variable ending in `print()`. Substring search needs nested iteration — checking, at each candidate starting position, whether an entire sequence of characters matches — which is the course's first genuine nested loop, a topic explicitly deferred all the way back in week 4 ("Nested `for` loops (two-dimensional patterns)").

---

## 1. Building a List Inside a Method: `positions`

Live-code the `positions` pseudocode from the week 7 assignment together. Contrast it directly with `find_char`: `find_char` stops the instant it finds a match, because it only wants the first one. `positions` must *not* stop early — it has to keep checking every remaining position even after a match, because there could be more. This is the live answer to the week 7 assignment's Problem 3 reflection question ("what had to change to go from finding the first match and stopping, to finding every match") — use that question as the bridge into today's code.

```python
def positions(letter, text):
    matches = []
    position = 0
    while position < len(text):
        if text[position] == letter:
            matches.append(position)
        position += 1
    return matches
```

Trace `positions('a', 'banana')` by hand, position by position, and confirm it produces `[1, 3, 5]`.

Name what's new here explicitly: this is the same accumulator-list pattern from week 5 (`long_words = []`, then `.append()` inside a loop) — but this is the first time that pattern lives inside a method body, ending in `return matches` instead of a script ending in `print(long_words)`. Also name why an empty list, not `-1`, is the right "not found" value: `-1` is a number pretending to mean "not found"; here the return type is always a list, so "nothing found" is simply the list with nothing in it — no sentinel value has to be invented. Tie this back to week 6 Problem 3's empty-string guard in `is_word`: not every "absent" case needs a magic value; sometimes the natural empty case already says what's needed.

---

## 2. Nested Loops: Does the Whole Target Match, Starting Here?

Motivate the jump: every method built so far — `find_char`, `occurrences`, `positions` — compares one character at a time to one target character. Substring search asks a different question at each position: not "is this one character a match" but "does this whole sequence of characters match, starting here." Answering that requires two loops working together: an **outer loop** that tries each candidate starting position in the text, and an **inner loop** that steps through the target string character by character to confirm the match before the outer loop moves on. Name this explicitly: a **nested loop** — a loop whose body contains another complete loop.

Build pseudocode into code together using the assignment's own example — `"cag"` inside `"Chicago"`, expected answer `3`:

```python
def find_substring(target, text):
    start = 0
    while start <= len(text) - len(target):
        offset = 0
        match = True
        while offset < len(target) and match:
            if text[start + offset] != target[offset]:
                match = False
            offset += 1
        if match:
            return start
        start += 1
    return -1
```

Trace `find_substring("cag", "Chicago")` and confirm it returns `3`. Walk through a failing starting position too (e.g., `start = 0`, comparing `"cag"` against `"Chi"`) and point out that the inner loop's `and match` condition stops it the instant one character fails — the same "stop as soon as you know the answer" instinct from `find_char`, just operating one level up, inside the inner loop instead of the outer one.

Handle the bounds case the assignment explicitly asks about: what if `target` is longer than the remaining text? Show that this falls out naturally from the outer loop's own condition (`start <= len(text) - len(target)`) rather than needing a separate check up front — have students verify this by hand with a `target` longer than the whole `text` and confirm the loop body never runs at all.

Name the cost difference informally — no formal complexity notation in this course yet, just the observation that a single loop looks at each character once, while a nested loop can look at the same characters again and again, once per candidate starting position tried. Longer targets and longer texts both mean more total work; leave it at that.

---

## 3. Zooming Out: What Every Method Built So Far Has in Common

Use the week 7 assignment's Problem 3 reflection questions as a discussion anchor rather than a separate lecture topic: the stop-early behavior of `find_char` versus the must-check-everything behavior of `is_word` and `positions`; the ASCII range test in `to_upper`; the empty-string guard in `is_word`. Have students articulate out loud the shape shared by every method built since week 6: set up state before the loop, check one thing per iteration, decide whether to stop early or keep going, report an answer at the end. This is a deliberate "name the pattern" moment before next week adds more machinery on top of it.

---

## Track 2: The Quadratic Equation — From Prints to Tuples to Complex Solutions

A second, independent thread for week 8: revisit `quad.py`, the standalone quadratic-equation script used earlier in the course, and push it through the same upgrade `positions` just went through in Track 1 — from a method that only prints, to one that returns a value the caller can actually use. This thread does not depend on nested loops or on anything else in Track 1; it can run in whichever session fits best.

### 4. Where `quad.py` Left Off

Put `quad.py` back on the screen:

```python
from math import sqrt

def solve_quadratic_equation(a: float, b: float, c: float):
    discriminant = b*b - 4*a*c
    if discriminant >= 0:
        x1 = (-b-sqrt(discriminant))/(2*a)
        x2 = (-b+sqrt(discriminant))/(2*a)
        print(x1, x2)
    else:
        print("Sorry, no real solutions for this equation.")
```

Name what it does and does not do. It correctly separates "has real solutions" from "does not," but it treats `discriminant > 0` (two distinct roots) and `discriminant == 0` (one repeated root) as the same case — worth naming out loud as a third mathematical case the code currently glosses over. More importantly: every branch ends in `print`. The solutions appear on the screen and are gone; nothing about them is available to the rest of the program. Ask directly: what if another part of a program needed `x1` and `x2` to keep computing — say, to check them by substituting back into the original equation? `print` cannot help with that.

### 5. Returning the Solutions: Introducing the Tuple

Rewrite `solve_quadratic_equation` to return its answer instead of printing it — and since there are up to two solutions to hand back at once, introduce the **tuple**:

```python
def solve_quadratic(a: float, b: float, c: float) -> tuple:
    """Solve a*x^2 + b*x + c = 0. Returns (x1, x2) if real solutions
    exist, or an empty tuple () if they do not."""
    solutions = ()
    discriminant = b * b - 4 * a * c
    if discriminant >= 0:
        x1 = (-b - sqrt(discriminant)) / (2 * a)
        x2 = (-b + sqrt(discriminant)) / (2 * a)
        solutions = (x1, x2)
    return solutions
```

Trace `solve_quadratic(1, -3, 2)` (expect `(1.0, 2.0)`) and `solve_quadratic(1, 2, 3)` (expect `()`), then name why the empty tuple, not `-1` or `None`, is the right way to say "no solutions" here — the exact same design choice `positions` made in Track 1, section 1, just with a tuple instead of a list.

**Tuple vs. list**, side by side on the board:

| | List | Tuple |
|---|---|---|
| Written as | `[x1, x2]` | `(x1, x2)` |
| Can change after creation? | Yes — `.append()`, item assignment, `.remove()` | No — immutable; `t[0] = 5` raises `TypeError` |
| Says to a reader... | "a sequence I might grow, shrink, filter, or loop over" | "a fixed-size bundle of values that belong together, in this order" |
| Right fit here because... | — | the equation always has exactly 0 or 2 real solutions — the size is fixed and known, so a tuple says so honestly |

CS1-appropriate uses of a tuple worth naming: returning more than one value from a method (`return x1, x2` is shorthand for `return (x1, x2)` — the parentheses are optional but the comma is what makes it a tuple), unpacking a result directly into two names (`sol1, sol2 = solve_quadratic(1, -3, 2)`), and representing any small, fixed-position bundle where each position has a distinct meaning — a coordinate `(x, y)`, an RGB color `(r, g, b)`, or here, `(smaller_root, larger_root)`.

### 6. Generalizing to Complex Solutions

When the discriminant is negative, the equation still has solutions — they are just not real numbers:

$$x = \frac{-b}{2a} \pm i\,\frac{\sqrt{-(b^2-4ac)}}{2a}$$

Both roots share the same real part; only the sign of the imaginary part differs. Generalize `solve_quadratic` so the *shape* of the returned tuple communicates which kind of solution it holds:

```python
def solve_quadratic(a: float, b: float, c: float) -> tuple:
    """Solve a*x^2 + b*x + c = 0.

    Returns (x1, x2) if the discriminant is >= 0 (real solutions), or
    ((re1, im1), (re2, im2)) if the discriminant is < 0 (complex
    solutions) -- a tuple of two tuples, each holding one solution's
    real and imaginary part.
    """
    discriminant = b * b - 4 * a * c
    if discriminant >= 0:
        x1 = (-b - sqrt(discriminant)) / (2 * a)
        x2 = (-b + sqrt(discriminant)) / (2 * a)
        solutions = (x1, x2)
    else:
        real_part = -b / (2 * a)
        imaginary_part = sqrt(-discriminant) / (2 * a)
        solutions = ((real_part, -imaginary_part), (real_part, imaginary_part))
    return solutions
```

Trace `solve_quadratic(1, 2, 5)`: the discriminant is $4 - 20 = -16$, so the expected return is `((-1.0, -2.0), (-1.0, 2.0))`. Name the new idea directly: a **tuple of tuples** — the outer tuple still means "two solutions," but each inner tuple is itself a fixed-size, two-position bundle, `(real part, imaginary part)`.

Name the design tension honestly rather than hiding it: the shape of what comes back now depends on the input. Calling code has to know in advance — or check — whether it received `(x1, x2)` or `((re1, im1), (re2, im2))` before it can safely unpack the result. Put the question to the class directly: is a method whose return shape changes based on its input harder to use correctly than one that always returns the same shape? What would a caller have to do to use this safely? (No need to resolve it by rewriting everything as complex numbers this week — just name the tradeoff.)

### 7. Handling `a = 0` Without Crashing

Every version so far divides by `2 * a`. If `a` is `0`, that is division by zero — a crash, not a "no solution" answer. Ask first: mathematically, what *is* the equation when `a = 0`? It is no longer quadratic — `b*x + c = 0` is linear, and if `b` is *also* `0`, there is no `x` left in the equation at all.

```python
def solve_quadratic(a: float, b: float, c: float) -> tuple:
    solutions = ()
    if a != 0:
        discriminant = b * b - 4 * a * c
        if discriminant >= 0:
            x1 = (-b - sqrt(discriminant)) / (2 * a)
            x2 = (-b + sqrt(discriminant)) / (2 * a)
            solutions = (x1, x2)
        else:
            real_part = -b / (2 * a)
            imaginary_part = sqrt(-discriminant) / (2 * a)
            solutions = ((real_part, -imaginary_part), (real_part, imaginary_part))
    elif b != 0:
        # a == 0: not quadratic anymore, just b*x + c = 0.
        solutions = (-c / b,)
    # a == 0 and b == 0: either every x satisfies c == 0 (infinitely
    # many solutions) or no x does (c != 0). Neither can be reported
    # as a finite tuple of numbers, so the empty tuple stands for both
    # -- an honest limitation to name, not to hide.
    return solutions
```

Walk through why checking `a != 0` first — before ever computing `discriminant` or dividing by `2 * a` — is what prevents the crash. This is the same "guard before you divide" instinct as `occurrences`'s missing-input guard from week 7. Trace `solve_quadratic(0, 2, -6)` (expect `(3.0,)`, a **one-element tuple** — note the comma; `(3.0)` alone is just the number `3.0` in parentheses, not a tuple) and `solve_quadratic(0, 0, 5)` (expect `()`).

---

## Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| Building a list inside a method | Accumulating results with `.append()` inside a `def`, then `return` instead of `print` |
| Nested loop | A loop whose body contains another complete loop |
| Outer loop / inner loop | The outer loop picks a candidate; the inner loop verifies it fully before the outer loop moves on |
| Early exit inside a nested loop | Stopping the inner loop the instant one character fails, without finishing it |
| Bounds check via loop condition | Letting a loop's own condition (`start <= len(text) - len(target)`) rule out impossible cases, instead of a separate `if` |
| Tuple | An ordered, fixed-size, immutable collection of values |
| Tuple vs. list | Tuple: fixed size, immutable, each position has a distinct meaning. List: variable length, mutable, elements are usually alike |
| Returning multiple values | `return a, b` is shorthand for `return (a, b)` — a method can hand back more than one value at once |
| Tuple of tuples | A fixed-size bundle whose elements are themselves fixed-size bundles — here, `((re1, im1), (re2, im2))` |
| Guard before you divide | Checking `a != 0` before computing `2 * a` in a denominator avoids `ZeroDivisionError` entirely |

---

## Reading

| Topic | Source |
|---|---|
| Loops, including a loop nested inside another | [Chapter 7: Loops — Lubanovic](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch07.html) · [for Statements — docs.python.org](https://docs.python.org/3/tutorial/controlflow.html#for-statements) |
| Lists and `.append()` | [Chapter 8: Lists — Lubanovic](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch08.html#c08_h_list_create) |
| Building and returning a value from inside a method | [Chapter 10: Functions — Lubanovic](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch10.html) · [Defining Functions — docs.python.org](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) |
| Tuples, and how they differ from lists | *placeholder — no link yet in the comp-170-su26 reading tables; flag for instructor to add* |

---

## Exercises

---
### Exercise 1 — `positions`, Traced by Hand

Before running anything, trace `positions('e', 'settlement')` by hand, position by position.

Questions:
1. How many total loop iterations does `positions` run on this input? Compare that to how many iterations `find_char` would run looking for the *first* `'e'` only — why is the difference expected?
2. What does `positions('z', 'settlement')` return, and why is an empty list the right answer here rather than `-1`?

---
### Exercise 2 — `find_substring`, Traced by Hand

Trace `find_substring("liga", "colligate")` by hand.

Questions:
1. At the starting position where the match ultimately succeeds, how many inner-loop iterations run before `match` is confirmed `True`?
2. Pick a starting position where the match fails on the very first character compared. How many inner-loop iterations run there before the inner loop gives up?

---
### Exercise 3 — When the Target Is Longer Than the Text

Call `find_substring("elephant", "cat")`.

Questions:
1. Using the actual lengths of `"elephant"` and `"cat"`, evaluate the outer loop's condition (`start <= len(text) - len(target)`) before the loop ever runs. Does the loop body execute even once?
2. Why does this behavior fall out of the loop condition itself, rather than requiring a separate `if len(target) > len(text): return -1` check before the loop?

---
### Exercise 4 — Combining Both: Every Occurrence of a Substring

Challenge: sketch pseudocode (Python optional) for `find_all_substrings(target, text)`, which returns a list of *every* starting position where `target` begins in `text`, not just the first — combining today's two methods.

Questions:
1. What has to change about `find_substring`'s "stop and return the position" logic to keep going and collect more matches instead?
2. Using `find_all_substrings("ana", "banana")` as a test case, what should the function return, and how many positions is that?

---
### Exercise 5 — Tuple vs. List, by Hand

Given `result = solve_quadratic(1, -3, 2)`, try `result.append(10)` and then `result[0] = 99`.

Questions:
1. What error does each line raise, and why does that error make sense for a tuple?
2. Rewrite the same two lines using a list instead (`result = [1.0, 2.0]`). Do they raise errors now? What changed?

---
### Exercise 6 — Tracing the Three Cases

Trace `solve_quadratic(1, -3, 2)`, `solve_quadratic(1, 2, 1)`, and `solve_quadratic(1, 2, 5)` by hand — one call for each sign of the discriminant (positive, zero, negative).

Questions:
1. What does each call return, and which of the three has a different *shape* (plain tuple of numbers vs. tuple of tuples) than the other two?
2. `solve_quadratic(1, 2, 1)` (the repeated-root case) returns a tuple with the same value twice. Should this case instead return a single value? Argue for one choice or the other.

---
### Exercise 7 — Handling `a = 0`

Trace `solve_quadratic(0, 2, -6)`, `solve_quadratic(0, 0, 5)`, and `solve_quadratic(0, 0, 0)` by hand.

Questions:
1. Which of the three calls returns a one-element tuple, and which return an empty tuple?
2. `solve_quadratic(0, 0, 0)` and `solve_quadratic(0, 0, 5)` both return `()`, even though mathematically one has infinitely many solutions and the other has none. Is this a problem? What would you change about the return value if you wanted the two to be distinguishable?

---
### Exercise 8 — Unpacking the Result

Call `sol = solve_quadratic(1, -3, 2)`, then write `x1, x2 = sol`.

Questions:
1. What are `x1` and `x2` after this line?
2. Try the same unpacking (`x1, x2 = sol`) on the result of `solve_quadratic(1, 2, 5)` (the complex case). What do `x1` and `x2` actually hold now, and why might that surprise a caller who expected two plain numbers?

---

## Topics Deferred to Later Weeks

- `find_all_substrings` — finding every occurrence of a whole substring, not just the first (previewed in Exercise 4, not built in class this week)
- Counting occurrences of a substring, as opposed to a single character (week 7's `occurrences` only ever counted one character)
- Two-dimensional patterns using nested loops (deferred since week 4; today's nested loop is search-shaped, not grid-shaped)
- Slicing (`text[i:j]`) as a possible shortcut for the inner-loop comparison — deferred until slicing itself is introduced
- Python's built-in `complex` number type (`3+4j`) as an alternative to the hand-built `(real, imaginary)` tuple
- Rewriting `solve_quadratic` so every case — real or complex — returns the same uniform shape, resolving the design tension named in section 6
- Distinguishing "infinitely many solutions" from "no solutions" when `a == 0` and `b == 0` (both currently collapse to the empty tuple)
- Named tuples (`collections.namedtuple`) as a way to label a tuple's positions with names instead of only positions

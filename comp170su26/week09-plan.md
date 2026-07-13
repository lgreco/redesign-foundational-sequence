# COMP 170 — Week 9 Plan (Proposed)

*This is a proposed plan, drafted before any week 9 class session notes exist. It is built from the week 8 plan, the actual week 8 session notes (July 6–8), the week 8 assignment, and the week 7 posted solutions. Some things the week 8 plan intended to teach live did not end up happening that way — see the continuity note below — so this plan accounts for what actually happened in the room, not just what was scheduled.*

## Continuity from Week 8

Week 8 did not run exactly as `week08-plan.md` sketched it. The plan's Track 1 (live-coding `positions` and `find_substring`, the nested-loop material) never happened in class — instead, `positions` and `find_substring` only reached students as **posted solutions** (`week07-solutions.md`), and the week 8 assignment's Problem 4 asked students to *reflect* on those solutions rather than derive them live. What actually filled the three sessions was the plan's Track 2 and more: revisiting `quad.py`, introducing complex numbers and the tuple-vs-list distinction, building `solve_quadratic()` up through the $a=0$ special case, comparing three levels of testing (naive `if`/`else`, plain helper functions, and a first look at `unittest`), and then a full session on designing `enter_grade` for a GPA tracker — which is where `raise ValueError` entered the course for the first time, prompted by two live bugs (a lowercase letter and a mistyped letter both silently scoring as zero).

That means two threads are open heading into week 9:

1. **Nested loops (`positions`, `find_substring`) have been *read*, not *worked*.** Students saw the pseudocode-to-code mapping and answered reflection questions about it, but nobody has traced these functions on the board or watched them run. Before building anything new on top of "search," it's worth closing this loop explicitly rather than assuming it landed.
2. **`raise ValueError` was introduced but never *caught*.** The week 8 assignment's tutorial section showed a `try`/`except` example as a read-along, and Problem 3 asked students to use `try`/`except` to test that `withdraw`/`deposit` raise correctly — but nobody has yet written a program that raises an error, catches it, and *keeps running* instead of crashing or just printing a pass/fail line. The `withdraw(amount, balance)` / `deposit(amount, balance)` assignment students are submitting going into week 9 is exactly the raw material for this.

Week 9 opens by debriefing that assignment, then uses it as the bridge into catching errors for real, and introduces dictionaries as a cleaner way to express the kind of letter-to-number lookup `enter_grade` currently does with a stack of `if` checks.

---

## 1. Debrief: Withdraw, Deposit, and the Order of Checks

Open by putting a few real student submissions of `withdraw(amount, balance)` on the screen (anonymized). The assignment's whole point was that checking "is `amount` a multiple of \$20" has to happen *before* checking "does `balance` cover it" — walk through at least one submission that got this order backwards and show a case where it produces a misleading error message (e.g. `withdraw(150, 100)`: is the problem that \$150 isn't available, or that \$150 isn't a multiple of \$20? it's actually neither check's fault until you decide which one runs first).

Do the same for `deposit`'s dollars-and-cents check (`amount * 100`, then `% 1` or comparing to `round()`), since this is the first time the course has validated a *float's shape* rather than just its sign or size.

Close with a quick, explicit trace of `positions('e', 'settlement')` and `find_substring("liga", "colligate")` on the board — the two functions from the posted week 7 solutions that were never actually run in front of the class. Five minutes each; the goal is confirming the pattern (accumulate-and-return vs. nested-loop-with-early-exit) actually landed, not re-teaching it.

---

## 2. Catching Errors: `try`/`except` for Real

Motivate directly from `withdraw`: right now, calling `withdraw(50, 200)` crashes the whole program. That's the correct behavior *inside* `withdraw` — an invalid amount really should stop that function cold — but a real program calling `withdraw` on behalf of a user shouldn't die because the user fat-fingered an amount. Introduce `try`/`except` as the tool that lets a caller decide what "invalid input" means to *it*, without changing what `withdraw` does:

```python
while True:
    amount = int(input("How much would you like to withdraw? "))
    try:
        balance = withdraw(amount, balance)
        print(f"Success. New balance: ${balance}")
        break
    except ValueError as error:
        print(f"That didn't work: {error}")
        print("Try again.")
```

Name what's new: this is the course's first **indefinite loop built to recover from bad input** rather than just to repeat a computation (`while True` + `break` on success, echoing the definite-vs-indefinite distinction from week 7, now put to a new use). Trace it with a bad amount first (not a multiple of \$20), then a good one, and point out that the loop's `except` block runs and the loop *continues* — nothing crashes, nothing exits early on the bad attempt.

Contrast this explicitly with Problem 3 from the week 8 assignment, where `try`/`except` was used only to confirm an error *was* raised, inside a one-shot test. Here it's used for the opposite purpose: to keep a program alive in spite of an error. Same syntax, different job — worth naming that distinction out loud.

### 2a. The Bug Hiding in the Example Above

Put the section 2 loop back on the screen and ask the class to break it: what happens if a user types `fifty` instead of `50`? Run it. `int(input(...))` crashes with its own `ValueError` — `invalid literal for int() with base 10: 'fifty'` — and the crash happens *before* the `try` block even starts, because the conversion sits outside it. The `try`/`except` students just watched work does nothing here, and it's worth letting that surprise land before fixing it.

The fix is to widen what the `try` block covers, so the conversion is protected too:

```python
while True:
    try:
        amount = int(input("How much would you like to withdraw? "))
        balance = withdraw(amount, balance)
        print(f"Success. New balance: ${balance}")
        break
    except ValueError as error:
        print(f"That didn't work: {error}")
        print("Try again.")
```

Name why one `except ValueError` is enough to cover two completely different failures — a bad conversion (`int('fifty')`) and a bad withdrawal (`withdraw(150, 100)` when \$150 isn't a multiple of \$20) — even though they happen in different lines and different functions: Python doesn't stop to ask which line raised the error; the moment *any* line inside `try` raises a `ValueError`, control jumps straight to `except`, skipping whatever was left in the `try` block. Trace both failure cases by hand and confirm the printed message is different each time (`error` holds whatever message the failing line attached), even though the same `except` line catches both.

### 2b. Two Ways to Guard Against the Same Mistake

Put `withdraw`'s own internal guard clause (`if amount % 20 != 0: raise ValueError(...)`) side by side with the `try`/`except` that surrounds a *call* to `withdraw`. These are two different idioms for handling the same category of mistake, and CS1 students will see both named elsewhere, so name them here first:

- **Look Before You Leap (LBYL):** check the condition *before* acting — this is what every guard clause in `withdraw` and `enter_grade` already does (`if amount % 20 != 0: raise ...` before ever touching `balance`).
- **Easier to Ask Forgiveness than Permission (EAFP):** just try the risky thing, and handle it if it fails — this is what the `try`/`except` around the *call site* does.

Point out that both idioms are doing real work in the same program at the same time: `withdraw` itself is written LBYL-style (it checks before it commits to a withdrawal), while the code calling `withdraw` is written EAFP-style (it doesn't pre-check whether the amount will be valid — it just calls `withdraw` and reacts if that fails). Neither idiom is "more correct"; a function's own guard clauses protect its internal logic, and a caller's `try`/`except` protects the *program* from a function's guard clauses doing their job loudly.

### 2c. Catching More Than One Kind of Failure

Extend the example with a second failure mode: what if `withdraw` and `deposit` are both being called from the same menu-driven loop, and either one might raise? Show that one `except` line can list more than one exception type, using a tuple:

```python
try:
    choice = input("Withdraw or deposit? ")
    amount = int(input("Amount: "))
    if choice == "withdraw":
        balance = withdraw(amount, balance)
    else:
        balance = deposit(amount, balance)
except (ValueError, TypeError) as error:
    print(f"That didn't work: {error}")
```

`deposit` and `withdraw` both only ever raise `ValueError` in this course so far, so `TypeError` is included here purely as an example of the *syntax* for catching more than one kind of exception at once — name the parentheses as what makes it a tuple of exception types, directly echoing the tuple syntax from week 8.

Contrast this with a **bare** `except:` (no exception type named at all), and why it's a trap, not a shortcut: it catches *everything*, including a typo like calling `withdrw(amount, balance)` (a `NameError`, not a `ValueError`) or forgetting a colon (a `SyntaxError`, though that one happens before the program even runs). A bare `except:` would silently swallow that typo and print "that didn't work" as though the *user's* input was the problem, hiding a real bug in the program itself. Naming the exact exception type you expect is what keeps `except` from turning into a blindfold.

---

## 3. Dictionaries: Replacing a Chain of `if`s with a Lookup

Put `enter_grade` from `gpa.py` back on the screen. Point at the four `if letter == 'X': grade = Y` lines and ask: what is this really doing? It's a **lookup** — given a key (`'A'`), find a value (`4.0`) — but it's written as a sequence of comparisons instead of stated as a lookup directly.

Introduce the **dictionary** as Python's built-in way to say that directly:

```python
grade_values = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
grade = grade_values[letter]
```

Rewrite `enter_grade` using it, keeping the existing guard clauses:

```python
def enter_grade(letter: str, gpa: float) -> float:
    letter = letter.upper()
    grade_values = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    if letter not in grade_values:
        raise ValueError('Oops, you must enter A, B, C, D, or F')
    if gpa < 0:
        raise ValueError('Oops, current GPA cannot be negative')
    grade = grade_values[letter]
    return (gpa + grade) / 2
```

Name the direct callback to week 8: `letter not in 'ABCDF'` already used `in` to check membership in a string; `letter not in grade_values` uses the *exact same operator* to check membership among a dictionary's **keys** — same idea, richer container. Put dictionaries next to lists and tuples on the board as a third way to hold multiple values, and be explicit about what distinguishes them:

| | List | Tuple | Dictionary |
|---|---|---|---|
| Written as | `[x1, x2]` | `(x1, x2)` | `{'A': 4.0, 'B': 3.0}` |
| Found by... | position (`x[0]`) | position (`x[0]`) | key (`x['A']`) |
| Right fit when... | order matters, might grow/shrink | a fixed-size bundle where position has meaning | you look things up by name, not position |

Close by revisiting `solve_quadratic`'s branch-by-branch case table from week 8 (the `(a,b,c)` cases table in `2026-07-07-COMP170.md`) and asking: would a dictionary help anywhere in that function? (It wouldn't, directly — there's no natural "key" for a quadratic's coefficients — which is itself a useful negative example: dictionaries fit *lookup by name*, not every multi-value situation.)

---

## Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| Catching an error | `try`/`except` lets a caller recover from a `raise`d error instead of crashing |
| Recovery loop | `while True` with a `try`/`except` inside and `break` on success — an indefinite loop built to retry, not just repeat |
| What a `try` block covers | Only code physically inside `try` is protected — a risky line left outside it (like an unguarded `int(input(...))`) still crashes the program |
| LBYL vs. EAFP | Look Before You Leap (guard clauses that check first) vs. Easier to Ask Forgiveness than Permission (`try`/`except` that acts first and reacts to failure) — two idioms for the same category of problem |
| Catching multiple exception types | `except (ValueError, TypeError) as error:` catches either kind in one clause, using the same tuple syntax as week 8 |
| Bare `except:` as a trap | Catching everything, with no exception type named, silently swallows real bugs (typos, `NameError`) alongside the input errors it was meant to catch |
| Dictionary | A collection of key-value pairs, looked up by key instead of by position |
| Membership in a dictionary | `key in some_dict` checks the dictionary's keys, the same `in` operator used for strings and lists |
| Lookup vs. chain of comparisons | Replacing `if x == 'A': ... if x == 'B': ...` with `values[x]` when the check is really "find the value that goes with this key" |

---

## Reading

| Topic | Source |
|---|---|
| `try`/`except`, catching errors instead of crashing | [Errors and Exceptions — docs.python.org](https://docs.python.org/3/tutorial/errors.html) · [Learning Python, 6th Ed. — Ch. 34: Exception Basics](https://learning.oreilly.com/library/view/learning-python-6th/9781098171292/ch34.html#id4405) |
| Dictionaries | *placeholder — no Lubanovic chapter link yet in the comp-170-su26 reading table; flag for instructor to add (likely the chapter following Lists in* Introducing Python, *3rd ed.)* |
| Membership testing with `in` | *placeholder — same as above; the `in` operator itself has no dedicated reading entry yet, only mentioned in week 8's assignment notes* |

---

## Exercises

---
### Exercise 1 — Order of Checks, Revisited

Given `withdraw(150, 100)`, trace both possible check orders by hand: (a) multiple-of-\$20 first, then balance; (b) balance first, then multiple-of-\$20.

Questions:
1. Which check fails first under each ordering, and does the error message a user sees differ between them?
2. Is there an `(amount, balance)` pair where the two orderings would report a *different* error entirely (not just first vs. second)? Find one, or explain why none exists.

---
### Exercise 2 — Tracing the Recovery Loop

Trace the `while True` / `try`/`except` withdrawal loop from section 2 with this sequence of user inputs, in order: `50`, `500`, `60` (assume a starting `balance` of `200`).

Questions:
1. After each input, does the loop print an error and continue, or print success and `break`? Walk through all three.
2. What would happen if `break` were removed from the `try` block entirely — would the loop still stop after a successful withdrawal?

---
### Exercise 3 — Widening the `try` Block

Compare the two versions of the withdrawal loop from sections 2 and 2a: one with `amount = int(input(...))` outside the `try`, one with it moved inside.

Questions:
1. For a user who types `fifty`, what happens under each version — does the program crash, or print a "that didn't work" message and keep going?
2. Is there ever a good reason to *deliberately* leave a risky line outside a `try` block, so that it crashes instead of being caught? (Hint: think about the difference between an error the program can meaningfully recover from and one that signals something is fundamentally broken.)

---
### Exercise 4 — Dictionary vs. Chain of `if`s

Given `grade_values = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}`, evaluate `grade_values['B']` and `grade_values['E']` by hand.

Questions:
1. What does Python actually do when you look up a key that isn't in the dictionary — is it silent like `.find()`, or does it crash like `.index()`? What kind of error is it, specifically?
2. Given that answer, why does `enter_grade` still need its own `if letter not in grade_values: raise ValueError(...)` guard *before* the lookup, rather than just letting the dictionary lookup fail on its own?

---
### Exercise 5 — Building a Dictionary from Scratch

Sketch (pseudocode or Python) a dictionary called `state_capitals` that maps at least four U.S. state names to their capital cities, then write one lookup and one membership test (`in`) against it.

Questions:
1. What happens if you try to build this same lookup using two parallel lists (`states = [...]`, `capitals = [...]`) instead of a dictionary? What extra bookkeeping does the two-list version require that the dictionary avoids?
2. Is there a case where two parallel lists would actually be the *better* choice over a dictionary? (Hint: think about what a dictionary's keys are required to be.)

---

## Topics Deferred to Later Weeks

- `find_all_substrings` — finding every occurrence of a whole substring, not just the first (previewed in the week 8 plan's Exercise 4, still not built in class)
- Two-dimensional patterns using nested loops (deferred since week 4; still not addressed — search-shaped nested loops have been covered, grid-shaped ones have not)
- Slicing (`text[i:j]`) as a possible shortcut for string comparison
- Python's built-in `complex` number type, as an alternative to the hand-built `(real, imaginary)` tuple in `solve_quadratic`
- Rewriting `solve_quadratic` so every case — real or complex — returns a uniform shape
- Named tuples (`collections.namedtuple`)
- Reading and writing text files — a natural next step once dictionaries and `try`/`except` are in place (e.g., persisting a bank balance or a GPA between runs), and the closest analog in the pre-redesign COMP 170 syllabus places file I/O immediately after this stretch of exception-handling material
- Dictionary methods beyond lookup and `in` (`.get()`, `.keys()`, `.values()`, `.items()`) — introduce only once a concrete need for them comes up

# QA Report — COMP 158/159 Against checklist.md

*Reviewed against current document state as of 2026-05-14. Files checked:
`topics-158-159.md`, `syllabus-158.md`, `syllabus-159.md`, `proposal.md`,
`assessment.md`.*

---

## Summary

Of the 6 specific requests and 19 list items in the checklist, **15 are fully
covered**, **2 are partially covered**, and **6 remain absent**. No checklist
item conflicts with a settled design decision — the IDE item, which previously
appeared to conflict, has been resolved by the Week 9 transition.

---

## Specific Requests

### 1. Combinations and permutations — ABSENT

> "Explain and demonstrate the difference between combinations and
> permutations. Use both theoretical examples (e.g., powerset of a set) and
> practical/silly problems: how many n-scoops of ice cream combinations can
> you make with Baskin-Robbins 31 flavors? Permutations thereof?"

Powersets are covered in `topics-158-159.md` Week 10, but combinations and
permutations are never named or distinguished anywhere in the sequence.
The binomial theorem is explicitly deferred in the Topics Deferred table
(source: COMP 163), but the checklist is asking for the applied, intuitive
treatment — not the formal theorem. These are different things.

**Recommendation:** Add to 158 Week 10 (alongside powersets and sets) or 159
Week 9 (alongside probability). A one-session treatment with the Baskin-Robbins
example and a Python `itertools.combinations` / `itertools.permutations`
demonstration would satisfy the checklist intent without adding formal
combinatorics.

---

### 2. Sets connected to keys, hashtables, and dicts — COVERED

> "Discuss mathematical sets, their ability to 'reject' duplicates, and how
> this can be connected with primary keys, key-value pairs, hashtables, and
> Python dictionaries."

Covered in two places:

- `topics-158-159.md` COMP 158 Week 10: Python `set` introduced; `dict`
  previewed as a structure whose keys form a set.
- `topics-158-159.md` COMP 159 Week 7: dicts and hashing in depth — hash
  function as a mapping, pigeonhole principle, collision handling.

---

### 3. Shell-first, then IDE — COVERED

> "COMP 158 should start within a shell, reinforcing filesystem commands and
> plain text editor (Vim). Eventually transition to an IDE like VSC."

Weeks 1–8 of COMP 158 are Vim + terminal only. VS Code is introduced in
Week 9 (`topics-158-159.md`), with an explicit rationale: students must first
understand that a program is a text file before an IDE abstracts that away.
`syllabus-158.md`, `syllabus-159.md`, `proposal.md`, and `CLAUDE.md` all
reflect the two-phase design.

---

### 4. Basic probability and statistics — COVERED

> "At some point the 158+159 sequence should cover basic probability and
> statistics. For example, compute π by throwing random points within a
> square with an inscribed circle."

Covered in `topics-158-159.md` COMP 159 Week 9 (Probability and
Expected-Case Analysis). Monte Carlo π estimation is the explicit worked
example. Sample spaces, expected value, and hash collision simulation are
also in that week.

---

### 5. Algorithms not in Week 2 — COVERED

> "The current COMP 170 outline covers algorithms in week 2. We believe
> that's too early. Cover variables and expressions at depth first."

COMP 158 Week 2 is values, types, and variables only. Algorithm analysis
(Big-O) does not appear until COMP 159 Week 3. Sorting algorithms arrive
in COMP 159 Week 4. The concern is fully addressed by the design.

---

### 6. I/O terminology — ABSENT

> "We need to differentiate terminology between program i/o (`input()`,
> `open()`, etc) and function i/o. Maybe for functions/method use 'entry'
> and 'exit'?"

Nothing in the current documents addresses this. The word "input" is used
in two senses throughout — the `input()` built-in and the parameters of a
function — without any signal to students that these are different things.

**Recommendation:** Add a terminological note in `topics-158-159.md` Week 4
(Functions: The Mathematical Idea), when `def`, parameters, and `return` are
introduced. One paragraph is sufficient: name the ambiguity, establish the
course's convention (whether "entry"/"exit" or some other choice), and apply
it consistently in docstrings and assignments from that point forward.

---

## List Items

| Item | Status | Where |
|---|---|---|
| terminal / shell | Covered | 158 Wk 1, throughout |
| text editor | Covered | Vim: 158 Wk 1–8; VS Code: 158 Wk 9+ |
| file commands | Covered | 158 Wk 1 (`ls`, `cd`, `pwd`, `mkdir`, `cp`, `mv`, `rm`) |
| computer organization basics (memory hierarchy) | **Absent** | — |
| IDE basics | Covered | 158 Wk 9 (VS Code setup, file explorer, debugger) |
| simple debugging | Covered | 158 Wk 9 (breakpoints, step over/into/out in VS Code) |
| variable types | Covered | 158 Wk 2 |
| expressions | Covered | 158 Wk 2 |
| methods | Covered | 158 Wk 12; 159 Wk 5–6 |
| lists, loops | Covered | 158 Wk 6–9 |
| `if` statements | Covered | 158 Wk 3 |
| strings | Covered | 158 Wk 9 (string methods) |
| boolean | Covered | 158 Wk 3 |
| simple algorithms as pseudocode | **Absent** | — |
| vectors | Covered | 158 Wk 6 |
| matrices | **Partial** | Mentioned as optional capstone prompt only; not taught |
| exceptions | Covered | 158 Wk 8 (intro); 159 Wk 12 (full) |
| Python file I/O | Covered | 158 Wk 10 (`open()`, `readline()`, `strip()`, `with`) |
| intro to OOP | Covered | 158 Wk 12–13; 159 Wk 5–6 |

---

## Remaining Gaps

In priority order:

**1. Combinations and permutations** (specific request, with examples)
Natural home: 158 Wk 10 alongside powersets, or 159 Wk 9 alongside
probability. Python's `itertools` makes the applied demonstration
straightforward without requiring formal combinatorics.

**2. I/O terminology** (specific request)
One paragraph in 158 Wk 4. Low effort, high clarity payoff — the ambiguity
of "input" compounds every week once functions are introduced.

**3. Memory hierarchy** (list item)
One session or subsection in 158 Wk 11 (Number Representation), extending
the bits → bytes discussion upward to the storage pyramid (registers → cache
→ RAM → disk). Students are already thinking about how data lives in a
machine; the hierarchy is a natural extension.

**4. Pseudocode** (list item)
Minor. A one-paragraph note in 158 Wk 3 or Wk 7 — introduce pseudocode as
notation for describing an algorithm before committing to Python syntax.
Useful for the math↔code bridging that is central to the course's identity.

**5. Matrices** (list item)
Currently optional capstone only. Whether this should be formally taught is
a judgment call — matrix operations do not appear in the immediate downstream
pipeline (COMP 271 does not require them). If Karima and Leo want it, 158
Wk 6 (Sequences and Vectors) is the natural extension.

# COMP 170 — A 15-Week Outline of the Same Material

This is not a new curriculum. It is the actual Summer 2026 COMP 170 — the same four pillars (strings, if statements, loops, arrays), the same testing unit, the same file-I/O and dictionary capstone — repaced from 11 compressed weeks into a standard 15-week semester. No topic here is beyond what students in `../../comp-170-su26/` actually learned; the extra four weeks buy breathing room on the densest stretches, and every week now carries a small linux/system thread and a small math thread alongside the programming, instead of those threads showing up only in the weeks where they happened to fit (week01's shell content, week03's ASCII/number systems, week08's quadratic formula).

**Reading legend:**
- **Lubanovic** — Bill Lubanovic, *Introducing Python*, 3rd ed. Chapter numbers match the citations already established in `../../comp-170-su26/CLAUDE.md`'s Reading Materials table; a chapter cited there for the first time in this document is marked *(new citation)*.
- **TLCL** — William Shotts, *The Linux Command Line*, 6th ed. (linuxcommand.org, free) — supplementary source for the weekly linux/system bit, alongside the Bash and Vim cheat sheets already in the student-facing reading table.
- **notes** — original course material (this repository, or a new in-class handout), used where no single textbook chapter covers the idea cleanly — the same convention `proposal_158_159/comp170-revised.md` uses.
- Where a URL is not yet confirmed against a real source, it is marked *(placeholder — flag for instructor)*, per this repo's standing rule against inventing links.

A coverage map at the end shows exactly which original week each new week descends from.

---

## Week 1 — The Shell and Your First Program
*(= original Week 1, part 1)*

- **Linux/System:** `pwd`, `ls`, `cd`, `mkdir`; the shell as the program that reads and runs commands; Vim's two modes (`i`, `Esc`, `:w`, `:q`, `:wq`).
- **Programming:** `python3 file.py`, `print()`, comments; the edit–save–run loop.
- **Math:** a script is a strictly ordered list of steps — the same idea as a numbered recipe. This is the informal seed of "sequence" that Week 5 and Week 7 will make precise.
- **Reading:** Lubanovic Ch. 1 (Introduction); Bash cheat sheet; Vim cheat sheet; `tools/vim_tutorial.md`.

---

## Week 2 — Data, Types, and the Command Line
*(= original Week 1, part 2)*

- **Linux/System:** file extensions as convention, not enforcement; `man` and `--help`; first look at output redirection (`python3 script.py > out.txt`) as a preview of "a program's output can go somewhere other than the screen."
- **Programming:** `str`, `int`, `float`; `type()`; type conversion; variables and assignment; arithmetic operators and precedence.
- **Math:** a type as a set of legal values, and a type error as an operation applied outside that set; `/` vs. `//` as true vs. floor division.
- **Reading:** Lubanovic Ch. 2 (Types and Variables), Ch. 3 (Numbers); docs.python.org — An Informal Introduction: Text.

---

## Week 3 — Building a Real Program: Separation of Concerns
*(= original Week 2)*

- **Linux/System:** command history and the up-arrow as the practical reason the edit–run loop is fast; a first look at shell variables (`export RATE=0.05`) as a spoken parallel to a Python variable.
- **Programming:** `input()`, the compound-interest calculator, and the discipline of separating input, logic, and output into distinct sections of a program (`interest.py` → `interest_pro.py`).
- **Math:** the compound interest formula $$A = P(1 + r)^t$$ and rounding to a sensible number of decimal places for currency.
- **Reading:** Lubanovic Ch. 2–3 (review, applied); TLCL Ch. 3 (navigation) for the history/shell-variables bit.

---

## Week 4 — Strings, ASCII, and Number Systems
*(= original Week 3, part 1)*

- **Linux/System:** `cat` and `less` for viewing a text file's raw contents; a first, informal look at character encoding (why a terminal shows the letters it shows).
- **Programming:** `ord()`/`chr()`, string repetition (`*`) as something conceptually different from arithmetic multiplication, `int()` conversion.
- **Math:** four ASCII anchor values worth memorizing ($32$ space, $48$ `'0'`, $65$ `'A'`, $97$ `'a'`); positional number systems (decimal, binary, hexadecimal) and converting between them by hand.
- **Reading:** Lubanovic Ch. 4 (Strings); docs.python.org — An Informal Introduction: Text.

---

## Week 5 — Loops and Pattern-Making
*(= original Week 3, part 2)*

- **Linux/System:** the shell's own `for` loop (`for i in {1..5}; do echo $i; done`) as the same idea in different syntax — a first explicit "this concept, two languages" moment.
- **Programming:** `for` loops, `range()`, drawing shapes (staircase, right-aligned triangle, diamond, bar chart) by discovering the row-by-row pattern first and writing pseudocode before code; scope and indentation.
- **Math:** for a triangle of height $N$, row $i$ has $N - i$ spaces and $i$ stars — an algebraic expression discovered from a table of examples, not handed down.
- **Reading:** Lubanovic Ch. 7 (Loops, first half — `for`); docs.python.org — for Statements; docs.python.org — The range() Function; TLCL Ch. 11 (shell loops) *(new citation — flag for instructor to confirm exact TLCL chapter number)*.

---

## Week 6 — Conditionals and Modular Arithmetic
*(= original Week 4, part 1)*

- **Linux/System:** exit codes (`$?`) as the shell's own true/false, and a first look at a shell `if [ ... ]` test as a spoken parallel to Python's `if`.
- **Programming:** `if`/`elif`/`else`, `and`/`or`, `==` vs. `=`, the modulo operator, the airplane-seating problem.
- **Math:** modular arithmetic (remainders, and why $n \bmod m$ cycles through $0, 1, \dots, m-1$); `and`/`or` described informally as intersection and union of two conditions being simultaneously or either true.
- **Reading:** Lubanovic Ch. 3 (Numbers, `%` operator), Ch. 5 or equivalent conditionals section *(new citation — flag for instructor: confirm the exact Lubanovic chapter number for `if`/Boolean expressions, not yet in the student-facing reading table)*.

---

## Week 7 — Lists and the Cumulative Pattern
*(= original Week 4, part 2)*

- **Linux/System:** `wc -l` as a real-world running count, and `|` (the pipe) as chaining one command's output into another — the shell's own version of passing a list from one step to the next.
- **Programming:** list creation, zero-based indexing, `len()`, and the cumulative algorithm (running sum / running average).
- **Math:** a list as an indexed family $a_0, a_1, \dots, a_{n-1}$; zero-based indexing as an offset from the start; the mean $$\bar{a} = \frac{1}{n}\sum_{i=0}^{n-1} a_i$$
- **Reading:** Lubanovic Ch. 8 (Lists); TLCL text-processing chapter (`wc`, `|`).

---

## Week 8 — Splitting Strings and Writing Methods
*(= original Week 5, part 1)*

- **Linux/System:** `grep` and `cut` as command-line tools that already do a version of what `.split()` does — search and column-extraction on text.
- **Programming:** `sentence.split()`, the enhanced `for` loop, packaging logic into a method with type hints, a docstring, and input validation.
- **Math:** a method as an input → output rule, described informally (not yet formal domain/codomain — that stays out of scope, matching the original course); a precondition as a stated assumption about what comes in.
- **Reading:** Lubanovic Ch. 4 (Strings, `.split()`), Ch. 10 (Functions — defining a `def`, type hints, docstrings); docs.python.org — Defining Functions.

---

## Week 9 — Organizing Code Across Files
*(= original Week 5, part 2)*

- **Linux/System:** multi-file project layout, `ls -R` to see it; first touch of Git — `git init`, `git add`, `git commit`, `git status` — as the natural tool once a project is more than one file.
- **Programming:** running a script directly vs. importing its methods from another file; `if __name__ == "__main__":` as the boundary between "reusable logic" and "demo code."
- **Math:** a module's namespace as a set of unique names — no two `def`s in the same file can share a name — a light foreshadow of the uniqueness of dictionary keys in Week 15.
- **Reading:** Lubanovic Ch. 10 (Functions, continued); TLCL Ch. on version control *(placeholder — flag for instructor: TLCL 6th ed. covers Git only lightly if at all; confirm source or substitute the official Git documentation)*.

---

## Week 10 — Accumulators, Factorials, and a First Look at Recursion
*(= original Week 6, part 1)*

- **Linux/System:** shell arithmetic with `$(( ))`, and a two-line bash loop that accumulates a running total — the same accumulator pattern, one more syntax.
- **Programming:** loop variable naming conventions, the accumulator pattern for running sum/product, the factorial method, and a first, brief look at recursion.
- **Math:** the recursive definition $$n! = n \cdot (n-1)!, \quad 0! = 1$$ and how quickly factorial grows compared to the loop-based accumulator computing it.
- **Reading:** Lubanovic Ch. 10 (Functions — recursion section, optional per the student-facing reading table, now assigned directly).

---

## Week 11 — Reinventing `split()` and Debugging Loops
*(= original Week 6, part 2)*

- **Linux/System:** `sed` and `awk`, named (not taught in depth) as the tools that already solve this class of problem professionally; `diff` for comparing a program's actual output against its expected output while debugging.
- **Programming:** parsing a string character by character to reimplement `str.split()` from scratch, the classic consecutive-delimiter bug, and method headers with default parameter values.
- **Math:** boundary/edge-case reasoning made explicit — what happens at the first character, the last character, and two delimiters in a row — the same habit that Week 13's input validation will lean on.
- **Reading:** Lubanovic Ch. 4 (Strings, revisited); Ch. 10 (Functions — default parameter values).

---

## Week 12 — Searching Strings and Multiplication Grids
*(= original Week 7, part 1 + a slice of original Week 9)*

- **Linux/System:** `grep` and `find`, now used directly rather than just named — a real search over real files, side by side with the `.find()`/`.index()` code students write by hand.
- **Programming:** writing `.find()`/`.index()`-style search from scratch, definite vs. indefinite loops, infinite loops, counting occurrences, guard clauses against missing input; nested loops via the multiplication-table exercise.
- **Math:** an existence question asked informally — "does the character occur, and if so, where?" — plus the multiplication table itself as ordered pairs $(i, j) \mapsto i \times j$, a first, gentle taste of a Cartesian grid.
- **Reading:** Lubanovic Ch. 7 (Loops, second half — `while`); docs.python.org — for Statements (revisited for nested loops).

---

## Week 13 — Validating Input: `try`/`except` and the ATM
*(= original Week 9, remainder)*

- **Linux/System:** a shell `until` loop as the retry-loop pattern's shell-side cousin; `trap`/basic error handling in bash, named as the shell's own answer to "something went wrong, now what?"
- **Programming:** `try`/`except` around `int(input())`, a `max_tries` cap, the difference between separate `if` statements (fall-through) and `elif` (mutually exclusive branches), and the retry-loop pattern organized into `withdraw()` / `attempt_withdrawal()` / `main()`.
- **Math:** interval membership — checking a birth year against $[1901, 2025]$ is the same idea as checking a withdrawal amount against a maximum, phrased as "is this value inside a valid range?"
- **Reading:** docs.python.org — Errors and Exceptions; *Learning Python, 6th ed.* Ch. 34 (Exception Basics).

---

## Week 14 — Designing and Testing a Method
*(= original Week 8)*

- **Linux/System:** running `python3 -m unittest` from the command line and reading its pass/fail summary; the shell's exit-status convention (`0` = success) as the same signal `unittest` gives a CI system, described in one sentence as a preview of what "automated" testing means.
- **Programming:** the quadratic formula and discriminant, complex numbers represented as `(real_part, imaginary_part)` tuples, designing `solve_quadratic()` case by case with a flow chart and matching pseudocode, and three levels of testing — naive `print()` checks, plain assertion methods, and `unittest` — applied to a real, published PyPI package (`mathemagics`).
- **Math:** the quadratic formula $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$ the discriminant $b^2 - 4ac$ as the value that decides which of the three cases applies, and complex numbers $a + bi$ as ordered pairs.
- **Reading:** `mathemagics` on PyPI; docs.python.org — Errors and Exceptions (raise/ValueError, revisited).

---

## Week 15 — Files, Dictionaries, and Reading a Book from the Web
*(= original Week 10 + original Week 11)*

- **Linux/System:** file permissions (`ls -l`, `chmod`) now that files are finally being created and read; `curl`/`wget` as the command-line equivalent of `urllib.request.urlopen()`; `sort | uniq -c | sort -rn` at the shell as the exact same word-frequency idea the dictionary program builds in Python, solved with three piped commands instead of a loop.
- **Programming:** what a file is, why writes buffer until `.close()`, the three file modes (write/append/read), reading a file line by line; then the capstone — reading a public-domain book directly from a URL, stripping punctuation with `.replace()` (no `re` needed), and counting words with a dictionary instead of two synchronized lists, closing with the same refactor into named methods that ended the original course.
- **Math:** bytes and bits as powers of two (a callback to Week 4's number systems); a dictionary's keys as a set with no duplicates — the same uniqueness idea introduced informally in Week 9's namespace discussion, now with real machinery behind it.
- **Reading:** Lubanovic Ch. 20 (Files); Lubanovic Ch. 9 (Dictionaries and Sets); Computer file (Wikipedia); Memory & Storage Timeline (Computer History Museum).

---

## Coverage Map

| New week(s) | Original week | What carries over unchanged |
|---|---|---|
| 1–2 | Week 1 | Shell, Vim, `python3`, data types, variables |
| 3 | Week 2 | Compound interest, separation of concerns |
| 4–5 | Week 3 | ASCII, strings, number systems, loops, shapes, scope |
| 6–7 | Week 4 | Booleans/if, modulo, airplane seats, lists, cumulative pattern |
| 8–9 | Week 5 | `.split()`, enhanced `for`, method design, imports |
| 10–11 | Week 6 | Accumulator, factorial/recursion, reinventing `.split()`, debugging |
| 12 | Week 7 (+ part of 9) | `.find()`/`.index()`, definite/indefinite loops, nested loops |
| 13 | Week 9 (remainder) | `try`/`except`, ATM `if`/`elif` vs. separate `if`s, retry loop |
| 14 | Week 8 | Quadratic formula, complex numbers, three-level testing |
| 15 | Weeks 10–11 | Files, memory/storage, dictionaries, word counting from a URL |

Four blocks absorb the four extra weeks (original Weeks 3, 6, 8, and the 7/9 split); every other original week keeps its original one-week footprint. No new programming topic was added anywhere in this table — only linux/system and math threads, which the original 11-week course carried in just a handful of weeks (mainly Week 1, Week 3, and Week 8), now run through all fifteen.

# COMP 170 — Revised Outline
### Rearranged to reflect the content of COMP 158 and the first half of COMP 159

Topics marked **[new]** have no counterpart in the original COMP 170 schedule; they come from content in COMP 141 (CLI tools), COMP 163 (discrete mathematics), or the expanded programming scope of COMP 158/159.

OER references use the following abbreviations:
- **TP** — Allen Downey, *Think Python*, 3rd ed. (greenteapress.com)
- **TLCL** — William Shotts, *The Linux Command Line*, 6th ed. (linuxcommand.org)
- **notes** — course notes distributed via the course repository (mathematical content)

A summary coverage map appears at the end of this document.

---

## COMP 158 — 14 Weeks

### Before Week 1 — Setup
- Course overview and student survey *(original COMP 170 pre-class)*
- Unix environment setup: Mac Terminal, Linux, or Windows with WSL **[new]**

---

### Week 1 — The Environment
- Running a Python script: `python3`, `print()`, comments *(TP: "Programming as a Way of Thinking")*
- Filesystem navigation: `ls`, `cd`, `pwd`, `mkdir`, `cp`, `mv`, `rm` *(TLCL: navigation and file operations)* **[new CLI]**
- Editing in Vim: modes, navigation, saving *(TLCL: text editors)* **[new CLI]**
- Git basics: `init`, `add`, `commit`, `status` **[new CLI]**

---

### Week 2 — Values, Types, and Variables
*(TP: "Variables and Statements")*
- Data types: `int`, `float`, `str`, `bool`; literals
- Type conversion: `int()`, `float()`, `str()`
- Variables, assignment, arithmetic operators and precedence
- `input()`: reading a value, doing arithmetic on it, printing the result
- A type as a set; a type error as an operation applied outside its domain *(notes)* **[new math]**

---

### Week 3 — Logic and Conditionals
*(TP: "Conditionals and Recursion")*
- `if`, `elif`, `else`; Boolean expressions with `and`, `or`, `not`
- Short-circuit evaluation; nested conditionals
- Propositions, truth values, connectives (∧, ∨, ¬), truth tables *(notes)* **[new math]**
- De Morgan's laws: ¬(P ∧ Q) ≡ ¬P ∨ ¬Q; ¬(P ∨ Q) ≡ ¬P ∧ ¬Q *(notes)* **[new math]**
- I/O redirection: `>`, `>>`, `<` *(TLCL: redirection)* **[new CLI]**

---

### Week 4 — Functions: The Mathematical Idea
*(TP: "Functions"; "Return Values")*
- Algorithms as step-by-step procedures
- `def`, parameters, `return`; the call stack
- Parameters and return values; the `math` module
- Pure functions (output depends only on input) vs. functions with side effects
- Functions as mappings (domain → codomain); function composition *(notes)* **[new math]**
- Makefile with a `run` target: `make run` replaces retyping `python3 script.py` *(TLCL: make)* **[new CLI]**

---

### Week 5 — Designing and Testing Functions
*(TP: "Functions"; "Return Values")*
- Interactive programs; `input()` in context
- Pre- and post-conditions; docstrings (`"""..."""`); `help()`
- `assert`-based testing; writing a `test_` function for each function under development **[new]**
- `make test` target; the working habit: write the docstring, write the test, then write the code **[new]**

---

### Week 6 — Sequences and Vectors
*(TP: "Lists" — introductory portion)*
- Python lists: literals, indexing (`lst[0]`), `len()`, `append()`, slicing
- First encounter with list iteration (`for x in lst`) — formalized next week
- Mathematical sequences as indexed families (a₁, a₂, ..., aₙ) *(notes)* **[new math]**
- Vectors as elements of ℝⁿ; summation notation ∑; the dot product as a motivating example *(notes)* **[new math]**

---

### Week 7 — Iteration: Operationalizing ∀ and ∑
*(TP: "Iteration")*
- `for` loop, `range()` (start, stop, step)
- The accumulator pattern: running total, running maximum, running minimum
- Tracing loop execution by hand
- The universal quantifier ∀ and the `for` loop as its realization *(notes)* **[new math]**
- Summation ∑ implemented as an accumulator loop; dot product as the worked example *(notes)* **[new math]**
- Shell `for` loop as the same concept in a different syntax *(TLCL: loops)* **[new CLI]**

---

### Week 8 — Searching and ∃
*(TP: "Iteration" — while loop; "Files and Databases" — exceptions)*
- `while` loop, loop conditions, `break`
- Linear search: iterate until found or exhausted
- Interaction loop: keep prompting until valid input is given
- `try`/`except`: wrapping `int(input())`, catching `ValueError`
- The existential quantifier ∃; negation of quantifiers: ¬(∀x, P(x)) ≡ ∃x, ¬P(x) *(notes)* **[new math]**
- `grep` as existential search at the shell; comparing `grep` on a data file to a Python search script *(TLCL: grep)* **[new CLI]**

---

### Week 9 — More on Lists; IDE Transition
*(TP: "Strings"; "Lists")*
- List comprehension: `[f(x) for x in lst if p(x)]`
- List methods: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `sorted()`, `reverse()`
- String methods: `split()`, `strip()`, `join()`, `lower()`, `replace()`, `find()`
- List comprehension as set-builder notation {x ∈ A | P(x)} *(notes)* **[new math]**
- VS Code: file explorer, syntax highlighting, integrated terminal, debugger basics (breakpoints, step over/into/out) **[new IDE]**
- Shell sequence tools: `grep`, `sort`, `uniq`, `cut` — solving the same problem as Python, compared side by side *(TLCL: text processing tools)* **[new CLI]**

---

### Week 10 — Sets and File Input
*(TP: "Files and Databases")*
- File input: `open()`, iterating over lines, `strip()`, `readline()`, `with open(...) as f:`
- Reading a text file and collecting its words
- Set theory: ∈, ⊆, ∪, ∩, \, Cartesian product A × B; sets vs. sequences *(notes)* **[new math]**
- Python `set` and `frozenset`; set operations (`|`, `&`, `-`, `<=`) **[new]**
- Converting between lists and sets; dict previewed as a structure whose keys form a set **[new]**
- `sort | uniq` at the shell; `comm` for intersection and difference *(TLCL: text processing tools)* **[new CLI]**

---

### Week 11 — Number Representation
*(not in original COMP 170)*
- Binary (base 2) and hexadecimal (base 16); counting and converting between bases; binary addition *(notes)* **[new math]**
- `bin()`, `hex()`, `int('1010', 2)`; bitwise operators (`&`, `|`, `^`, `<<`, `>>`) **[new]**
- File permissions in octal: `chmod 644`; `xxd` to view file bytes in hexadecimal *(TLCL: permissions)* **[new CLI]**

---

### Week 12 — Classes and Objects
*(TP: "Classes"; "Classes and Methods")*
- OO programming: `class`, `__init__`, instance variables, `self`, methods, dot notation
- Object state and behavior; constructors; creating instances
- A first complete class: `Vector`, with a constructor, a `dot()` method, and `__len__`
- Defining a class as defining a mathematical structure (a set of objects together with operations) *(notes)* **[new math]**
- Organizing code into multiple `.py` files; updating the Makefile **[new CLI]**

---

### Week 13 — Designing with Classes
*(TP: "Classes and Methods" — extended)*
- Two classes interacting; class invariants; pre/post conditions on methods
- Docstrings that state the class invariant and the conditions on each method
- Relations: reflexive, symmetric, transitive, antisymmetric *(notes)* **[new math]**
- Equivalence relations and partial orders; sorted order as a partial order *(notes)* **[new math]**

---

### Week 14 — Capstone
*(original COMP 170: project presentations and final exam)*
- Mini-project: a multi-class Python program with a clear mathematical motivation
- Full docstrings, a `make test` target that runs all assertions, submitted via `git push`
- Review: each programming concept paired with its mathematical counterpart

---

## COMP 159 — Weeks 1–7

### Week 1 — Recursion: The Concept
*(not in original COMP 170; TP: "Conditionals and Recursion" — recursion introduced but not developed)*
- Recursive functions in Python: base case and recursive case **[new]**
- Tracing the call stack: factorial and sum of a list **[new]**
- Mathematical induction: base case P(0) and inductive step P(n−1) → P(n) *(notes)* **[new math]**

---

### Week 2 — Recursion Patterns and Recurrence Relations
*(not in original COMP 170)*
- Recursive list processing: reverse, flatten, count occurrences **[new]**
- Recursive string processing: palindrome check **[new]**
- Head/tail pattern; mutual recursion (briefly) **[new]**
- Recurrence relations: T(n) = T(n−1) + c → O(n); setting up recurrences from code *(notes)* **[new math]**
- `find` as recursive directory traversal — the shell doing recursion on the filesystem *(TLCL: find)* **[new CLI]**

---

### Week 3 — Algorithm Analysis and Big-O
*(original COMP 170: algorithms introduced informally; significantly extended here)*
- Counting operations in code; why algorithm choice matters
- Big-O notation: formal definition; common classes O(1), O(log n), O(n), O(n log n), O(n²) *(notes)* **[new math]**
- Growth rate comparison; best, worst, and average case *(notes)* **[new math]**
- Cost of list operations: `append` O(1) amortized, insertion at position 0 is O(n) **[new]**
- `time` command; shell loop benchmarking: observing growth empirically before analyzing it *(TLCL: shell scripts)* **[new CLI]**

---

### Week 4 — Sorting
*(not in original COMP 170)*
- Selection sort and insertion sort: both O(n²), easy to trace by hand **[new]**
- Merge sort: divide the list in half, sort each half recursively, merge the results **[new]**
- Recurrence for merge sort: T(n) = 2T(n/2) + n; solving by unrolling → O(n log n) *(notes)* **[new math]**
- Master Theorem as a recipe for divide-and-conquer recurrences *(notes)* **[new math]**
- `sort` with options (`-n`, `-r`, `-k`); comparing shell sort and Python sort on the same file *(TLCL: text processing tools)* **[new CLI]**

---

### Week 5 — Inheritance
*(not in original COMP 170; single-class OOP only)*
- `class Dog(Animal)`, method inheritance, `super()`, method overriding, `isinstance()` **[new]**
- Worked hierarchy: `Shape` → `Circle`, `Rectangle`, `Triangle`; each overrides `.area()` and `.perimeter()` **[new]**
- Subclass as subset: `Dog ⊆ Animal`; Liskov substitution principle informally *(notes)* **[new math]**
- Multi-file project organization; updating the Makefile **[new CLI]**

---

### Week 6 — Polymorphism and Multiple Interacting Classes
*(not in original COMP 170)*
- Polymorphism: a list of `Shape` objects, `.area()` dispatching to the correct subclass **[new]**
- `Node` + `LinkedContainer` pattern: the foundation COMP 271 will use at speed **[new]**
- `__main__` blocks for independent class testing; `diff`-based output testing in the Makefile **[new CLI]**

---

### Week 7 — Dictionaries and Hashing
*(not in original COMP 170)*
- Python `dict`: creation, lookup, insertion, `in`, `.items()`, `.keys()`, `.values()`, iteration *(TP: "Dictionaries")* **[new]**
- Dict comprehension; use cases: word frequency counting, grouping by property, memoized Fibonacci **[new]**
- Hash function as a mapping from keys to bucket indices — same domain/codomain vocabulary as COMP 158 Week 4 *(notes)* **[new math]**
- Pigeonhole principle: why collisions are inevitable when keys outnumber buckets *(notes)* **[new math]**
- Word frequency: Python dict compared to `sort | uniq -c | sort -rn` at the shell **[new CLI]**

---

## Coverage Map

| Original COMP 170 topic | Integrated sequence placement |
|---|---|
| Pre-class: setup, survey | COMP 158 pre-course |
| Intro to Python: running scripts, `print()`, comments | COMP 158 Week 1 |
| Algorithms and functions (informal) | COMP 158 Week 4; COMP 159 Week 3 |
| Data types, variables, expressions | COMP 158 Week 2 |
| The `for` loop and problem solving | COMP 158 Week 7 |
| Parameters and return values; `math` module | COMP 158 Week 4 |
| Interactive programs; `input()` in context | COMP 158 Week 5 |
| `random` module | Deferred to COMP 159 Week 9 (probability simulation) — beyond first-half scope |
| The `if` statement and Boolean expressions | COMP 158 Week 3 |
| Intro to lists | COMP 158 Week 6 |
| Pre- and post-conditions; docstrings | COMP 158 Week 5 |
| Text processing; string methods | COMP 158 Week 9 |
| Exceptions: first encounter with `try`/`except` | COMP 158 Week 8 |
| `while` loop and indefinite loops | COMP 158 Week 8 |
| Intro to text files | COMP 158 Week 10 |
| Relational expressions | COMP 158 Week 3 |
| Assertions and `try`/`except` in depth | COMP 158 Weeks 5 and 8 |
| File processing | COMP 158 Week 10 |
| More about lists | COMP 158 Week 9 |
| OO programming: classes, constructors, state and behavior | COMP 158 Weeks 12–13 |
| Project and final exam | COMP 158 Week 14 |

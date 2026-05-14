# COMP 158 — Computing, Mathematics, and Programming I
### 3 Credit Hours | Offered fall and spring

---

## Instructors

| | |
|---|---|
| **Instructor A** | *name* · *office* · *email* · Office hours: *TBD* |
| **Instructor B** | *name* · *office* · *email* · Office hours: *TBD* |

This course is co-taught. Both instructors are present for most sessions and share responsibility for grading and office hours.

---

## Meeting Times

*Days, times, and room — see the registrar.*

---

## Course Description

COMP 158 is the first half of a two-semester integrated introduction to programming, computing tools, and the mathematics of computation. Topics from introductory programming, discrete mathematics, and Unix command-line tools are presented together, in an order driven by programming concepts rather than by subject-area boundaries. Mathematical ideas are introduced when they clarify what a program is doing; command-line tools are used throughout as the working environment. By the end of the semester, students will write Python programs from the terminal, manage their work with Git, reason about programs using basic logic and set theory, and design simple classes. COMP 159 follows in the subsequent term.

---

## Prerequisites

No prior programming experience is required or assumed. Some familiarity with algebra is helpful but not formally required.

---

## Required Materials

All required texts are freely available online. No purchase is necessary.

- **Allen Downey, *Think Python*, 3rd edition.** Available at [greenteapress.com](https://greenteapress.com/wp/think-python-3rd-edition/). The primary Python reference for the course.
- **William Shotts, *The Linux Command Line*, 6th edition.** Available at [linuxcommand.org](https://linuxcommand.org/tlcl.php). The primary reference for shell and command-line topics.
- **Course notes** for mathematical content (logic, sets, functions, relations) will be distributed as needed via the course repository.

You will need access to a Unix-like environment: a Mac (Terminal), a Linux machine, or Windows with WSL (Windows Subsystem for Linux) installed. Setup instructions are provided in the first week.

---

## Learning Outcomes

By the end of COMP 158, students will be able to:

1. Navigate the Unix filesystem and use the shell as a development environment.
2. Write, run, and debug Python programs using a plain text editor and the command line.
3. Use Git for version control and `make` for build automation.
4. Translate propositional logic — propositions, connectives, De Morgan's laws — into Python boolean expressions and conditional statements.
5. Define and implement Python functions, connecting the programming concept to its mathematical definition as a mapping from domain to codomain.
6. Specify function behavior with preconditions, postconditions, and docstrings, and verify it with `assert`-based tests.
7. Work with lists as ordered sequences; apply common list algorithms including searching, filtering, and accumulation.
8. Apply set theory — membership, subsets, union, intersection — to Python collections.
9. Design and implement a class with instance variables, methods, and a stated invariant.

---

## How This Course Works

**Weeks 1–8 are shell-only.** Code is written in Vim, run from the terminal, and submitted via `git push`. No IDE. The reason is deliberate: a plain text editor forces you to understand that a program is a file, that running it is a command, and that errors come back as text you have to read. An IDE that hides these layers before you understand them is a liability, not an asset.

**In week 9, VS Code is introduced** as the primary editor for the rest of the semester. By then the foundations are solid, and the IDE's file browser, syntax highlighting, and debugger become tools rather than crutches. The integrated terminal inside VS Code runs the same `git push` and `make test` commands — nothing about how code is submitted or tested changes.

Mathematical concepts are not taught as a separate subject. They arrive when they are needed to explain something in the code. You will see propositional logic the same week you write your first `if` statement, and summation notation the week before you write your first `for` loop accumulator. The goal is not to compartmentalize — it is to show that the math and the code are describing the same thing.

---

## Assignments and Grading

| Component | Weight | Notes |
|-----------|--------|-------|
| Programming assignments | 50% | Approximately one per week; submitted via `git push` |
| Midterm exam | 20% | Written; covers weeks 1–7 |
| Capstone project | 25% | Week 14; see description below |
| Participation | 5% | In-class exercises and engagement |

### Programming Assignments

Assignments are posted Monday and due the following Sunday at 11:59 pm. Each assignment specifies a `make` target — `make test` must pass before submission. Partial credit is given for partial solutions that are clearly reasoned and documented.

**Late policy:** 10% deducted per calendar day. No submissions accepted more than five days after the deadline without a documented exception arranged in advance.

### Midterm Exam

A written exam covering programming concepts, mathematical reasoning, and CLI tasks from weeks 1–7. You will be asked to trace code, write short functions, construct truth tables, and answer short-answer questions about program behavior.

### Capstone Project

A multi-class Python program completed in the final week of the course. Requirements:
- At least two interacting classes, each with a stated invariant and documented methods
- A complete test suite run via `make test`
- Full docstrings on all functions and classes
- Submitted via `git push`

The project is individual work. A brief (10-minute) oral review may be requested for any submission.

### Grading Scale

| Grade | Range |
|-------|-------|
| A | 93–100 |
| A− | 90–92 |
| B+ | 87–89 |
| B | 83–86 |
| B− | 80–82 |
| C+ | 77–79 |
| C | 73–76 |
| C− | 70–72 |
| D | 60–69 |
| F | below 60 |

---

## Weekly Schedule

| Week | Topic | Key skills |
|------|-------|------------|
| 1 | The environment | Filesystem navigation, Vim, running Python, Git basics |
| 2 | Values, types, and variables | Data types, expressions, assignment; types as sets |
| 3 | Logic and conditionals | Propositions, truth tables, De Morgan's laws; `if`/`elif`/`else` |
| 4 | Functions: the mathematical idea | Domain, codomain; `def`, parameters, `return` |
| 5 | Designing and testing functions | Preconditions, docstrings, `assert`; `make test` |
| 6 | Sequences and vectors | Indexing, summation ∑; lists, `len()`, slicing |
| 7 | Iteration — the `for` loop | Universal quantifier ∀; accumulator pattern, dot product |
| 8 | Searching — the `while` loop | Existential quantifier ∃; linear search, `break`; `try`/`except` for input validation |
| 9 | List algorithms and comprehension; IDE transition | Set-builder notation; comprehensions, string methods; VS Code setup, debugger basics |
| 10 | Sets and file input | Set theory: ∈, ∪, ∩, ×; Python `set` and `frozenset`; `open()`, `strip()`, `split()` |
| 11 | Number representation | Binary and hexadecimal; `bin()`, `hex()`, file permissions |
| 12 | Classes and objects | Mathematical structures; `class`, `__init__`, methods |
| 13 | Designing with classes | Relations, partial orders; multi-class design, invariants |
| 14 | Capstone | Project due; review: each math concept with its programming analog |

*The schedule may shift by a session or two as the semester develops. Any changes will be announced in class and posted to the course repository.*

---

## Course Policies

### AI Tools

You may use AI coding assistants (ChatGPT, GitHub Copilot, Claude, or others) to help you understand concepts, interpret error messages, or get unstuck. You may not submit code generated by an AI as your own work.

A practical test: if you cannot explain every line of your submitted code — what it does, why it is there, and what would happen if it were removed — then the submission is not your own work. In-class exercises and any oral review of the capstone are designed to verify this understanding directly.

The deeper point: this course exists precisely to build the understanding that AI tools cannot substitute for. A student who understands why a loop is the right structure for a summation is in a different position than one who has learned to ask an AI to write loops. Both may produce correct-looking code; only one can tell when the code is wrong, and why.

### Academic Integrity

All submitted work must be your own unless the assignment explicitly designates a partner or group component. Discussion of concepts and debugging approaches with classmates is encouraged. Copying code — from a classmate, from the internet, or from an AI tool — and submitting it as your own is a violation of the university's academic integrity policy and will be referred to the Dean's office.

### Attendance

No formal attendance grade, but in-class exercises count toward the participation component and cannot be made up. If you must miss a session, let us know in advance.

### Accessibility

Students who require accommodations should contact the university's accessibility office and provide documentation to the instructors within the first two weeks of the semester. We will work to ensure full access to course materials and assessments.

### Communication

Questions about assignments should be posted to the course discussion board so that answers are visible to everyone. Email is appropriate for personal matters. We aim to respond within one business day.

---

## A Note on the Course Design

This is a pilot course. The sequence is new, the integration of topics is experimental, and we expect to learn from the first offering. If something is not working — the pacing, the tools, the assignment format — tell us. We will be collecting data on student outcomes throughout (see the course repository for the assessment framework), and your feedback is part of that data.

What we ask in return: engage with the tools, even when they feel slower than an IDE. The terminal is uncomfortable at first for almost everyone. That discomfort is temporary; the fluency is permanent.

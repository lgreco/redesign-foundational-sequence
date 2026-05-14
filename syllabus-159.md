# COMP 159 — Computing, Mathematics, and Programming II
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

COMP 159 is the second half of the integrated introductory sequence that began in COMP 158. Students enter having written Python from the terminal, designed classes, and connected programming to basic logic, set theory, and functions. This semester builds on that foundation: recursion and its mathematical justification, algorithm analysis and Big-O notation, advanced object-oriented design (inheritance, polymorphism, multiple interacting classes), dictionaries and hashing, mutability and object references, abstract data types, and shell scripting. By the end of the semester, students are prepared to enter COMP 271 (Data Structures) with both the programming vocabulary and the mathematical vocabulary that course assumes.

---

## Prerequisites

COMP 158 with a grade of C or better.

---

## Required Materials

The same freely available texts as COMP 158, continued:

- **Allen Downey, *Think Python*, 3rd edition.** Available at [greenteapress.com](https://greenteapress.com/wp/think-python-3rd-edition/).
- **William Shotts, *The Linux Command Line*, 6th edition.** Available at [linuxcommand.org](https://linuxcommand.org/tlcl.php).
- **Course notes** for mathematical content (recurrence relations, Big-O, probability) distributed via the course repository.

---

## Learning Outcomes

By the end of COMP 159, students will be able to:

1. Write recursive functions, trace their execution, and identify the base case and recursive case.
2. Express the running time of a recursive algorithm as a recurrence relation and solve simple recurrences by unrolling.
3. Apply Big-O notation to analyze and compare algorithms; use the Master Theorem as a recipe for divide-and-conquer recurrences.
4. Implement inheritance and polymorphism; design systems with multiple interacting classes.
5. Use Python dictionaries fluently and explain the role of a hash function as a mapping from keys to bucket indices.
6. Reason about mutability, aliasing, and object references; explain why two names can refer to the same object and what follows from that.
7. Implement stack and queue abstract data types in at least two ways, demonstrating that the interface is independent of the implementation.
8. Write shell scripts that orchestrate Python programs; use positional parameters, branching, and loops in bash.
9. Write complete test suites including edge cases; document code with full docstrings.
10. Describe iteration, recursion, and object-oriented design in terms that are independent of Python syntax, in preparation for working in other languages.

---

## How This Course Works

COMP 159 continues where COMP 158 left off. The terminal remains the only development environment. Git and `make` remain the submission and build mechanisms. The pace is faster: students arrive with the baseline, and the course moves directly into new material.

The semester's mathematical arc runs alongside the programming arc: mathematical induction justifies recursion; recurrence relations describe recursive algorithms; Big-O formalizes the intuition of "how fast does this grow"; expected value connects to hash table behavior; function composition names what shell pipelines do. None of these is a detour — each arrives in the week where the programming concept needs it.

One session near the end of the semester compiles a Java program from the terminal. This is not an introduction to Java. It is a demonstration that the terminal workflow, and the conceptual vocabulary built in COMP 158 and 159, transfers immediately to any language. The tools do not change; the compiler does.

---

## Assignments and Grading

| Component | Weight | Notes |
|-----------|--------|-------|
| Programming assignments | 45% | Approximately one per week; submitted via `git push` |
| Midterm exam | 20% | Written; covers weeks 1–7 |
| Capstone project | 30% | Weeks 13–14; see description below |
| Participation | 5% | In-class exercises and engagement |

### Programming Assignments

Assignments are posted Monday and due the following Sunday at 11:59 pm. `make test` must pass before submission. Assignments in the second half of the semester are longer and require more design judgment — start early.

**Late policy:** 10% deducted per calendar day. No submissions accepted more than five days after the deadline without a documented exception arranged in advance.

### Midterm Exam

A written exam covering weeks 1–7: recursion, recurrence relations, Big-O, sorting, and inheritance. You will be asked to trace recursive execution, write recurrences for given code, compare growth rates, and implement a subclass.

### Capstone Project

The semester capstone is a multi-class Python program developed over the final two weeks. Requirements:

- At least two classes connected by inheritance
- At least one recursive operation
- A dictionary used for grouping, counting, or memoization
- File input for the primary data
- A complete test suite run via `make test`, including edge cases
- Full docstrings on all functions, methods, and classes
- Submitted via `git push`

The capstone is the primary assessment artifact for the integrated sequence. It is individual work. **An oral exit interview of approximately 15 minutes is required for all students.** You will be asked to walk through your code, explain your design decisions, and demonstrate the program running in the terminal. The interview is scheduled during the final week of classes.

> **IRB note:** Oral exit interviews may be recorded for research purposes. Participation in recording is voluntary and does not affect your grade. Consent forms will be distributed in advance.

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
| 1 | Recursion: the concept | Base case, recursive case, call stack; induction intuition |
| 2 | Recursion patterns | Head/tail decomposition; recurrence relations, unrolling |
| 3 | Algorithm analysis | Counting operations; Big-O notation, growth rate comparison |
| 4 | Sorting | Selection, insertion, merge sort; T(n) = 2T(n/2) + n; Master Theorem |
| 5 | Inheritance | Subclass as subset; `super()`, method overriding, `isinstance()` |
| 6 | Polymorphism and multi-class design | `Node` + container pattern; composition vs. inheritance |
| 7 | Dictionaries and hashing | Hash function as a mapping; `dict` creation, lookup, comprehension |
| 8 | Mutability and object references | Aliasing, shallow vs. deep copy; `id()`, mutable vs. immutable |
| 9 | Probability and expected-case analysis | Sample spaces, expected value; simulating hash collision rates |
| 10 | Abstract data types | Stack and queue; two implementations, same test suite |
| 11 | Shell scripting in depth | Functions, `$1`/`$@`, loops; `sys.argv`; pipeline as composition |
| 12 | Testing and code quality | Test suites, edge cases, `diff`-based testing; loop invariants; `raise`, `try`/`except` in tests |
| 13 | Language-agnostic thinking | Concepts without syntax; Java Hello World from the terminal |
| 14 | Capstone and oral exit interview | Project due; oral interview scheduled this week |

*The schedule may shift by a session or two as the semester develops. Any changes will be announced in class and posted to the course repository.*

---

## Course Policies

### AI Tools

The policy from COMP 158 continues and, if anything, matters more here. The topics in COMP 159 — recursion, algorithm analysis, class design — are exactly the topics where AI tools produce plausible-looking but frequently wrong code. A recursive function with no base case terminates with an error; an O(n²) algorithm where an O(n log n) one was needed passes all small tests and fails in production.

You may use AI tools to understand concepts and debug errors. You may not submit AI-generated code as your own. The oral exit interview is specifically designed to distinguish between students who understand their code and students who do not.

### Academic Integrity

All submitted work must be your own unless otherwise specified. The same standards as COMP 158 apply. Violations are referred to the Dean's office.

### Attendance

No formal attendance grade, but in-class exercises count toward participation and cannot be made up. The oral exit interview in week 14 is required — contact us immediately if a scheduling conflict arises.

### Accessibility

Students who require accommodations should contact the accessibility office and share documentation with the instructors within the first two weeks of the semester. Oral exit interviews can be conducted in alternative formats with appropriate accommodation documentation.

### Communication

Questions about assignments go to the course discussion board. Email for personal matters. We aim to respond within one business day.

---

## Preparation for COMP 271

Students who complete COMP 159 are ready for COMP 271 (Data Structures). That course assumes:

- Python fluency, including OOP through inheritance and polymorphism — covered in COMP 158 and 159
- Comfort with the command-line environment — the working environment throughout COMP 158 and 159
- Familiarity with Big-O notation and basic algorithm analysis — covered in weeks 3–4 of COMP 159
- Conceptual understanding of linked structures — previewed in the `Node` + container exercises in week 6

Students who struggle with any of these in COMP 271's first two weeks should come to office hours immediately. The gaps are fixable; letting them compound is not.

One further note on COMP 272, which follows COMP 271: that course is taught in Java. Students who understand iteration, recursion, and object-oriented design as concepts — not as Python syntax — will find the language transition straightforward. Week 13 of this course is specifically designed with that transition in mind.

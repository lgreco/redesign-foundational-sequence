# Proposal: COMP 158 and COMP 159
## An Integrated Introductory Sequence in Programming, Mathematics, and Computing Tools

---

## The Problem

Students who complete COMP 141 (computing tools), COMP 163 (discrete mathematics), and COMP 170 (introductory programming) arrive at COMP 271 (data structures) underprepared — not because the courses are weak, but because the courses do not talk to each other. This underpreparation is amplified as students cap off the foundational sequence (271, 272, 363) and enter upper classes with serious gaps.

Three specific symptoms repeat across cohorts:

1. **CLI skills do not carry forward.** Students who used the terminal in COMP 141 have largely abandoned it by the time they reach COMP 271. They write Python in an IDE and have no habit of using `git`, `make`, or the command line as a development environment.

2. **Discrete math stays abstract.** Students who saw summation notation and quantifiers in COMP 163 cannot recognize those concepts in code. A student who learned ∑ xᵢyᵢ in math does not connect it to a `for` loop accumulator in Python — because the two were never presented together.

3. **COMP 170 stops short of what COMP 271 expects.** The current COMP 170 schedule ends before reaching inheritance, recursion, Python dictionaries, or mutability. All four appear in the first weeks of COMP 271. Students are not missing isolated topics — they are missing the OOP vocabulary that COMP 271 is built on.

In our opinion, the root cause is not the content of any single course. It is isolation: three subjects taught by different instructors in different semesters with no explicit connective tissue between them.

There is a second, less immediate concern. AI coding tools are now capable of generating syntactically plausible code for well-described tasks. What they do not substitute for is the judgment to evaluate that code — to recognize when it is wrong, inefficient, or solving the wrong problem. That judgment is not a syntactic skill. It depends on understanding why programs behave the way they do: the mathematical structure behind an algorithm, the behavior of the system beneath the code, the cost of a design decision at scale. Our current sequence produces students who have encountered these ideas separately, in different courses, in different semesters. Familiarity without integration is exactly what AI tools replicate most effectively. Understanding that cuts across math, tools, and code is not.

---

## The Proposal

We propose two new courses — **COMP 158** and **COMP 159** — offered back-to-back in a Fall/Spring arrangement, co-taught by two instructors. Together they cover the material currently distributed across COMP 141, 163, and 170, with three significant changes:

1. **Topics are sequenced around programming concepts**, not around course boundaries. Math and CLI tools appear when they illuminate a programming idea, not on a separate schedule. Propositional logic arrives the week students write their first `if` statement. Summation notation arrives the week before the accumulator loop. Quantifiers arrive alongside `while` and `break`.

2. **The terminal is the only programming environment.** No IDE. Students write code in Vim or nano, run it from the shell, manage it with Git, and build it with `make`. CLI fluency is not a module — it is the substrate every assignment runs on.

3. **The content is rationalized against the actual downstream pipeline.** Topics from the three source courses that have no direct application in COMP 271 or COMP 272 — combinatorial circuits, Boolean algebra as a standalone subject, four weeks of file processing, C compilation, networking commands — are deferred to later courses where they arise naturally. Topics the source courses do not reach — inheritance, recursion, dictionaries, mutability, Makefiles — are added, because COMP 271 assumes them.

---

## Course Outline

Each course runs 14 weeks at three 50-minute or two 75-minute sessions per week.

### COMP 158 — Fall

The arc: environment → values and types → logic and conditionals → functions → sequences and vectors → iteration → list algorithms → sets → number representation → classes.

| Week | Central concept | Math introduced |
|------|----------------|-----------------|
| 1 | Terminal, filesystem, first Python | — |
| 2 | Values, types, variables | Types as sets |
| 3 | Logic and conditionals | Propositions, truth tables, De Morgan's laws |
| 4 | Functions: the mathematical idea | Functions as mappings; domain, codomain |
| 5 | Designing and testing functions | Pre/post conditions; docstrings; `assert` |
| 6 | Sequences and vectors | Sequences, vectors, indexing, summation ∑ |
| 7 | Iteration — the `for` loop | Universal quantifier ∀; ∑ as a loop |
| 8 | Searching — the `while` loop | Existential quantifier ∃; negation of ∀ |
| 9 | List algorithms, comprehension | Set-builder notation |
| 10 | Sets | Set theory: ∈, ∪, ∩, ×, power sets |
| 11 | Number representation | Binary and hexadecimal |
| 12 | Classes and objects | Mathematical structures |
| 13 | Multi-class design | Relations, equivalence, partial orders |
| 14 | Capstone | Review: each math concept paired with its programming analog |

### COMP 159 — Spring

The arc: recursion → algorithm analysis → sorting → inheritance and polymorphism → dictionaries and hashing → mutability → probability and expected-case analysis → abstract data types → shell scripting → testing → language-agnostic thinking.

| Week | Central concept | Math introduced |
|------|----------------|-----------------|
| 1 | Recursion: the concept | Mathematical induction — intuition |
| 2 | Recursion patterns | Recurrence relations; solving by unrolling |
| 3 | Algorithm analysis | Big-O notation; growth rates |
| 4 | Sorting | T(n) = 2T(n/2) + n; O(n log n); Master Theorem |
| 5 | Inheritance | Subclass as subset; Liskov substitution |
| 6 | Polymorphism; multi-class design | Composition of structures |
| 7 | Dictionaries and hashing | Hash function as a mapping; pigeonhole principle |
| 8 | Mutability and object references | Reference model; aliasing |
| 9 | Probability and expected-case analysis | Sample spaces; expected value |
| 10 | Abstract data types | Interface vs. implementation |
| 11 | Shell scripting in depth | Pipelines as function composition |
| 12 | Testing and code quality | Loop invariants; pre/post with ∀ |
| 13 | Language-agnostic thinking | Type systems; invariants |
| 14 | Capstone | Full review |

The COMP 159 capstone requires inheritance, a recursive operation, a dictionary, file input, and a complete test suite — all submitted via `git push` and built with `make`. It directly generates the CLI and programming assessment artifacts called for in the evaluation framework.

---

## What Is Not Covered

The following topics appear in the source courses and are deliberately not included. This is a design decision, not an oversight.

| Topic | Source | Reason for deferral |
|-------|--------|---------------------|
| Networking: `ssh`, `scp`, `sftp` | COMP 141 | Belongs in a systems or networking course |
| C compilation | COMP 141 | Not on the Python → Java path |
| Combinatorial circuits, logic gates | COMP 163 | Digital logic / computer architecture |
| Boolean algebra (standalone) | COMP 163 | Subsumed by De Morgan's; rest motivated by circuits |
| Strong induction, formal proof-writing | COMP 163 | COMP 271/272 do not require writing proofs |
| Binomial theorem | COMP 163 | No direct application in 271/272 |
| Conditional probability (formal) | COMP 163 | Statistics / ML territory |
| Floating-point representation (IEEE 754) | COMP 163 | Numerical methods; awareness note only |
| Deep file I/O (currently 4 weeks) | COMP 170 | Reduced to one session |

None of these topics disappears from the curriculum. They move to courses where students will use them immediately rather than abstractly.

---

## Pilot Structure

**Treatment group:** ~25–30 students per cohort take COMP 158 → COMP 159 → COMP 271.

**Control group:** Matched students from the concurrent and recent legacy sequence (COMP 141 + 163 + 170 → COMP 271). Matched on declared major, incoming math placement score, and term of first CS course.

**Timeline:**
```
Year 1 Fall   → Cohort 1 begins COMP 158
Year 1 Spring → Cohort 1 takes COMP 159; Cohort 2 begins COMP 158
Year 2 Fall   → Cohort 1 enters COMP 271 (primary outcome window)
               → Cohort 2 takes COMP 159
Year 2 Spring → Cohort 2 enters COMP 271 (replication window)
               → Cross-cohort analysis and report
```

Two cohorts allow Year 2 to replicate and refine Year 1 findings, and to test whether the novelty of a new course — not the design — explains any observed improvement.

---

## How We Will Know If It Works

**Primary outcome:** COMP 271 performance. We collect final grade, grade on the first programming assignment, and withdrawal rate for both treatment and matched control students. Additionally, COMP 271 instructors — ideally without knowing which students came from which sequence — rate a random sample of submitted work on code organization, tool use, and mathematical reasoning.

**Secondary outcomes:** Three short concept tests (~10 items each) administered at entry to 158, exit from 159, and entry to 271:

- *Module A:* CLI fluency — scenario-based tasks ("given this directory tree, write the command that...")
- *Module B:* Math operationalization — translating formulas into code ("given **x**·**y** = ∑ xᵢyᵢ, write a Python loop that computes it")
- *Module C:* Programming concepts — adapted from the validated FCS1 inventory

**CLI artifacts:** Shell history exports (opt-in, anonymized) and submission logs analyzed for command vocabulary, use of piping, and presence of scripting constructs at the end of 158, 159, and the first week of 271.

> **IRB note:** Shell history exports and any oral exam recordings may require IRB approval and participant consent before data collection begins.

**Success threshold:** The pilot is a candidate for adoption if it meets at least three of these four criteria:

1. Statistically significant higher gain scores on Module B (math operationalization) at COMP 271 entry.
2. COMP 271 first-assignment grade ≥ 0.3 letter grades higher on average than matched controls.
3. CLI artifacts in COMP 271 week 1 rated higher for treatment students in a blinded rubric review.
4. Retention from end of intro sequence to COMP 271 enrollment at least 5 percentage points higher for the treatment group.

Meeting two criteria warrants a revised second offering before a broader rollout decision.

---

## What We Are Asking For

1. **Approval to offer COMP 158 and COMP 159 as experimental sections** beginning in the fall semester of Year 1, running in parallel with the existing legacy sequence for the duration of the pilot.

2. **Two faculty assigned to co-teach**, one with strength in systems and tools, one with strength in algorithms and discrete math. The co-teaching model is itself under evaluation — pedagogical coherence from the student perspective is one of the research questions.

3. **A target enrollment of 25–30 students per cohort**, recruited from incoming students who declare CS or a related major. Voluntary enrollment with standard academic credit.

4. **Access to COMP 271 grade data** for the matched control group, subject to applicable data governance requirements.

5. **A two-year evaluation window** before any decision on scaling, replacement of the legacy sequence, or discontinuation.

---

## The Argument in Brief

Three courses taught in isolation have not produced the preparation COMP 271 needs. The proposal does not ask for more content or more credit hours — it asks to reorganize what we already teach so that the terminal, the math, and the code are learned together, in a sequence where each concept arrives exactly when it earns its place.

The pilot is small, the evaluation plan is concrete, and the legacy sequence runs in parallel throughout. The cost of trying this is low. The cost of not finding out whether it works is borne quietly, every semester, in COMP 271.

One final point. A student who understands that a dot product is ∑ xᵢyᵢ and can recognize that structure in a `for` loop with an accumulator has understood something. A student who can produce the same loop by copying a familiar pattern has not. The difference has always mattered; it matters more now. AI tools are fluent at producing the pattern. They are not a substitute for understanding what the pattern does, when it is correct, and when a different approach is needed. The integrated sequence is designed to produce students who can direct, evaluate, and correct generated code — because they understand the mathematics behind it and the system beneath it. That is the kind of grounding that remains valuable regardless of how the tools change.

# COMP 158/159 Pilot Project

## Context

You are a computer science professor collaborating with colleagues to redesign the introductory CS sequence. The working hypothesis is that teaching COMP 141 (CLI/tools), COMP 163 (discrete math), and COMP 170 (CS1/Python) as separate courses — often spaced 1–2 semesters apart — produces low retention of foundational skills by the time students reach CS2.

The proposed remedy is two integrated back-to-back courses, **COMP 158** (fall) and **COMP 159** (spring), where CLI tools, discrete mathematics, and programming are interlaced weekly. The courses are **co-taught by two instructors**. The full rationale and assessment plan are in [assessment.md](./assessment.md).

## Pedagogical Decisions Already Made

These are settled design choices — do not relitigate them unless asked:

- **CLI-first**: the terminal is the primary environment for all work. No IDE. Students use Vim or nano, run Python from the shell, and submit via `git push` from week 2 onward.
- **Math in service of programming**: mathematical concepts (logic, sets, combinatorics, recurrences) are introduced at the moment they clarify what a program is doing — not on a separate schedule.
- **Sequence driven by programming concepts**: the weekly order follows programming development (types → logic → functions → sequences → iteration → OOP → recursion → algorithm analysis), with math and CLI woven in.
- **Python → Java transition**: COMP 158/159 and the immediate downstream course (COMP 271) use Python. COMP 272 uses Java. The integrated sequence should build language-agnostic intuition (separating concepts like recursion and iteration from syntax) so the Python-to-Java shift in COMP 272 is not a barrier.

## Work in Progress

Draft files already in this repo — read these before proposing changes to content they cover:

- [proposal.md](./proposal.md) — original rationale memo
- [syllabus-158.md](./syllabus-158.md) — full draft syllabus for COMP 158
- [syllabus-159.md](./syllabus-159.md) — full draft syllabus for COMP 159
- [topics-141-163-170.md](./topics-141-163-170.md) — topic-by-topic breakdown of the three legacy courses
- [topics-158-159.md](./topics-158-159.md) — week-by-week topic plan for the integrated sequence

## Tasks

Typical work includes: refining syllabi and weekly topic plans, designing rubrics, mapping topic integrations across source courses, writing assessment instruments, analyzing data, and drafting memos for the curriculum committee. Outputs may go to faculty colleagues or the curriculum committee — tone should be collegial and evidence-grounded.

## Conventions
- Responses in Markdown
- Avoid education jargon; prefer plain language
- Assessment framework targets two cohorts over two years

## Key Constraints
- Student data available: grades from approximately 270 student records, concept tests, oral exams, CLI artifacts
- No retention/continuation rate data
- ~25–30 students per treatment cohort

## Standing Instructions
- When proposing rubrics, keep them to 3-point scales
- Flag any assessment instrument that requires IRB consideration

## Source Syllabi

Original course materials are in [./sources/](./sources/).

Courses being integrated:

- [COMP 141](./sources/COMP%20141%20Syllabus%20Spring%202026.pdf) — CLI and computing tools
- [COMP 163](./sources/COMP%20163%20Syllabus%20Spring%202026.pdf) — discrete mathematics
- [COMP 170](./sources/COMP%20170%20Syllabus%20Spring%202026.pdf) — introductory programming (CS1, Python)

Downstream courses the integrated sequence must prepare students for:

- [COMP 271](./sources/COMP%20271%20Syllabus%20Spring%202026.pdf) — linear data structures (CS2, Python)
- [COMP 272](./sources/COMP%20272%20Syllabus%20Spring%202026.pdf) — non-linear data structures (Java)
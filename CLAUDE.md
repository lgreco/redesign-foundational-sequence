# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A curriculum design project at Loyola University Chicago. The primary work is redesigning the introductory CS sequence by proposing two integrated courses — **COMP 158** (fall) and **COMP 159** (spring) — to replace three separate legacy courses: COMP 141 (CLI/tools), COMP 163 (discrete math), and COMP 170 (CS1/Python). The downstream courses the sequence must prepare students for are COMP 271 (CS2, Python) and COMP 272 (non-linear data structures, Java).

The two principal authors are Leo Irakliotis and Karima Ennaoui.

## Repository structure

| Folder / file | Purpose |
|---|---|
| `proposal_158_159/` | Curriculum design documents: proposal, syllabi, topic plans, assessment framework, and QA notes. Contains its own `claude.md` with detailed context — read it before working on proposal content. |
| `comp170su26/` | **Private** — development and planning materials for the Summer 2026 COMP 170 section: weekly review drafts, class session notes, code files, and Lubanovic textbook excerpts (`blubanovic<NN>.pdf`). Not student-facing. |
| `comp271su26/` | **Private** — same role for the Summer 2026 COMP 271 section. Not student-facing. |
| `../../comp-170-su26/` | **Student-facing** sibling repo for COMP 170. Published material goes here. |
| `../../comp-271-su26/` | **Student-facing** sibling repo for COMP 271. Published material goes here. |
| `recording_transcripts/` | Raw closed-caption `.txt` transcripts and the processed per-class `.md` summaries split by course. Contains a `summarize_transcript_prompt.md` prompt that governs how transcripts are processed. |
| `sources/` | Original syllabi PDFs for COMP 141, 163, 170, 271, and 272 (Spring 2026). |
| `.github/` | CI workflow and publish script (see below). |

## Recurring tasks

### Summarizing transcripts

Raw transcripts are in `recording_transcripts/YYYY-MM-DD.txt`. Class times:
- COMP 271: 10:25–11:15 AM
- COMP 170: 11:30–12:20 PM

Use timestamps to split each `.txt` into two `.md` summaries (`YYYY-MM-DD-COMP170.md` and `YYYY-MM-DD-COMP271.md`) and place them in `recording_transcripts/`. After writing both files, copy each to its respective sibling repo directory (`../../comp-170-su26/` and `../../comp-271-su26/`). Full instructions are in `recording_transcripts/summarize_transcript_prompt.md`.

### Writing weekly review documents

Weekly review documents (`week<NN>-review.md`) live in `comp170su26/` and `comp271su26/`. Each course has a dedicated prompt file that governs structure, style, and sourcing — read it before writing:
- COMP 170: `comp170su26/weekly-review-prompt.md`
- COMP 271: `comp271su26/weekly-review-prompt.md`

Before writing, read the class session notes and any `.py` files for that week from the corresponding `../comp-<NNN>-su26/week<NN>/` sibling repo directory.

### Planning the next week's content

To suggest a plan for week N+1, read the following in order:

1. **Private folder** (`comp170su26/` or `comp271su26/`) — all `week<NN>-plan.md`, `week<NN>-review.md`, and any code or notebook files present.
2. **Student-facing folder** (`../../comp-170-su26/` or `../../comp-271-su26/`) — the `week<NN>/` subdirectories for all completed weeks: class session notes (`.md` files named by date), code artifacts (`.py` files), and any assignment files (`week<NN>-assignment.md`). Read through the most recent week's materials carefully.
3. **Deferred topics** — check the previous plan's "Topics Deferred to Later Weeks" section, and the "Looking ahead" or "Next week" notes in the most recent class session summaries.

Then write `week<N+1>-plan.md` in the private folder (`comp170su26/` or `comp271su26/`). Follow the structure of the existing plan files in those folders:
- Open with a "Continuity from Week N" section that names the specific endpoint of the previous week and the thread that carries into this one.
- Number the main content sections.
- Include a **Reading** section (after "Concepts to Name This Week", before "Exercises") as a table mapping topics to sources.
- End with an Exercises section (each exercise preceded by `---`) and a "Topics Deferred to Later Weeks" section.

**Reading sources:** All URLs and descriptions for the Reading section must be drawn from the reading tables in the respective student-facing CLAUDE.md:
- COMP 170 readings: `../../comp-170-su26/CLAUDE.md` → "Reading Materials" table
- COMP 271 readings: `../../comp-271-su26/CLAUDE.md` → "Reading Materials" tables (Python Official Documentation, Lubanovic, Shell and Editor Resources)

Do not invent URLs. If a needed resource is not yet in those tables, note it as a placeholder and flag it for the instructor to add.

Do not write to the student-facing repo — plans are private working documents.

### Publishing review documents

Pushing a `comp*su26/week*-review.md` file triggers the GitHub Actions workflow at `.github/workflows/publish-review.yml`. It runs `.github/scripts/publish_review.py`, which clones the target student-facing repo (`comp-<NNN>-su26`), copies the review file and any locally-linked assets into a `week<NN>/` subdirectory, and pushes a commit. The workflow requires a `PUBLISH_TOKEN` secret with write access to the target repos.

## Math formatting

Use LaTeX for all mathematical notation in `comp170su26/` and `comp271su26/` materials (plans, reviews, assignments). Inline math uses `$...$`; display math uses `$$...$$`. Examples: $O(n)$, $T(n) \leq c \cdot f(n)$, display-block equations for sums or formal definitions. Plain English approximations ("proportional to n", "constant time") are fine as companions to the LaTeX, but do not substitute for it.

## Terminology conventions (apply across all course materials)

- Use **method** instead of **function** everywhere except when referring to a strictly mathematical function. This applies to `print()`, `input()`, user-defined `def` blocks, and all general discussion of callable code. Do not use "functions" in headings, prose, code comments, or reference cards.
- Avoid education jargon; prefer plain language.
- Assessment rubrics use **3-point scales**. Flag any assessment instrument that may require IRB consideration.
- The assessment framework targets two cohorts over two years (~25–30 students per treatment cohort). Available data: ~270 historical student records, concept tests, oral exams, CLI artifacts. No retention/continuation rate data exists.

## Settled design decisions (do not relitigate unless asked)

- **CLI-first (weeks 1–8 of COMP 158):** Vim + terminal only; VS Code introduced in week 9.
- **Math in service of programming:** mathematical concepts arrive when they clarify what a program is doing, not on a separate schedule.
- **Sequence order:** types → logic → functions → sequences → iteration → OOP → recursion → algorithm analysis.
- **Python → Java transition:** COMP 158/159/271 use Python; COMP 272 uses Java. Build language-agnostic intuition throughout.

## Key source documents

Before proposing changes to proposal content, read the relevant files in `proposal_158_159/`:
- `proposal.md` — original rationale memo
- `syllabus-158.md` / `syllabus-159.md` — full draft syllabi
- `topics-158-159.md` — week-by-week topic plan
- `topics-141-163-170.md` — legacy course topic inventory with gap analysis
- `assessment.md` — full rationale and two-year assessment framework

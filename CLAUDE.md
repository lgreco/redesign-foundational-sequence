# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A curriculum design project at Loyola University Chicago. The primary work is redesigning the introductory CS sequence by proposing two integrated courses — **COMP 158** (fall) and **COMP 159** (spring) — to replace three separate legacy courses: COMP 141 (CLI/tools), COMP 163 (discrete math), and COMP 170 (CS1/Python). The downstream courses the sequence must prepare students for are COMP 271 (CS2, Python) and COMP 272 (non-linear data structures, Java).

The principal authors are Leo Irakliotis, Karima Ennaoui, and Eric Chantin.

This repository is scoped tightly to two things: the COMP 158/159 redesign proposal and the CFD Human-Centered AI grant built on it. `proposal_158_159/legacy_outline_170_271.md` is the ground-truth record of what the Summer 2026 COMP 170/271 pilot terms actually covered — use it as the source for that history.

## Repository structure

| Folder / file | Purpose |
|---|---|
| `proposal_158_159/` | Curriculum design documents: proposal, syllabi, topic plans, assessment framework, QA notes, and the legacy-sequence ground-truth record. Contains its own `claude.md` with detailed context — read it before working on proposal content. |
| `luc_ai_grants/` | Draft materials for a CFD Human-Centered AI grant proposal (`proposal_outline.md`, `rationale.md`), built on the completed Summer 2026 COMP 170/271 pilot as feasibility evidence for the COMP 158/159 sequence. |
| `sources/` | Original syllabi PDFs for COMP 141, 163, 170, 271, and 272 (Spring 2026). |

## Math formatting

Use LaTeX for all mathematical notation in this repository's materials (proposal content, grant materials, planning documents). Inline math uses `$...$`; display math uses `$$...$$`. Examples: $O(n)$, $T(n) \leq c \cdot f(n)$, display-block equations for sums or formal definitions. Plain English approximations ("proportional to n", "constant time") are fine as companions to the LaTeX, but do not substitute for it.

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

## Pedagogical Decisions Already Made

- **AI use is framed as human-centric, not incidental.** Every AI-mediated element of the sequence (e.g., agent-conducted oral exams) must be defensible as *restoring* a human pedagogical practice at scale, not replacing it. The standing example: agent-conducted orals are framed as recovering *viva voce* assessment in a large-enrollment CS1 where the realistic alternative is an autograder scoring unsubmitted-for-defense code, not a professor sitting with each student. Faculty retain evaluative judgment; students remain obliged to articulate reasoning aloud.
- **When evaluating any AI-integration choice in this curriculum, ask first what human practice it recovers or protects**, and name that explicitly — this is the throughline for CFD Human-Centered AI grant framing (see `luc_ai_grants/rationale.md` and `luc_ai_grants/proposal_outline.md`) and should inform how COMP 158/159 syllabi, assessment design, and any AI-policy language are written.
- **Where AI should be disallowed is a deliberate design decision, not a gap.** Don't default to permitting AI use in an assignment or activity; treat prohibition as an equally legitimate, explicitly reasoned pedagogical choice alongside adoption.

**Documented precedent:** `proposal_158_159/legacy_outline_170_271.md` retroactively frames AI-mediated elements already used in the completed Summer 2026 COMP 170/271 terms (agent-conducted orals, AI-assisted grading) through this same human-centric/recovery lens, so the completed terms can serve as documented precedent/evidence for the CFD grant proposal rather than being left as undocumented practice.

## Key source documents

Before proposing changes to proposal content, read the relevant files in `proposal_158_159/`:
- `proposal.md` — original rationale memo
- `syllabus-158.md` / `syllabus-159.md` — full draft syllabi
- `topics-158-159.md` — week-by-week topic plan for the integrated sequence
- `topics-141-163-170.md` — legacy course topic inventory with gap analysis (syllabus-on-paper view)
- `legacy_outline_170_271.md` — the legacy sequence *as actually taught* in Summer 2026 (lived-experience ground-truth, reconstructed after the source folders were removed)
- `comp170-revised.md` — COMP 170 content rearranged to show how it maps onto COMP 158 and the first half of COMP 159
- `assessment.md` — full rationale and two-year assessment framework
- `qa.md` / `checklist.md` — open questions and review checklist

Before proposing changes to grant content, read `luc_ai_grants/proposal_outline.md` and `luc_ai_grants/rationale.md`.

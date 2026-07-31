# Session Prompt: End-of-Term Wrap-Up

## Context

This is COMP 170, an introductory programming course (CS1) at Loyola University Chicago, using Python. Like COMP 271, it has a student-facing repo (`../comp-170-su26/`) and this private instructor-facing folder (`comp170su26/`) inside `redesign-foundational-sequence/`. The term has ended. This prompt produces the same five end-of-term deliverables that closed out the Summer 2026 COMP 170 term, adapted to whatever this term of COMP 170 actually covered.

Run this as one session, in order — each step benefits from the reading done in the previous one.

**If `../comp-170-su26/week99/` or `comp170su26/week99/` already contain files from a previous term**, do not silently overwrite them — check their dates/content first, and ask the instructor whether this term's output should replace them, sit alongside them under a term-qualified filename, or move the old ones into a dated subfolder before writing the new ones.

## What to read at the start of the session

1. **Every folder** in `../comp-170-su26/` — all `week<NN>/` directories, in full: class session notes (`.md`, named by date), code artifacts (`.py`), assignment files (`week<NN>-assignment.md`), and posted solutions. Also read `../comp-170-su26/CLAUDE.md` for the repo's own content table, reading-materials table, and any style/terminology conventions already established there.
2. **This private folder** (`comp170su26/`) — all `week<NN>-plan.md`, `week<NN>-review.md`, and the Lubanovic excerpts (`blubanovic<NN>.pdf`), for context on what was planned vs. what actually happened in class.
3. **The redesign proposal** — read `../proposal_158_159/topics-141-163-170.md` for the standing gap analysis of what COMP 170 is missing relative to COMP 271, and `../proposal_158_159/comp170-revised.md` for how this material has already been rethought at semester length. Check whether anything this term repeats a gap that analysis already named (dictionaries taught late, no git, testing introduced late, etc.) — if a past improvements.md exists (`comp170su26/improvements.md`), read it too, since it may already flag exactly this.
4. **`redesign-foundational-sequence/CLAUDE.md`** (repo root) — for terminology conventions (method vs. function, LaTeX math formatting) and the settled design decisions section.

## The task

### Step 1 — Course review (student-facing repo)

Write `../comp-170-su26/week99/course-review.md`: a retrospective tracing the course's actual week-by-week progression. Track how the course covered its core recurring themes — for COMP 170 that's the instructor's "four pillars" (strings, if statements, loops, arrays), unless this term's actual content departed from that framing, in which case identify and use whatever themes actually recurred. Show where each pillar/theme was introduced and where it recurred and combined with the others later. Close with a section on what the course had no time to cover, framed as self-study suggestions for students, not as a critique.

### Step 2 — Final assignment (student-facing repo) — course-specific, do not reuse a prior term's content

Write `../comp-170-su26/week99/last_assignment.md`. **This is the one step that does not carry over from a prior term verbatim** — the Summer 2026 last assignment (URL reading, punctuation stripping, dictionaries, word frequency) was built around what that specific term happened to end on. For this term:

- Base the assignment's technical content on whatever topic the course actually closed on (check the last `week<NN>/` folder and the last class session notes for this).
- Include a short tutorial section for any technique the assignment needs that hasn't been formally taught yet, in the same explain-from-first-principles style as the rest of the course's materials (minimal imports, avoid heavier tools like `re` when a simpler built-in approach exists, ground new vocabulary in a named OER chapter).
- Follow the exact "How to Submit" and "How Your Work Is Evaluated" templates already established in `../comp-170-su26/CLAUDE.md`.
- Include a reflection component: a short (~300-word) self-graded write-up covering attendance, participation, and how closely the student's own code matched posted solutions across the term, submitted as a plain text file separate from the code, with the same attendance-based grade ceiling language used previously (5–9 absences preclude an A unless excused by the university police; 10+ preclude a passing grade) unless the instructor specifies different thresholds for this term.

### Step 3 — Repaced N-week outline (instructor-facing repo)

Write `comp170su26/week99/<N>-week-outline.md`, where `<N>` is a semester-length week count (typically 15) longer than however many weeks this term of COMP 170 actually ran. This is **not a new curriculum** — it is the same material the course actually covered, repaced with more breathing room, where every week carries three threads:

- **Linux/system** — a small, genuinely relevant command-line or tooling nugget, ideally one that parallels or reinforces that week's programming topic (e.g., a shell `for` loop next to a Python `for` loop, `grep`/`find` next to string search, `git` once multi-file projects appear).
- **Programming** — the course's actual content for that stretch, unchanged in scope.
- **Math** — a small, genuinely relevant nugget (number systems, modular arithmetic, the quadratic formula, sequences, whatever fits what's being taught that week), not invented filler.

Use Lubanovic as the primary reading source, citing chapters already established in `../comp-170-su26/CLAUDE.md`'s reading table where they exist; supplement with other real sources (docs.python.org, TLCL, Real Python, Wikipedia, etc.) where needed, and explicitly flag any citation you cannot verify against a real table of contents as a placeholder for the instructor to confirm — do not invent chapter numbers or URLs. Close with a coverage map showing which new week(s) map to which original week, and name explicitly which weeks absorbed the extra pacing room and why.

### Step 4 — Update both CLAUDE.md files

- `../comp-170-su26/CLAUDE.md`: add any missing week rows to the content table (check especially the most recent weeks — this table tends to lag behind the actual repo), add a `week99/` row describing the two new files from Steps 1–2, add a note near the top that the term has ended, and add any new reading-table rows the final assignment required (with a note if a chapter number is inferred rather than verified).
- `redesign-foundational-sequence/CLAUDE.md`: update the `comp170su26/` row in the repository-structure table to mention the term's end and the new `week99/` outline file, and add a one-line pointer to wherever the end-of-term reflection (Step 5) ends up.

### Step 5 — Improvements reflection (instructor-facing repo)

Write `comp170su26/improvements.md`: an honest, specific reflection in two parts. If a prior `improvements.md` already exists from an earlier term, read it first and note in the new one whether its recommendations were acted on this term or are still open.

- **The course** — concrete things worth changing next term, grounded in what you actually observed while reading through the repo (pacing problems, topics introduced too late to reinforce, gaps between what was taught and what the reading table cites, repo hygiene issues, anything the standing gap analysis in `topics-141-163-170.md` predicted that turned out to be true in practice).
- **These Claude sessions** — concrete things about how this session (and future ones like it) could go better: where existing conventions (CLAUDE.md, prompt files) did real work and are worth investing in further, where something had to be inferred rather than verified and should be checked by the instructor, and what would have made this session's output better with less back-and-forth.

## Conventions to carry over

- Use **method**, not **function**, throughout instructor-facing material (`comp170su26/`) — except for genuinely mathematical functions. Match whatever convention `../comp-170-su26/CLAUDE.md` already uses for student-facing material.
- All math notation in LaTeX (`$...$` inline, `$$...$$` display).
- Never invent a URL or a textbook chapter/page number. If it's not already cited somewhere in this repo, mark it as a placeholder and say so.
- Do not write instructor-only content (grade-ceiling policy language, reflections on class dynamics, self-assessment rubrics) into the student-facing repo, or student-facing assignment prose into this private folder.
- Follow the existing document conventions in each repo (assignment templates, review-document structure, prompt-file format) rather than inventing new ones — this file itself follows the format of `weekly-review-prompt.md` for that reason.

## Output

Five new files, across two repos:

```
../comp-170-su26/week99/course-review.md
../comp-170-su26/week99/last_assignment.md
comp170su26/week99/<N>-week-outline.md
comp170su26/improvements.md
```

Plus edits (not new files) to `../comp-170-su26/CLAUDE.md` and `redesign-foundational-sequence/CLAUDE.md`.

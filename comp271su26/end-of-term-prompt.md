# Session Prompt: End-of-Term Wrap-Up

## Context

This is COMP 271, a second programming course (CS2) at Loyola University Chicago, using Python to introduce linear data structures. Like COMP 170, it has a student-facing repo (`../comp-271-su26/`) and this private instructor-facing folder (`comp271su26/`) inside `redesign-foundational-sequence/`. The term has ended. This prompt produces the same five end-of-term deliverables that closed out COMP 170, adapted to whatever COMP 271 actually covered this term.

Run this as one session, in order — each step benefits from the reading done in the previous one.

## What to read at the start of the session

1. **Every folder** in `../comp-271-su26/` — all `week<NN>/` directories, in full: class session notes (`.md`, named by date), code artifacts (`.py`), assignment files (`week<NN>-assignment.md`), and posted solutions. Also read `../comp-271-su26/CLAUDE.md` for the repo's own content table, reading-materials table, and any style/terminology conventions already established there.
2. **This private folder** (`comp271su26/`) — all `week<NN>-plan.md`, `week<NN>-review.md`, and the Lubanovic excerpts (`blubanovic<NN>.pdf`), for context on what was planned vs. what actually happened in class.
3. **The redesign proposal**, if it exists for this course (`../proposal_158_159/`) — read `topics-141-163-170.md` (or its COMP 271/272 equivalent) for any prior gap analysis naming what this course is missing relative to its downstream course.
4. **`redesign-foundational-sequence/CLAUDE.md`** (repo root) — for terminology conventions (method vs. function, LaTeX math formatting) and the settled design decisions section.

## The task

### Step 1 — Course review (student-facing repo)

Write `../comp-271-su26/week99/course-review.md`: a retrospective tracing the course's actual week-by-week progression. Identify this course's own recurring core themes — the COMP 271 analog of COMP 170's "four pillars" (for COMP 271 that's likely something like arrays/lists → stacks/queues → linked structures → recursion → complexity, but confirm against what was actually taught rather than assuming). Show where each theme was introduced and where it recurred/combined with others later. Close with a section on what the course had no time to cover, framed as self-study suggestions for students, not as a critique.

### Step 2 — Final assignment (student-facing repo) — course-specific, do not reuse COMP 170's content

Write `../comp-271-su26/week99/last_assignment.md`. **This is the one step that does not carry over from COMP 170 verbatim** — COMP 170's last assignment (URL reading, punctuation stripping, dictionaries, word frequency) was built around what COMP 170 specifically ended on. For COMP 271:

- Base the assignment on the following; ask the students to create a class, called SimpleHash. The objects should have an underlying array where simple linked list nodes can be stored. The array location of a node is given by some hash function. For simplicity, the nodes' data payload is just a string with a person's name. Hashing is done with hash(string). If the underlying array position is empty, place the node there. If not, append the existing linked list to the new node and place the new node there. Keep track of how many nodes are in the object and also how many elements of the underlying array and used. When usage of underlying array elements exceed a threshold (default value 70%), double the size of the underlying array and redistribute the objects. The class should implement the following methods:
  - add(string)
  - exists(string): bool
  - __str__
  - along with any additional methods necessary.
- Include a short tutorial section for any technique the assignment needs that hasn't been formally taught yet, in the same explain-from-first-principles style as the rest of the course's materials.
- Follow the exact "How to Submit" and "How Your Work Is Evaluated" templates already established in `../comp-271-su26/CLAUDE.md` (or write them fresh, matching COMP 170's wording, if COMP 271's CLAUDE.md has no template yet).
- Include a reflection component: a short (~300-word) self-graded write-up covering attendance, participation, and how closely the student's own code matched posted solutions across the term, submitted as a plain text file separate from the code, with the same attendance-based grade ceiling language COMP 170 used (5–9 absences preclude an A unless excused by the university police; 10+ preclude a passing grade) unless the instructor specifies different thresholds for this course.

### Step 3 — Repaced N-week outline (instructor-facing repo)

Write `comp271su26/week99/<N>-week-outline.md`, where `<N>` is a semester-length week count (typically 15) longer than however many weeks COMP 271 actually ran this term. This is **not a new curriculum** — it is the same material the course actually covered, repaced with more breathing room, where every week carries three threads:

- **Linux/system** — a small, genuinely relevant command-line or tooling nugget, ideally one that parallels or reinforces that week's programming topic (e.g., a shell loop next to a Python loop, `grep`/`find` next to search algorithms, `git` once multi-file projects appear).
- **Programming** — the course's actual content for that stretch, unchanged in scope.
- **Math** — a small, genuinely relevant nugget (complexity/counting arguments, recurrence intuition, whatever fits what's being taught that week), not invented filler.

Use Lubanovic as the primary reading source, citing chapters already established in `../comp-271-su26/CLAUDE.md`'s reading table where they exist; supplement with other real sources (docs.python.org, TLCL, Real Python, etc.) where needed, and explicitly flag any citation you cannot verify against a real table of contents as a placeholder for the instructor to confirm — do not invent chapter numbers or URLs. Close with a coverage map showing which new week(s) map to which original week, and name explicitly which weeks absorbed the extra pacing room and why.

### Step 4 — Update both CLAUDE.md files

- `../comp-271-su26/CLAUDE.md`: add any missing week rows to the content table (check especially the most recent weeks — this table tends to lag behind the actual repo), add a `week99/` row describing the two new files from Steps 1–2, add a note near the top that the term has ended, and add any new reading-table rows the final assignment required (with a note if a chapter number is inferred rather than verified).
- `redesign-foundational-sequence/CLAUDE.md`: update the `comp271su26/` row in the repository-structure table to mention the term's end and the new `week99/` outline file, and add a one-line pointer to wherever the end-of-term reflection (Step 5) ends up, the same way COMP 170's entry now points to `comp170su26/improvements.md`.

### Step 5 — Improvements reflection (instructor-facing repo)

Write `comp271su26/improvements.md`: an honest, specific reflection in two parts.

- **The course** — concrete things worth changing next term, grounded in what you actually observed while reading through the repo (pacing problems, topics introduced too late to reinforce, gaps between what was taught and what the reading table cites, repo hygiene issues, anything a prior gap analysis predicted that turned out to be true in practice).
- **These Claude sessions** — concrete things about how this session (and future ones like it) could go better: where existing conventions (CLAUDE.md, prompt files) did real work and are worth investing in further, where something had to be inferred rather than verified and should be checked by the instructor, and what would have made this session's output better with less back-and-forth.

## Conventions to carry over from COMP 170

- Use **method**, not **function**, throughout instructor-facing material (`comp271su26/`) — except for genuinely mathematical functions. Match whatever convention `../comp-271-su26/CLAUDE.md` already uses for student-facing material (check first; do not assume it matches).
- All math notation in LaTeX (`$...$` inline, `$$...$$` display).
- Never invent a URL or a textbook chapter/page number. If it's not already cited somewhere in this repo, mark it as a placeholder and say so.
- Do not write instructor-only content (grade-ceiling policy language, reflections on class dynamics, self-assessment rubrics) into the student-facing repo, or student-facing assignment prose into this private folder.
- Follow the existing document conventions in each repo (assignment templates, review-document structure, prompt-file format) rather than inventing new ones — this file itself follows the format of `weekly-review-prompt.md` for that reason.

## Output

Five new files, across two repos:

```
../comp-271-su26/week99/course-review.md
../comp-271-su26/week99/last_assignment.md
comp271su26/week99/<N>-week-outline.md
comp271su26/improvements.md
```

Plus edits (not new files) to `../comp-271-su26/CLAUDE.md` and `redesign-foundational-sequence/CLAUDE.md`.

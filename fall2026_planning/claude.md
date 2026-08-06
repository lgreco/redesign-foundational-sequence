# Fall 2026 Planning

## Context

You are helping Leo Irakliotis plan the Fall 2026 offerings of **COMP 170** (CS1, Python) and **COMP 271** (CS2, Python) — his own sections, taught again after the Summer 2026 terms just ended. This folder is where that near-term planning happens.

This is **not** the same work as `../proposal_158_159/` — that folder is the multi-year proposal to replace COMP 141/163/170 with the new COMP 158/159 sequence, aimed at the curriculum committee. This folder is Leo's own near-term redesign of the courses as they exist *today*, informed by what the Summer 2026 terms revealed, and it can move independently of whether/when the 158/159 proposal is adopted.

## Starting Points

Before proposing changes here, read the end-of-term reflections from the terms that just finished — they name specific things to change, not just general impressions:

- `../comp170su26/improvements.md` — COMP 170 end-of-term reflection
- `../comp271su26/improvements.md` — COMP 271 end-of-term reflection

Both link onward to `week99/` material (a 15-week repacing of the same content, the final course review, and the last assignment) in the respective private and student-facing repos — see the root `CLAUDE.md`'s "What happened at the end of the Summer 2026 COMP 170/271 term" sections for the full pointer chain.

## Theme: Reading Code Before Writing It

The organizing idea for Fall 2026 (COMP 170 so far; may extend to COMP 271): AI tools make generating syntactically correct code cheap, so the scarce skill shifts from *writing* code to *reading* it — predicting what a program does, spotting the one changed instruction that changes everything, before trusting or running it. Lessons built around this theme open with a close-reading exercise, before any syntax is taught, rather than opening with "write your first program."

See `comp-170-lesson-reading-code-before-writing.md` for the first worked example (a matched pair of near-identical recipes, bridged into a matched pair of near-identical Python snippets).

## File Naming

Prefix every file with the course it belongs to: `comp-170-...` or `comp-271-...`. This folder holds planning for both courses side by side, so the prefix is what keeps them apart at a glance.

## Conventions

Inherits everything in the root `CLAUDE.md` — most relevantly:
- Use **method**, not **function**, except for strictly mathematical functions.
- LaTeX for all math (`$...$` inline, `$$...$$` display).
- Do not invent reading URLs — pull only from the reading tables in `../../comp-170-su26/CLAUDE.md` and `../../comp-271-su26/CLAUDE.md`.

## Files in This Folder

- `comp-170-lesson-reading-code-before-writing.md` — first lesson plan built around the reading-first theme; still has open placement/sequencing questions flagged at the bottom.

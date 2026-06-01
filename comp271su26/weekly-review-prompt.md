# Session Prompt: Weekly Review Document

## Context

This is COMP 271, an second programming course (CS2) at Loyola University Chicago. Students have complete a CS1-like course. The course uses Python to introduce linear data structures. The workflow is based initially on the terminal: Bash shell, Vim, and `python3`; later in IDE+GitHub Course material is mostly OER provided by the instructor. For language reference, I recommend *Introducing Python*, 3rd edition, by Bill Lubanovic (O'Reilly), available free to students at https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ using their LUC email.

## What to read at the start of the session

Before writing anything, read all of the following:

1. **Class session notes** for the target week, in `../comp-271-su26/week<NN>/` — one `.md` file per class meeting, named by date (e.g., `2026-05-26-COMP271.md`). These capture what was actually covered, what analogies were used, which students contributed, and what questions came up live.

2. **Code files** for the target week, also in `../comp-271-su26/week<NN>/` — any `.py` files written during or alongside class. Read them carefully; they are the concrete artifacts students worked with.

3. **Textbook excerpts** in `./comp271su26/` — PDF files named `blubanovic<NN>.pdf`. These are chapter excerpts from Lubanovic. Identify which sections are directly relevant to the week's topics before writing.

4. **Existing review documents** in `./comp271su26/` — `week01-review.md` and any previously written `week<NN>-review.md` files. Use these as the style and format reference.

## Open Education Resources (OER) to consult

* https://docs.python.org/3/tutorial/index.html, and in particular:
  * https://docs.python.org/3/tutorial/classes.html 
* https://en.wikipedia.org/wiki/Object-oriented_programming
* https://en.wikipedia.org/wiki/Array_(data_structure)
* https://alandix.com/blog/2021/07/27/a-brief-history-of-array-indices-making-programs-that-fit-people/
* https://www.reddit.com/r/learnprogramming/comments/1s69vfh/i_have_a_question_about_arrays_in_programming/
 

## The task

Write `week<NN>-review.md` in `./comp271su26/`, where `<NN>` is the target week number (zero-padded, e.g., `02`, `03`).

The document should help a CS2 student consolidate and extend what was covered in class that week. It is not a transcript of the lectures — it is a coherent, readable set of notes that:

- Explains the *why* behind each concept, not just the *what*
- Connects class material to the relevant OER including Lubanovic chapters, citing them by name and chapter number
- Uses the class's own examples, analogies, and student moments where they illustrate a point well
- Anticipates confusion points for a first-time programmer and addresses them directly

## Document structure

Follow the structure established in `week01-review.md` and `week02-review.md`:

1. **Opening paragraph** — a brief orientation sentence pointing to the O'Reilly URL and the LUC login note.
2. **Numbered sections** (`## 1.`, `## 2.`, etc.) — one per major concept or topic cluster from the week. Each section has:
   - A clear heading that names the concept
   - Prose explanation (narrative, not just bullets)
   - Code examples in fenced blocks where relevant
   - A Lubanovic reference where the textbook covers the same ground
3. **Exercises** — at the end, before the quick reference card. Follow this format exactly:
   - Horizontal rule (`---`) before each exercise
   - `### Exercise N — [descriptive title]`
   - A brief narrative setup
   - A code block (if applicable)
   - A `Questions:` section with 2–3 numbered questions that prompt the student to think, predict, or explain — not just execute
4. **Quick reference card** — a compact `## Quick Reference Card` section with fenced code blocks covering the new Bash, Vim (if any), and Python syntax from the week.

## Terminology and style conventions

- Use **method** instead of **function** throughout, except when referring to a strictly mathematical function (e.g., the compound interest formula itself). This applies to built-in Python methods (`print()`, `input()`, `int()`, `float()`, `type()`, etc.), user-defined methods defined with `def`, and any general discussion of named, callable code blocks.
- Do not use the word "functions" in section headings, prose, table headers, code comments, or the quick reference card.
- Keep explanations concrete and grounded in the week's specific examples. Avoid abstract generalization without a specific example to anchor it.
- Write for a student who is not yet comfortable with the terminal or with reading code — assume no prior programming experience, but do not be condescending.
- Exercises should require the student to *predict* before running, or to *explain* after running — not just copy and execute. At least one exercise per week should involve introducing a deliberate error and reading the resulting message.

## Output

A single file: `./comp271su26/week<NN>-review.md`

Do not create any other files. Do not modify the class session notes, code files, or PDF excerpts.
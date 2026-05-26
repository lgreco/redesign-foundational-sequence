# Summarize classroom transcript

## Definitions

COMP 271 meets from 10:25 AM to 11:15 AM
COMP 170 meets from 11:30 AM to 12:20 PM

## Input

<YYYY-MM-DD>.txt: closed caption transcript for class meetings on YYYY-MM-DD.

## Output:

YYYY-MM-DD-COMP170.md: summary of discussion for COMP 170.
YYYY-MM-DD-COMP271.md: summary of discussion for COMP 271.

## Task 

For every day (YYYY-MM-DD) for which there are no YYYY-MM-DD-COMP170.md and YYYY-MM-DD-COMP271.md files present:

* Review the input file YYYY-MM-DD.txt.
* Use the timestamps and the class time definitions above to identify which portions of the transcript belong to each class. Ignore any conversation that falls outside both class windows (e.g., one-on-one exchanges after a class ends).
* Write a summary for the COMP 271 class in YYYY-MM-DD-COMP271.md. Keep the summary simple and short, about 250 words. Use markdown headers to organize topics covered.
* Write a summary for the COMP 170 class in YYYY-MM-DD-COMP170.md. Keep the summary simple and short, about 250 words. Use markdown headers to organize topics covered.

## Tone and language

Write from a first-person plural ("we") perspective that treats the class as a shared experience. When a student contributed something in class — sharing their screen, running code, answering a question — acknowledge their role collaboratively rather than describing them as a subject. For example:
* Prefer: "With Evan's help, we demonstrated X" or "We explored X together with Evan"
* Avoid: "Student Evan did X" or "Evan performed X"

Keep the voice active, collegial, and concise.

## Course-level calibration

COMP 170 is a CS1 course — many students are writing code for the first time. COMP 271 is a CS2 course — students have one semester of Python behind them but are still building their mental models of computation.

**For COMP 170 summaries:**
* Avoid technical jargon entirely. Prefer plain English descriptions: "a list of words" not "a string array"; "goes up to but not including" not "exclusive upper bound."
* When a new term is introduced in class, include it but explain it briefly in plain language.
* Focus on what the code *does* in concrete terms — what a student would see in the terminal — rather than on design principles.

**For COMP 271 summaries:**
* Introduce CS terminology precisely but explain it on first use: e.g., "an array — a fixed-size block of memory where every element is the same type."
* Connect new ideas to what students already know from COMP 170, making the progression explicit.
* Capture not just *what* was coded but *why* — the design rationale, the limitation that motivated the new approach.

## Technical accuracy

Summaries must be precise enough that a student could use them to reconstruct what happened in class without being misled.

* **Functions vs. methods**: Standalone functions in Python are *functions*, not *methods*. Methods belong to classes. Do not use these terms interchangeably.
* **Loop bounds**: `range(n)` yields `0` through `n − 1`. Describe ranges as "0 through n − 1", not "0 to n."
* **`print()` behavior**: `print()` with no arguments moves to the next line. It does not insert a blank line *between* rows — only between blocks of output if called at the end of a group.
* **Code behavior**: Describe what the code actually does. If the code checks a condition before doing work (e.g., verifying all letters are the same height), note it — even briefly — because it models a habit worth learning.
* **Python lists vs. arrays**: Python lists are not true arrays. When the course makes this distinction, the summary should reflect it clearly.

* After both summaries are written, copy YYYY-MM-DD-COMP170.md to ../../comp-170-su26/ and copy YYYY-MM-DD-COMP271.md to ../../comp-271-su26/.
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
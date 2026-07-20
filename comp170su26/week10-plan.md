# COMP 170 — Week 10 Plan (Proposed)

*Drafted before any week 10 class session notes exist. Week 10 opens with an async Monday (`monday-async.md`, already posted in the student-facing repo, shared with COMP 271) — students work independently on four LeetCode problems (Two Sum, Reverse String, Palindrome Number, Roman to Integer) instead of meeting live. That leaves two live sessions this week, Tuesday and Wednesday, for new material. This plan covers those two sessions.*

## Continuity from Week 9

Week 9 ended two things and opened a third. It closed out nested-loop substring search (`banana.py`) and built a full `try`/`except` retry pattern for the ATM (`atm.py`), which the week 9 assignment then had students repeat independently in `ATM.py`. The `week09-plan.md` draft had also proposed introducing dictionaries this stretch — replacing `enter_grade`'s chain of `if` checks with a lookup — but that did not happen in class or in the assignment. Dictionaries remain fully unstarted, and this plan defers them again rather than reopening them, at the instructor's direction: **week 10 pivots to file I/O instead.**

That pivot was previewed on the record. July 15's class closed with "Looking Ahead: Files" — a poll on how much memory students' own computers have, which mostly surfaced storage capacities instead, a mix-up the notes call out directly. `week09-plan.md`'s deferred-topics list separately flagged reading and writing text files as "a natural next step once dictionaries and `try`/`except` are in place... the closest analog in the pre-redesign COMP 170 syllabus places file I/O immediately after this stretch of exception-handling material." Week 10 acts on that thread, using it as the concrete payoff for `try`/`except`: a file that fails to open is a raised error like any other, caught and recovered from the same way `int(input(...))` failing was in week 9.

The specific request shaping this week: start from the concept of a file itself, before any syntax — aimed squarely at students who have only ever known unified flash storage (a phone or laptop where "memory" and "storage" are the same chip, nothing spins, nothing seeks) and may have no mechanical intuition for why the memory/storage distinction exists at all. From there, move outward to filesystem concepts, local vs. network vs. cloud storage, Python's `os`/`sys` modules, and finally plain `open()`/read/write operations.

---

## 1. What a File Actually Is (Tuesday)

Open with the July 15 poll's mix-up as the hook: most guesses described storage capacity (128 GB, 256 GB), not memory (8 GB, 16 GB). Ask directly: what's the difference, if a phone doesn't have two visibly different chips the way older machines did?

Draw the distinction concretely, without assuming any mechanical background:

| | Memory (RAM) | Storage (disk/flash) |
|---|---|---|
| What lives there | A running program's variables, right now | Files, saved on purpose, whether or not anything is running |
| Survives the program ending? | No — gone the instant `python3 atm.py` finishes | Yes — still there tomorrow |
| Survives power off? | No | Yes |
| How you reach it in code | By name (`balance = 140`) | By path (`"balance.txt"`) |

Use a whiteboard-vs-notebook analogy: memory is the whiteboard everyone in the room is looking at and writing on right now — erase it (end the program) and every trace is gone. Storage is a notebook — close it, walk away, come back next week, and what's written is still there. Every Python program so far in this course has only ever used the whiteboard: `balance`, `year`, `grade_values` all vanish the moment the script ends. Week 10 is about the notebook.

Then give the historical mechanical picture, briefly, as *context for why the distinction used to be physically obvious* rather than as a topic in its own right: a hard disk drive stores bits as magnetized spots on a spinning platter, read and written by a head that has to physically move to the right spot (*seek time* — a real, measurable delay); RAM has no moving parts and is read/written electrically, which is why it's so much faster and also why it forgets everything the instant power is cut. Flash storage (what's actually in a modern phone or laptop) has no moving parts either, which is exactly why the old mechanical tell — "the thing that spins is storage, the thing that doesn't is memory" — no longer works for this generation of hardware. The distinction that matters was never "does it spin," it was always "does it survive after the power comes off, or after the program ends" — name that as the actual definition, now that the mechanical shortcut is gone.

Close by connecting to something already true of every program written so far: `atm.py`'s `balance` starts over at whatever the code hard-codes it to, every single run. Ask: what would it take to make the ATM remember a balance from one run to the next? That question is the throughline for the rest of the week.

---

## 2. Filesystems, and Where Files Actually Live (Tuesday, continued)

Name the filesystem as the thing that organizes storage into files and directories — a tree, exactly like the one students have been navigating since week 1 with `pwd`, `ls`, `cd`, `mkdir`. This is not new vocabulary, just a new reason to care about it: a *path* (`week10/balance.txt`, `/Users/name/comp170/week10/balance.txt`) is how a Python program names a specific notebook page inside that tree, the same way `cd` names a specific branch of it. Distinguish absolute paths (start from the root of the tree) from relative paths (start from wherever the program is currently running) — and connect relative paths directly to `pwd`: a relative path only means what you think it means if you know what directory the program considers "here."

Then widen the picture: local vs. network vs. cloud storage.

- **Local**: the notebook is in the room — reading or writing it costs a few electrical signals, effectively instant.
- **Network storage**: the notebook is in a different building, and every read or write is a request sent over a wire (or Wi-Fi) and a response sent back — slower, and it can fail in a new way local storage can't (the connection drops).
- **Cloud storage**: the same idea as network storage, wearing a friendlier name — "the cloud" is not a place without a filesystem, it's someone else's filesystem, reached over a network. Make this concrete: the little sync icons on iCloud Drive or Google Drive files are a *local* shadow copy standing in for a file that may or may not have finished traveling over the network yet — the sync icon is the program's way of showing you which kind of storage you're actually looking at, moment to moment.

Name the payoff of this section directly: everything Python does with `open()` this week only ever talks to *local* storage. Network and cloud storage exist behind the same-looking file interface in other libraries and services, but the seek-time-vs-network-latency distinction from section 1 explains why "just read the file" is a very different promise depending on where the file actually lives.

---

## 3. `os` and `sys`: Python's View of the Filesystem (Wednesday)

Introduce the two standard-library modules that let a program look at its own surroundings rather than only the files it opens by name:

```python
import sys
import os

print(sys.argv)          # the command itself, as a list of strings
print(os.getcwd())       # "here" -- the directory the program is running from
print(os.listdir("."))   # what's in "here"
print(os.path.exists("balance.txt"))  # a yes/no check before trying to open something
```

Tie `sys.argv` back to the CLI-first spine of the whole course: every `python3 something.py` command students have typed since week 1 is itself a list of strings Python can inspect (`sys.argv[0]` is the script name; anything typed after it lands in `sys.argv[1:]`). This is the same command line, seen from inside the program instead of from the terminal prompt.

Use `os.path.exists(...)` as a guard clause students already know the shape of: "check before you leap" (LBYL, named explicitly in week 9) applies directly here — checking whether a file exists *before* trying to open it is the same instinct as checking `amount % 20 == 0` before withdrawing.

---

## 4. Reading and Writing Files (Wednesday, continued)

Introduce `open()`, the three core modes, and the `with` statement as the default way to use all of them:

```python
with open("balance.txt", "w") as file:
    file.write("140\n")

with open("balance.txt", "r") as file:
    saved_balance = file.readline()
    print(f"Starting balance: {saved_balance}")
```

Name what `with` buys for free: a file that's opened has to be closed, or the notebook is left lying open after you walk away — `with` closes it automatically once the indented block ends, even if something inside that block raises an error. Contrast with the version that forgets to close:

```python
file = open("balance.txt", "w")
file.write("140\n")
# forgot file.close() -- the write may not even be saved yet
```

Cover the three modes directly: `"r"` (read; fails if the file doesn't exist), `"w"` (write; creates the file if missing, *erases* it first if it already exists), `"a"` (append; adds to the end without erasing what's there). Read line-by-line with `.readline()` and all-at-once with `.read()`, and show the `for line in file:` pattern as the natural loop over a file's contents — the same enhanced-`for`-loop shape from week 5, now iterating over lines instead of a list.

Close the loop back to week 9's `try`/`except`: opening a file that doesn't exist in `"r"` mode raises `FileNotFoundError`, and that's a `raise` a program can catch exactly like `ValueError`:

```python
try:
    with open("balance.txt", "r") as file:
        saved_balance = file.readline()
except FileNotFoundError:
    print("No saved balance yet -- starting fresh.")
    saved_balance = "0"
```

Name this out loud as the same pattern from week 9, applied to a new kind of failure: a risky operation, wrapped in `try`, with a fallback instead of a crash. Nothing about `try`/`except` itself is new here — only the specific exception type is.

End the week by rewriting a small piece of `atm.py` to persist `balance` to a file at the end of a run and read it back in at the start of the next one — the direct answer to the question section 1 closed on.

---

## Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| Memory vs. storage | Memory holds a running program's state and disappears when it ends; storage holds files and survives after the program (and the power) is gone |
| Filesystem | The tree of directories and files that organizes storage -- the same tree `pwd`/`ls`/`cd` have navigated since week 1 |
| Path (absolute vs. relative) | How a program names a specific file in that tree; a relative path is only meaningful relative to "here" (`os.getcwd()`) |
| Local vs. network vs. cloud storage | Local storage is read/written electrically, near-instantly; network and cloud storage are the same idea over a wire, with latency and failure modes local storage doesn't have |
| `sys.argv` | The command that launched the program, available to the program itself as a list of strings |
| `os.getcwd()` / `os.listdir()` / `os.path.exists()` | Ways for a program to inspect its own surroundings before acting on them |
| `open()` modes: `"r"`, `"w"`, `"a"` | Read (fails if missing), write (erases first), append (adds to the end) |
| `with open(...) as file:` | Guarantees the file is closed when the block ends, even if an error is raised inside it |
| `FileNotFoundError` | A `raise`d error like `ValueError`, catchable with the same `try`/`except` pattern from week 9 |

---

## Reading

| Topic | Source |
|---|---|
| `try`/`except` around file operations (`FileNotFoundError`) | [Errors and Exceptions — docs.python.org](https://docs.python.org/3/tutorial/errors.html) (same reading assigned in weeks 8 and 9) |
| Files, `open()`, reading/writing, `os`/`sys` modules | *placeholder — no Lubanovic chapter or docs.python.org file-I/O link is yet in the comp-170-su26 reading table; flag for instructor to add (Lubanovic's *Introducing Python, 3rd ed.* has a dedicated Files and Directories chapter, and docs.python.org's tutorial has "Reading and Writing Files") |
| Local vs. network vs. cloud storage (conceptual, non-Python) | *placeholder — no existing entry; this is background conceptual material rather than a Python-specific reading, so may not need a course-textbook citation at all* |

---

## Exercises

---
### Exercise 1 — Memory or Storage?

For each of the following, say whether it describes memory or storage, and why:
1. A variable `balance = 140` inside a running Python script.
2. A file named `balance.txt` sitting in the `week10/` folder.
3. The text you typed into `input()` a moment ago, still visible on screen.
4. The same text, after you've called `file.write()` on it and the program has ended.

---
### Exercise 2 — Tracing a Relative Path

Suppose `os.getcwd()` returns `/Users/student/comp170/week10`. For each of the following calls made from that directory, say whether it succeeds or raises `FileNotFoundError`, and if it succeeds, what absolute path it actually reaches:
1. `open("balance.txt", "r")`, assuming `balance.txt` sits directly inside `week10/`.
2. `open("week09/atm.py", "r")`, assuming `atm.py` sits inside the sibling `week09/` folder, not `week10/`.
3. `open("/Users/student/comp170/week09/atm.py", "r")`.

---
### Exercise 3 — Read, Write, or Append?

For each scenario, name the correct mode (`"r"`, `"w"`, or `"a"`) and explain what would go wrong with each of the other two:
1. Saving a bank balance at the end of every run, always replacing whatever was there before.
2. Keeping a running log where every run's result gets added to the bottom, without erasing previous runs.
3. Loading a saved balance back in at the start of a run.

---
### Exercise 4 — Catching a Missing File

Given this code:

```python
with open("scores.txt", "r") as file:
    line = file.readline()
```

1. What happens if `scores.txt` does not exist yet? Name the exact exception type.
2. Rewrite this using `try`/`except` so that a missing file prints `"No scores yet."` and continues, instead of crashing -- following the same shape as week 9's retry-loop pattern.

---
### Exercise 5 — Persisting the ATM's Balance

Sketch (pseudocode or Python) the two missing pieces of `atm.py`: a function that saves the current `balance` to a file when the program ends, and a function that loads it back in when the program starts (falling back to a starting balance of `0` if no file exists yet).

1. Where in `main()` does each function need to be called?
2. What happens the very first time the program ever runs, before any balance file exists?

---

## Topics Deferred to Later Weeks

- Dictionaries — proposed in `week09-plan.md`, not yet taught; still open, now deferred a second time in favor of this week's file I/O pivot
- `find_all_substrings`, 2D nested-loop patterns, slicing, Python's built-in `complex` type, named tuples — all carried forward unchanged from `week09-plan.md`
- Structured file formats (CSV, JSON) as a step up from plain text
- Binary file modes (`"rb"`, `"wb"`) and the text-vs-binary distinction
- `pathlib` as a more modern alternative to `os.path` for path manipulation
- File permissions and what "local" storage means on a multi-user system

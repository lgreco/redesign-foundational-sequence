# COMP 170 — Week 10 Assignment: Solutions
# =========================================
# This file contains annotated solutions for Problem 1 (groceries.py --
# writing a list to a file, one line per item, in write mode) and
# Problem 2 (diary.py -- appending one entry per run to a growing
# file). Problem 3 (reflection on the Week 9 solutions) is answered
# in comments at the bottom, the same way it was in Week 9. Read the
# comments carefully -- they explain not just WHAT the code does, but
# WHY each piece is written the way it is.


# =============================================================================
# PROBLEM 1 — Write a Grocery List to a File
# =============================================================================
#
# The whole point of this problem is the difference between "in the
# file" and "on the screen": write_grocery_list() only ever talks to
# groceries.txt, and print_grocery_list() only ever talks to the
# screen. They're kept as two separate functions on purpose, mirroring
# the two separate steps the assignment describes -- write everything,
# close the file, THEN reopen it and read it back. Nothing is printed
# to the screen while the list is being built; the only proof the file
# worked is reading it back afterward, which is exactly what the
# in-class buffer discussion (July 22) was about: until .close() runs,
# what's been written isn't guaranteed to actually be on disk yet.

print("=" * 60)
print("PROBLEM 1 — Write a Grocery List to a File")
print("=" * 60)


def write_grocery_list():
    """Ask for grocery items until the user types 'done', writing each
    one to groceries.txt.

    Opening in write mode ("w") happens exactly once, before the loop
    starts -- this is what "starts the file fresh" every run means in
    practice. If we instead opened the file inside the loop, every
    single item would wipe out the ones written before it, because
    write mode always starts from an empty page.
    """
    f = open("groceries.txt", "w")
    while True:
        item = input("Enter a grocery item (or 'done' to finish): ")
        # guard clause, of sorts: check whether this input means "stop"
        # BEFORE treating it as a grocery item to write. .strip() drops
        # accidental leading/trailing spaces and .lower() makes the
        # check case-insensitive, so "Done", "DONE", and "done" all
        # end the loop the same way. This has to run before the
        # .write() below, or a literal "done" would end up as a line
        # in groceries.txt.
        if item.strip().lower() == "done":
            break
        # .write() does not add "\n" the way print() does -- if we
        # don't add it ourselves, every item would run together on one
        # single line instead of appearing one per line.
        f.write(item + "\n")
    # nothing written above is guaranteed to be saved to disk until
    # this line runs -- .close() is what flushes the buffer to the
    # actual file.
    f.close()


def print_grocery_list():
    """Reopen groceries.txt in read mode and print every item back,
    one per line, with no extra blank lines in between.
    """
    f = open("groceries.txt", "r")
    print()
    print("Your grocery list:")
    # .readline() returns one line at a time, trailing "\n" included,
    # and returns "" (which is falsy) once the file is exhausted --
    # that emptiness is exactly what ends this while loop, the same
    # pattern SimpleFileOps.py used in class.
    line = f.readline()
    while line:
        # print() adds its own line break. If we printed `line` as-is,
        # its own trailing "\n" plus print()'s newline would put a
        # blank line after every item. .rstrip("\n") removes just that
        # trailing newline, leaving the item's own text untouched.
        print(line.rstrip("\n"))
        line = f.readline()
    f.close()


# =============================================================================
# PROBLEM 2 — A Diary That Remembers
# =============================================================================
#
# The only mechanical difference between this problem and Problem 1 is
# one word: "a" instead of "w" when opening the file to write to it.
# That single letter is the entire reason diary.txt grows across runs
# instead of resetting -- append mode finds the end of whatever is
# already there and starts writing from that point, rather than
# discarding it. Reading the file back afterward works identically to
# Problem 1, because reading doesn't care how the file was written to;
# it just walks through whatever lines currently exist.

print()
print("=" * 60)
print("PROBLEM 2 — A Diary That Remembers")
print("=" * 60)


def add_diary_entry():
    """Ask for one line of text and append it to diary.txt, preserving
    every entry written on previous runs.
    """
    # "a" for append: if diary.txt doesn't exist yet, this creates it
    # (just like "w" would); if it does exist, opening it in append
    # mode does NOT wipe it -- new writes land after the existing
    # content instead of replacing it.
    f = open("diary.txt", "a")
    entry = input("What happened today? ")
    f.write(entry + "\n")
    f.close()


def print_diary():
    """Reopen diary.txt in read mode and print every entry ever
    written, not just the one from this run.
    """
    f = open("diary.txt", "r")
    print("Diary so far:")
    # Same readline loop as print_grocery_list() -- it has no way to
    # know in advance how many entries exist, and doesn't need to: it
    # just keeps asking for the next line until there isn't one.
    line = f.readline()
    while line:
        print(line.rstrip("\n"))
        line = f.readline()
    f.close()


def main():
    write_grocery_list()
    print_grocery_list()
    print()
    add_diary_entry()
    print_diary()


if __name__ == "__main__":
    main()


# =============================================================================
# PROBLEM 3 — Reflection on Week 9 Solutions
# =============================================================================
#
# Q1. Why raise instead of return unchanged?
#
#     raise makes success and failure two structurally different
#     outcomes, not just two different return values to compare. In
#     week09-solutions.py, withdraw() either returns a genuine new
#     balance or never returns at all -- execution stops right at the
#     raise. Because of that, attempt_withdrawal() never has to ask
#     "did the balance I got back actually change, or did something
#     silently fail?" -- if control returns from withdraw() at all,
#     the withdrawal genuinely happened. That's exactly what the
#     try/except around it depends on: except only runs when something
#     inside try actually raised, so the failure is caught by the
#     language itself instead of by the caller remembering to check a
#     return value against what it expected.
#
# Q2. Order of checks, again
#
#     A method-dependent rule can't be evaluated until the method is
#     known to be one of the two the ATM understands. "cash can't
#     include cents" and "cheque must be valid dollars and cents" are
#     two different rules -- checking the amount-shape rule before
#     method would force the code to guess which rule applies to
#     something like method = "bitcoin", or silently apply one of them
#     to a method that isn't even valid. Checking method second (right
#     after the amount > 0 check that doesn't depend on anything) is
#     what makes it safe for the amount-shape check after it to say
#     "cash" or "cheque" with certainty.
#
# Q3. The warning that still isn't an error
#
#     A raise means deposit() refuses to complete the transaction at
#     all -- the caller's try/except catches it and the deposit never
#     happens. The $10,000 case is the opposite: the deposit is
#     completely valid and does go through: IRS reporting is a
#     real-world side effect of a large, legal deposit, not a reason
#     to reject it. Using print() instead of raise keeps that
#     distinction visible directly in the code: every raise in
#     deposit() marks a transaction that stops, and the one print()
#     marks information about a transaction that continues anyway.
#
# Q4. Connecting to this week
#
#     write_grocery_list() checks whether the user's input is "done"
#     BEFORE writing anything to groceries.txt -- that's the same
#     check-before-acting discipline as a guard clause, just without a
#     raise attached to it. Order matters here for the same reason it
#     does in deposit(): the "is this done?" check has to run before
#     the .write() call, because writing first and checking second
#     would put a literal "done" line into the file. There's no
#     try/except in groceries.py or diary.py, but the underlying habit
#     -- decide whether an action is valid before doing it, not after
#     -- is the same one that makes withdraw()'s and deposit()'s guard
#     clauses work.
#
# Q5. Your choice
#
#     Revisiting attempt_deposit() changed how I read its loop
#     condition: "while tries < max_tries and not succeeded" isn't
#     just a counter, it's what stops the loop the moment a deposit
#     actually succeeds instead of wastefully asking again. That's
#     what pushed me toward giving print_grocery_list() and
#     print_diary() the same "stop exactly when there's nothing left"
#     shape, using the while line: pattern instead of trying to count
#     lines ahead of time. Neither function needs to know in advance
#     how many grocery items or diary entries exist -- the empty
#     string .readline() eventually returns is itself the stopping
#     condition, the same way succeeded becoming True is what stops
#     attempt_deposit() from asking a fifth time after the second try
#     already worked.

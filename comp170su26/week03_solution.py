# COMP 170 — Week 3 Assignment: Solutions
# =========================================
# This file contains annotated solutions for all four problems.
# Read the comments carefully — they explain not just WHAT the
# code does, but WHY each piece is written the way it is.


# =============================================================================
# PROBLEM 1 — Predicting String Repetition
# =============================================================================
#
# The * operator on strings means "repeat this string N times."
# It has nothing to do with multiplication of numbers.
#
#   'ha' * 3   →   'hahaha'      (repeat the text 3 times)
#   3 * 5      →   15            (arithmetic; no strings involved)
#
# The integer can go on either side:  3 * 'ab'  and  'ab' * 3  are identical.
#
# Python evaluates * before + (same precedence rules as arithmetic), so in
# a mixed expression like  'Na' * 8 + ' Batman!'  Python first builds the
# long 'NaNaNaNaNaNaNaNa' string, then appends ' Batman!'.

print("=" * 60)
print("PROBLEM 1 — String Repetition")
print("=" * 60)

print('*' * 1)          # one star:  *
print('*' * 5)          # five stars: *****
print('*' * 0)          # zero repetitions → empty string → blank line
print('-' * 20)         # a divider: --------------------
print('ha' * 4)         # hahahaha
print('Na' * 8 + ' Batman!')   # NaNaNaNaNaNaNaNa Batman!
print(3 * 'ab')         # ababab  (integer on the left works too)
print('=' * 10 + ' SCORE ' + '=' * 10)  # ==========  SCORE ==========

# ---- Answers to the reflection questions ----
#
# Q1: What does '*' * 0 produce?
#     An empty string "". Python simply prints nothing (a blank line).
#     This makes sense: repeating anything zero times gives you nothing.
#
# Q2: In '=' * 10 + ' SCORE ' + '=' * 10, what order does Python use?
#     Python evaluates all three * operations first (left to right),
#     producing '==========' , ' SCORE ', and '==========' ,
#     then joins them with + (also left to right).
#     The order does NOT matter here because all the * operations are
#     independent — none of them depend on the result of the others.
#
# Q3: Does  3 * 'ab'  vs  'ab' * 3  ever matter?
#     For the result: never — both give 'ababab'.
#     For readability: putting the string first ('ab' * 3) is the
#     conventional style; most Python programmers write it that way.


# =============================================================================
# PROBLEM 2 — Drawing a Staircase
# =============================================================================
#
# Pseudocode (plain-English description of the algorithm):
#   choose how many steps N
#   for each number i from 1 to N:
#       print i, then a space, then '*' repeated i times
#
# Translating to Python:
#   - range(1, N+1) produces  1, 2, 3, ..., N  (stops BEFORE N+1)
#   - print(i, '*' * i) automatically puts a space between its arguments,
#     which is exactly the space we need between the number and the stars.
#
# Why range(1, N+1) and not range(N)?
#   range(N) gives 0, 1, 2, ..., N-1  (zero-based, misses N)
#   range(1, N+1) gives 1, 2, 3, ..., N  (one-based, matches the row label)

print()
print("=" * 60)
print("PROBLEM 2 — Staircase")
print("=" * 60)

N = 5   # number of steps; change this to try other sizes

for i in range(1, N + 1):      # i goes: 1, 2, 3, 4, 5
    print(i, '*' * i)          # prints "1 *", "2 **", "3 ***", etc.

# Expected output for N = 5:
#   1 *
#   2 **
#   3 ***
#   4 ****
#   5 *****
#
# Try changing N to 10 — the loop handles any size without any other edits.


# =============================================================================
# PROBLEM 3 — Right-Aligned Triangle
# =============================================================================
#
# The shape for N = 5:
#       *        ← row 1: 4 spaces + 1 star
#      **        ← row 2: 3 spaces + 2 stars
#     ***        ← row 3: 2 spaces + 3 stars
#    ****        ← row 4: 1 space  + 4 stars
#   *****        ← row 5: 0 spaces + 5 stars
#
# Pattern in each row i (with N = 5):
#   leading spaces = N - i
#   stars          = i
#
# Why N - i spaces?  When i = 1 (first row), we need N-1 = 4 spaces.
# As i grows, N - i shrinks, so the star block shifts left row by row.
# At i = N, N - i = 0, so the last row has no leading spaces at all.
#
# Key technique: use + to concatenate the two pieces BEFORE printing.
#   ' ' * (N - i)  →  a string of spaces
#   '*' * i        →  a string of stars
#   combined       →  one string; print() shows it with no gap between them
#
# Contrast with Problem 2 where we used  print(i, '*' * i) — that form
# inserts a space automatically between arguments.  Here we want the spaces
# and stars to butt up against each other, so we concatenate with + first.

print()
print("=" * 60)
print("PROBLEM 3 — Right-Aligned Triangle")
print("=" * 60)

N = 5   # height (and width) of the triangle

for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)

# Try N = 8 — the formula still works because it always uses N and i,
# never hard-coded numbers.


# =============================================================================
# PROBLEM 4 — Filled Circle (Challenge)
# =============================================================================
#
# Goal: draw a filled circle that actually looks circular in the terminal.
#
# ---- The math ----
#
# A circle centered at the origin satisfies x² + y² = r².
# Every point where  x² + y² ≤ r²  is *inside* the circle.
#
# For a given row y, the farthest x still inside the circle is:
#   x_max = sqrt(r² - y²)
#
# That row then prints  2·x_max + 1  stars: from -x_max to +x_max.
# The stars are right-centered with leading spaces so the circle
# appears in the middle of the output, not shoved to the left edge.
#
# ---- Why we need discretization ----
#
# The terminal is a grid of characters — positions are always integers.
# sqrt() returns a float like 7.416..., which we must round to the
# nearest integer.  We use  int(value + 0.5)  instead of round()
# to make the rounding direction explicit and predictable.
#
# ---- The aspect-ratio problem ----
#
# A terminal character cell is roughly TWICE as tall as it is wide.
# If we loop y from -r to r (2r+1 rows) at 1 step each, the shape
# looks like a tall oval.
#
# Fix: loop y from -r//2 to r//2 (half as many rows), then multiply
# each y by 2 before plugging it into the formula.  This halves the
# vertical count while keeping the horizontal width the same, making
# the shape look approximately circular on screen.
#
# ---- Reading the loop line by line ----
#
#   for y in range(-r//2, r//2 + 1):
#       y_scaled = y * 2
#       x_max = int(math.sqrt(r*r - y_scaled*y_scaled) + 0.5)
#       print(' ' * (r - x_max) + '*' * (2 * x_max + 1))
#
#   y        — compressed row index; goes from -r//2 to +r//2
#   y_scaled — the "real" y used in the geometry (doubled back up)
#   x_max    — the rightmost column of stars for this row
#   r - x_max — leading spaces needed to center the row
#   2*x_max+1 — total number of stars per row

import math

print()
print("=" * 60)
print("PROBLEM 4 — Filled Circle")
print("=" * 60)

r = 8   # radius; try 5, 10, 12

for y in range(-r // 2, r // 2 + 1):
    y_scaled = y * 2                                     # undo vertical compression
    x_max = int(math.sqrt(r * r - y_scaled * y_scaled) + 0.5)  # half-width in stars
    print(' ' * (r - x_max) + '*' * (2 * x_max + 1))

# Expected output for r = 8 (may vary slightly by terminal font):
#      *******
#   *************
#  ***************
# *****************
# *****************
# *****************
#  ***************
#   *************
#      *******

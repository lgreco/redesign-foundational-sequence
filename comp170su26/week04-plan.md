# COMP 170 — Week 4 Plan

## Continuity from Week 3

Week 3 ended with a strong handle on `for` loops, `range()`, string repetition, and scope. The closing session note flagged explicitly: "Next week: `if` statements." The week 3 assignment included a right-aligned triangle (combining spaces and stars inside a loop) and a filled-circle challenge that introduced `math.sqrt`. Students who completed the challenge used a conditional expression implicitly (`int(x + 0.5)` for rounding). Week 4 makes that decision-making explicit.

---

## 1. Making Decisions: `if`, `elif`, `else`

So far, every program runs the same way no matter what values it encounters. An `if` statement lets a program choose. The concept is simple enough to introduce with a plain English analogy before touching Python:

> If the number is even, print "even." Otherwise, print "odd."

In Python:

```python
n = 7
if n % 2 == 0:
    print("even")
else:
    print("odd")
```

Two things to emphasize:

1. **The condition is a Boolean expression** — it evaluates to either `True` or `False`. The `%` operator returns the remainder, so `n % 2 == 0` asks "is the remainder when dividing by 2 equal to zero?"
2. **Indentation is the structure.** The body of the `if` and the body of the `else` are distinguished by indentation, exactly as the body of a `for` loop is. Consistent indentation is not style — it is syntax.

Introduce `elif` as soon as students have the basic shape:

```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("below C")
```

Walk through it for `score = 85`. Python checks conditions top to bottom and stops at the first `True`. Ask: what would happen if the conditions were reversed (lowest first)?

---

## 2. Boolean Expressions

A Boolean expression is any expression that evaluates to `True` or `False`. The comparison operators produce Boolean values:

| Operator | Meaning |
|---|---|
| `==` | equal to (note: two equals signs, not one) |
| `!=` | not equal to |
| `<`, `>` | less than, greater than |
| `<=`, `>=` | less than or equal, greater than or equal |

Common confusion to address directly: `=` assigns a value; `==` tests for equality. Writing `if n = 5:` is a syntax error in Python (unlike some other languages where it silently assigns and evaluates to `True`).

Compound conditions use `and`, `or`, and `not`:

```python
x = 15
if x > 10 and x < 20:
    print("between 10 and 20")

if x < 0 or x > 100:
    print("out of range")

if not x == 0:
    print("nonzero")
```

Keep the examples grounded in the kinds of values students already know — numbers and strings from the first three weeks.

---

## 3. `if` Inside a Loop

Combining `if` with `for` is where the real power appears. The ASCII art context from week 3 is a natural setting.

**Counting even numbers in a range:**

```python
count = 0
for i in range(10):
    if i % 2 == 0:
        count += 1
print(count)   # 5
```

**Printing only certain items:**

```python
for i in range(1, 16):
    if i % 3 == 0:
        print(i)
```

Ask students to predict the output before running. Then ask: what would change if the condition were `i % 3 != 0`?

**A checkerboard row:**
Connecting to the string/loop work from week 3 — alternate characters based on position parity:

```python
N = 10
row = ""
for i in range(N):
    if i % 2 == 0:
        row += "#"
    else:
        row += "."
print(row)   # #.#.#.#.#.
```

---

## 4. `while` Loops

`for` loops are for iterating over a known sequence. `while` loops are for repeating as long as a condition holds — the number of iterations may not be known in advance.

```python
n = 1
while n < 100:
    n = n * 2
print(n)   # 128
```

Ask: how many times did the loop body run? Have students trace it on paper before running.

A practical use case students can relate to: validating input. The program should keep asking until the user types something acceptable. (Do not implement full input validation this week — just show the pattern conceptually.)

Contrast with `for`:

| `for` | `while` |
|---|---|
| iterate over a sequence | repeat while a condition is true |
| number of iterations usually known | number of iterations may be unknown |
| `range()` is the common driver | a Boolean condition is the driver |

Introduce `break` briefly — a way to exit a `while` loop early — but do not linger. The goal this week is the basic `while` pattern.

---

## 5. Revisiting ASCII Art with Conditionals

Return to the triangle and staircase from week 3, now using `if` to add variation. A diamond is a good target because it combines the growing-then-shrinking pattern students can work out by hand:

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

For a diamond of half-width `r = 4`:
- Rows above the midpoint: spaces decrease, stars increase
- Rows below the midpoint: spaces increase, stars decrease

The pattern can be expressed with a single `if`/`else` inside the loop, or with two loops (one for the top half, one for the bottom). Let students try both. The two-loop version is simpler to understand; the single-loop version with `if`/`else` is a good challenge.

---

## 6. Concepts to Name This Week

| Concept | One-line definition |
|---|---|
| Boolean expression | An expression that evaluates to `True` or `False` |
| `if` / `elif` / `else` | Execute a block only when a condition is true |
| Comparison operators | `==`, `!=`, `<`, `>`, `<=`, `>=` — produce Boolean values |
| `and`, `or`, `not` | Combine or negate Boolean expressions |
| `while` loop | Repeat a block as long as a condition remains true |
| `break` | Exit a loop immediately |

---

## Reading

| Topic | Source |
|---|---|
| `if` / `elif` / `else` | [More Control Flow — docs.python.org](https://docs.python.org/3/tutorial/controlflow.html#if-statements) · [Choose with if — Lubanovic ch. 5](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch05.html) |
| Boolean operations (`and`, `or`, `not`) | [Boolean Operations — docs.python.org](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) |
| Comparison operators | [Comparisons — docs.python.org](https://docs.python.org/3/library/stdtypes.html#comparisons) |
| `while` loops and `break` | [while — docs.python.org](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) · [Loop with while and for — Lubanovic ch. 7](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch07.html) |
| `break` and `continue` | [break and continue — docs.python.org](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) |
| Collatz conjecture (Exercise 4 background) | [Collatz conjecture — Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture) |

---

## Exercises

---
### Exercise 1 — Predict Before Running

For each snippet, write the predicted output as a comment before running.

```python
x = 12
if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")
```

```python
for i in range(1, 6):
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")
```

Questions:
1. In the second snippet, `range(1, 6)` gives 1 through 5. Which values trigger the `even` branch?
2. What would change if `i % 2 == 0` were replaced with `i % 2 != 0`?

---
### Exercise 2 — FizzBuzz

Print the numbers 1 through 30. But:
- If the number is divisible by 3, print `Fizz` instead.
- If the number is divisible by 5, print `Buzz` instead.
- If divisible by both 3 and 5, print `FizzBuzz` instead.

Questions:
1. The "divisible by both" case must come first in your `if`/`elif` chain. Why? What happens if you put it last?
2. How many times does `Fizz` appear in the output? How many times does `Buzz`? Work it out before running.

---
### Exercise 3 — ASCII Art with a Condition

Print a diamond shape for `r = 4` (9 rows total: 4 above midpoint, midpoint, 4 below). Each row has `2 * stars - 1` stars and enough leading spaces to center them in a field of width `2 * r + 1`.

Questions:
1. Write out the number of stars and spaces for each row on paper before writing the code.
2. Did you use two loops (one for top half, one for bottom) or one loop with an `if`/`else`? Which approach was easier to reason about?

---
### Exercise 4 — `while` Loop Tracing

```python
n = 100
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1
print(steps)
```

This is the **Collatz sequence**. No one has proved it always terminates, but it does for every starting value tried so far.

Questions:
1. Trace the first five values of `n` by hand.
2. Run the program. How many steps does it take for `n = 100`? For `n = 27`?
3. Is there a `for` loop version of this program? Why or why not?

---

## Topics Deferred to Later Weeks

- Nested `for` loops (two-dimensional patterns)
- `while` with user input (`input()`)
- `break` and `continue` in depth
- Defining methods with `def` — the next major topic after conditionals and loops are solid

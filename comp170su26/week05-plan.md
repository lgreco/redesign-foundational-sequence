# Week 05 Plan — Methods, Strings, Lists, Loops, and If

## Where We Are

Students can now:

- Declare and index a list
- Loop over a list with `for i in range(len(...))`
- Track a running value (sum, max, count) inside a loop
- Use `if` to branch on a condition
- Work with strings using `*`, `+`, `ord()`, `chr()`, and indexing

Week 05 introduces **methods** — functions that belong to an object and are called
with dot notation (`object.method()`). The goal is not to enumerate all available
methods; it is to show that methods are just a different calling syntax for
operations that feel familiar, and that a handful of well-chosen string and list
methods unlock a whole new class of problems.

---

## The Unifying Problem

**Given a sentence, extract all "long" words — words longer than $N$ characters —
and print them in lowercase, one per line.**

Example input:

```python
sentence = "The relentless summer heat in Chicago made even the sidewalks shimmer"
```

Example output (for $N = 5$):

```
relentless
summer
chicago
sidewalks
shimmer
```

This one problem drives the entire week. Each method introduced is a step in
solving it:

| Step | What we need | Method |
|------|-------------|--------|
| 1 | Break the sentence into individual words | `str.split()` |
| 2 | Convert each word to lowercase | `str.lower()` |
| 3 | Keep only the long ones | `if len(word) > N` inside a loop |
| 4 | Collect the results | `list.append()` |

The four methods span both data types students know — string methods and list
methods — and every step uses at least one of: strings, lists, for loops, if.

---

## Key Concepts to Introduce

### 1. What Is a Method?

Students have called functions like `len()`, `print()`, and `range()`.
A method is a function that lives *inside* an object:

```python
# function call — the object is an argument
length = len(sentence)

# method call — the object comes first, before the dot
words = sentence.split()
```

The dot notation is the only syntax difference. Conceptually: the string `sentence`
*knows how* to split itself; calling `.split()` asks it to do so.

Contrast two string methods to build the intuition quickly:

```python
s = "Hello, World"
print(s.upper())    # "HELLO, WORLD"
print(s.lower())    # "hello, world"
```

### 2. `str.split()` — the Bridge from String to List

`.split()` with no arguments splits on any whitespace and returns a list of words.
This is the conceptual bridge students need: a single string becomes a list, and
everything they learned in Week 04 about looping over lists now applies to words.

```python
sentence = "the quick brown fox"
words = sentence.split()
# words is now ['the', 'quick', 'brown', 'fox']
print(len(words))   # 4
print(words[0])     # 'the'
```

### 3. `str.lower()` and `str.upper()` — Per-Element Methods in a Loop

Once you have a list of words, you can call a method on each element inside a loop.
This is the same loop pattern from Week 04, now with a method call in the body:

```python
for i in range(len(words)):
    print(words[i].lower())
```

### 4. `list.append()` — Building a Result List Incrementally

The counting loop from Week 04 accumulated a *number*. The same pattern can
accumulate *items* into a list by calling `.append()` instead of adding 1:

```python
long_words = []                      # start with an empty list

for i in range(len(words)):
    if len(words[i]) > 4:
        long_words.append(words[i])  # add this word to the result
```

This is a filter pattern — the list version of the counting loop — and it
completes the bridge: string → list of words → filtered list of results.

---

## Suggested Session Arc (Three Sessions)

### Session 1 — What Is a Method? String Methods.

- Motivation: we know `len(s)`, but the string has its own vocabulary too
- Demo `.upper()`, `.lower()`, `.replace()`, `.strip()` interactively
- Show that method calls can be chained: `s.strip().lower()`
- Introduce `.split()` as the day's main event; run it on several sentences
- End with: "now that we have a *list* of words, what can we do?"

**Live coding sketch:**

```python
headline = "  Scientists Discover Water on Mars  "
print(headline.strip())           # remove leading/trailing spaces
print(headline.strip().lower())   # strip, then lowercase
words = headline.strip().lower().split()
print(words)
print(len(words))
```

### Session 2 — list.append() and the Filter Pattern

- Recap: `.split()` gives us a list; now we loop over it
- Introduce the empty list: `result = []`
- Show `.append()` as "add one item to the end of the list"
- Build the long-word filter step by step, writing pseudocode first:

```
start with an empty result list
for each word in the sentence:
    if the word is long enough:
        add it to the result list
print the result list
```

- Translate pseudocode to code together
- Run it, modify the threshold $N$, discuss what changes

**Live coding sketch:**

```python
sentence = "The relentless summer heat in Chicago made even the sidewalks shimmer"
words = sentence.split()
long_words = []

for i in range(len(words)):
    if len(words[i]) > 5:
        long_words.append(words[i].lower())

print(long_words)
print("Found:", len(long_words), "long words")
```

### Session 3 — Combining Patterns; Introducing `for word in words`

- Show the direct iteration style: `for word in words` vs. `for i in range(len(words))`
  - Both work; the direct style is cleaner when you don't need the index
  - Reinforce: the index style is still needed when you want position information
- Solve one or two variations of the same problem to show that the pattern is reusable:
  - Count words that start with a vowel
  - Collect words that contain the letter 'e'
- Preview: next week we will write our own functions (using `def`) to package these patterns

**Live coding sketch (direct iteration):**

```python
sentence = "An elephant ate an entire apple and an orange"
words = sentence.split()
vowels = "aeiou"
vowel_words = []

for word in words:
    if word[0].lower() in vowels:
        vowel_words.append(word)

print(vowel_words)
```

---

## Concepts Explicitly Reinforced

| Concept | Where it appears |
|---------|-----------------|
| Strings | `sentence`, `word`, `.split()`, `.lower()`, `word[0]` |
| Lists | result of `.split()`, `long_words = []`, `.append()` |
| `for` loop | iterating over word list in every example |
| `if` statement | the filter condition (`len(word) > N`, `word[0] in vowels`) |
| `len()` | measuring words and lists |

---

## Methods Summary for Students

| Method | Called on | What it does | Returns |
|--------|-----------|-------------|---------|
| `s.split()` | string | splits on whitespace → word list | `list` |
| `s.lower()` | string | converts all characters to lowercase | `str` |
| `s.upper()` | string | converts all characters to uppercase | `str` |
| `s.strip()` | string | removes leading and trailing whitespace | `str` |
| `lst.append(x)` | list | adds item `x` to the end of the list | `None` |

---

## Assignment Preview

Four problems, all driven by the same data:

```python
sentence = "A long time ago in a galaxy far far away"
```

1. **Split and index** — call `.split()`, then print the first word, last word,
   and total word count. *(Reinforces: split, indexing, len)*

2. **Uppercase filter** — build a list of words longer than 3 characters,
   printed in uppercase. *(Reinforces: loop, if, append, upper)*

3. **Vowel counter** — count how many words begin with a vowel.
   *(Reinforces: loop, if, string indexing, lower)*

4. *(Challenge)* **Frequency** — count how many times a given short word
   (e.g., `"far"`, `"a"`) appears in the sentence without using `.count()` —
   instead, write the counting loop from scratch.
   *(Reinforces: all patterns; resists the shortcut)*

---

## What This Week Does Not Cover (Yet)

- Defining functions with `def` — next week
- Nested loops
- List slicing
- String `.count()`, `.find()`, `.index()` — can be mentioned briefly but
  not the focus; students should build the counting loop by hand first
- `while` loops

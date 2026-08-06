# COMP 170 — Fall 2026 — Lesson Plan: Reading Code Before Writing It

## Why This, Why Now

Every prior offering (see `../comp170su26/week01_outline.md`) opens with writing: terminal, Vim, `print("Hello, World!")`, run it. That order made sense when producing correct syntax was the scarce skill. It no longer is — AI tools generate syntactically correct code instantly. What's scarce now is the ability to look at code (yours, a classmate's, or a model's) and know what it actually does before you run it, trust it, or hand it in. Fall 2026 opens with that skill instead, deliberately, before students write a single line of Python.

The core idea: a program is a literal set of instructions performed on data, in order, with no common sense filled in. A single changed instruction — not a changed goal, not a changed ingredient — can produce a completely different result. Students need to feel that before they start writing, so that when they read code (their own, a classmate's, or an AI's) later in the term, close reading is already a habit, not a new skill bolted on.

## Placement (open decision)

This doesn't require any Python syntax, so it can run before `week01_outline.md` Day 1's terminal demo — either as a short Day 0 warm-up, or as the first 15–20 minutes of Day 1 before "The Terminal Is a Tool, Not Magic." Recommend the latter: keep it inside Day 1 so the recipe-to-code bridge (Part 2 below) lands in the same session as the first real `print()` demo, rather than a full day earlier. Flag for a decision once the rest of Week 1 is repaced around this addition.

---

## 1. Warm-Up: Two Recipes, One Instruction (No Code Yet)

Put both recipes on the board or screen side by side. Do not mention programming yet.

**Ingredients (identical for both):** 3 eggs, 1 tsp butter, pinch of salt.

**Recipe A — Scrambled Eggs**
1. Beat eggs with salt.
2. Melt butter in a pan over medium-low heat.
3. Pour in eggs.
4. **Stir continuously, scraping the bottom, until soft curds form.**
5. Remove from heat while still glossy.

**Recipe B — French Omelette**
1. Beat eggs with salt.
2. Melt butter in a pan over medium-low heat.
3. Pour in eggs.
4. **Let sit undisturbed for 10 seconds, then push the cooked edges toward the center, tilting the pan so raw egg flows to the edge. Do not stir continuously.**
5. When just set, fold in thirds and slide onto a plate.

**Ask students, in order:**
1. What's identical between these two recipes? (List it out loud: ingredients, pan, heat, number of steps.)
2. What's the one thing that's different?
3. Why does that one difference produce two completely different dishes — different texture, different presentation, different name on a menu?

**Land this point explicitly:** a recipe followed literally, by someone who fills in no gaps with judgment or experience, will always produce the same dish from the same recipe. A computer is exactly that literal a cook. It has no judgment to fill gaps with — it runs the instructions exactly as written, in order.

---

## 2. Bridging: From Recipes to Programs

Build this mapping with the class, don't just present it:

| Recipe | Program |
|---|---|
| Ingredients | Data / values |
| Numbered steps | Instructions / statements |
| The order the steps are performed in | Execution order |
| The dish that comes out | The output / behavior |
| A cook who follows the recipe literally | The computer / interpreter |

Name the concept explicitly: **a program is a sequence of instructions, executed in order, on some data, producing an output.** Reading code well means running that sequence in your head — like reading a recipe and picturing the dish — before you ever run it on a machine.

---

## 3. First Code-Reading Pair

Now switch to actual Python — the same "one instruction changes everything" structure, applied to code. No syntax lecture yet; treat this the same way the recipes were treated: read it, predict, then check.

**Version A**
```python
name = "Ada"
print("Hello,", name)
```

**Version B**
```python
name = "Ada"
print("Hello, name")
```

**Ask before running either one:**
1. What's identical between these two programs?
2. What's the one thing that's different?
3. Predict: what does each one print?

Run both. Confirm:
- Version A prints `Hello, Ada`
- Version B prints `Hello, name`

**Discussion — let students arrive at this, don't just tell them:** In the recipe, the one changed instruction was *stir continuously* vs. *let sit undisturbed*. Here, the one changed instruction is whether `name` sits **inside** the quotation marks or **outside** them, separated by a comma. Ask: based only on what just happened, what do quotation marks seem to mean? What does it seem to mean when something is *not* in quotes? Students should be able to propose, in their own words, something close to "quotes mean the text is used exactly as typed; no quotes means Python looks up a value stored under that name" — before that idea is ever formally defined as a string literal vs. a variable reference.

**Why this pair, specifically:** it isn't a contrived gotcha — forgetting to take a variable name out of quotes (or forgetting to put literal text into quotes) is one of the most common mistakes beginners make in the first two weeks of any Python course. Using it here means the first bug students learn to *read* is one they will personally *write* within days, and they'll recognize it when it happens instead of being surprised by it.

---

## 4. Concepts to Name This Session

| Concept | One-line definition |
|---|---|
| Instruction | A single step a program tells the computer to perform |
| Sequence | Instructions run in the order they're written, top to bottom |
| Literal (string) | Text used exactly as written, marked by quotation marks |
| Name / variable reference | A word that stands for a stored value, not the value itself |
| Reading code | Predicting what a program does before running it |

Do not formally define "variable" or "string" yet if `week01_outline.md`'s existing Day 4 material still covers that — this session's job is the *habit* of close reading, not the vocabulary. Let the vocabulary catch up when Day 4's `name = "Leo"` example arrives.

---

## Reading

| Topic | Source |
|---|---|
| What Python is, running a first program | [Introducing Python, 3rd Ed. — Ch. 1: Introduction](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/) |
| Strings as literal text | [An Informal Introduction: Text — docs.python.org](https://docs.python.org/3/tutorial/introduction.html#text) |

No new URLs invented — both pulled from `../../comp-170-su26/CLAUDE.md`'s Reading Materials table.

---

## 5. Recipe Pair Bank for Later in the Term

The eggs/omelette pair above is one instance of a general pattern: hold everything constant and change exactly one thing. Different pairs isolate different *kinds* of change, and each kind maps to a different category of code difference. Each pair below is placed at the week in `../comp170su26/week99/15-week-outline.md` where the matching code concept is actually taught — same format as Part 1: present both recipes, ask what's identical / what's different / predict the result, then name the code concept explicitly. (Placement assumes Fall 2026 follows that 15-week pacing — confirm before locking these in; see Open Questions.)

### Week 2 — Data, Types: Soft-Boiled Egg vs. Hard-Boiled Egg
*Same everything; one number changes.*

Same egg, same pot, same water, same steps: bring water to a boil, lower the egg in gently, boil, then transfer to ice water.
- **Recipe A (soft-boiled):** boil for **6 minutes**.
- **Recipe B (hard-boiled):** boil for **12 minutes**.

**Maps to:** a changed numeric literal or argument. Same procedure, one number swapped in, a completely different result (runny yolk vs. fully set). This is the cleanest pair for isolating "a number is the entire difference" — good contrast with the quotes pair, which isolates a *syntax structure* rather than a value.

### Week 3 — Separation of Concerns: Béchamel vs. Velouté
*Same technique; one input source changes.*

Same roux (2 tbsp butter melted with 2 tbsp flour, cooked 1–2 minutes), same method: whisk in the liquid gradually, simmer while whisking until thickened.
- **Recipe A (béchamel):** the liquid is **2 cups warm milk**.
- **Recipe B (velouté):** the liquid is **2 cups warm stock**.

**Maps to:** the same processing logic run against different data — the same shape as `interest.py` run with a different rate, or a method run against a different input file. The "algorithm" (roux + thicken) is identical; only the data fed into it changes, and that's enough to land in a different sauce family entirely.

### Week 11 — Default Parameter Values: Pancakes vs. Crêpes
*Same base; one ingredient present or absent.*

Same batter base (1 cup flour, 2 eggs, 3/4 cup milk, pinch of salt).
- **Recipe A (pancakes):** whisk in **1 tsp baking powder**. Cook in dollops until bubbles form, flip.
- **Recipe B (crêpes):** **omit the baking powder**; thin the batter with an extra 1/4 cup milk. Cook in a thin layer, tilting the pan to spread it, flip once.

**Maps to:** a parameter left at its default vs. supplied — one optional ingredient, present or absent, changes the entire downstream shape of the result. Direct lead-in to `def make_batter(leavening=True):`-style default-parameter thinking, which is exactly what this week introduces.

### Week 12 — `while` / Infinite Loops: Whipped Cream vs. Butter
*Same ingredient, same instruction; only the stopping point changes.*

One ingredient (1 cup heavy cream), one instruction (whip it). Nothing else differs.
- **Recipe A (whipped cream):** whip until **soft peaks form** (cream holds a shape but the tip droops). Stop there.
- **Recipe B (butter):** keep whipping **past** soft peaks, past stiff peaks, until the mixture suddenly turns grainy and separates into solid fat and buttermilk. Stop only then.

**Maps to:** a `while` loop's exit condition. The loop body doesn't change at all ("keep whipping") — only the condition that decides when to stop. This is the cleanest recipe form of "loop until X" vs. "loop one stage past X," and a natural lead-in to infinite-loop bugs, where the stopping condition is wrong or missing.

### Week 13 — Interval / Range Validation: Caramel vs. Burnt Sugar
*Same everything; cooked a little too far past the target.*

Same sugar, same pan, same heat: melt sugar over medium heat, swirling (not stirring).
- **Recipe A (caramel):** remove from heat at a deep amber color, roughly 340–350°F.
- **Recipe B (burnt sugar):** keep cooking past that point — even 20–30 seconds longer, past ~370°F — and it turns dark, bitter, and unusable.

**Maps to:** a boundary crossed by a small margin — the same shape as an off-by-one bug, or a range check using `<=` where `<` was meant. Unlike the other pairs, this one isn't two valid dishes — it's correct vs. broken, which is closer to what real debugging feels like. Pairs naturally with this week's interval-membership math thread (checking a value against $[1901, 2025]$ is the same shape as checking a temperature against a safe range).

---

## Open Questions for the Instructor

- **Placement:** fold into Day 1 (recommended above) or run as a standalone Day 0? Affects whether `week01_outline.md` needs to be rewritten or just extended.
- **Confirm the pacing assumption:** Part 5's placements assume Fall 2026 follows `week99/15-week-outline.md` week-for-week. If Fall 2026's actual pacing diverges, the five pairs need to be re-mapped to wherever their matching concept (numeric literals, same-logic-different-data, default parameters, `while` loops, range validation) actually lands.
- **Assessment tie-in:** if "predict before running" becomes a running habit, consider whether it belongs as a standing instruction on assignments from week 1 onward (a one-line "before you run this, write what you expect to see" prompt), rather than a one-time warm-up exercise.

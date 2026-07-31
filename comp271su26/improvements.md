# Improvements -- End of Term Reflection

Observations from working across the full COMP 271 repository set this term: the student-facing repo, this private planning folder, and the `proposal_158_159/` redesign work. Two parts, as asked: the course itself, and how these Claude sessions went.

---

## 1. The Course

### No sorting algorithm was ever implemented

Across eleven weeks of arrays, linked lists, stacks, queues, graphs, and hash tables, students never wrote a sort -- not even a simple $\mathcal O(n^2)$ one. This is a real gap for a second data-structures course: sorting is one of the most natural vehicles for teaching nested-loop complexity analysis, and the course already built the exact scaffolding a sort needs (an array with `get`/`swap`-equivalent access, a firm grasp of $\mathcal O(n)$ versus $\mathcal O(n^2)$ from week 6 onward). `proposal_158_159/topics-141-163-170.md`'s gap analysis names Big-O as "the most directly prerequisite topic for COMP 271 and 272," but never separately flags sorting as its own prerequisite gap -- worth adding to that document, since COMP 272 (non-linear structures in Java) is likely to assume at least one sort has been implemented by hand before it arrives.

### Trees never appeared, despite the node vocabulary being ready by week 6

By week 6, students had built a node object with a payload and a pointer to another node of the same class. That is the entire prerequisite for a binary search tree -- a node just needs a second pointer field. The course never took that step; every linked structure this term was linear (train line, doubly linked list, hash-table chain). Given that COMP 272 is described in `redesign-foundational-sequence/CLAUDE.md` as covering "non-linear data structures," this is the single largest structural gap between where COMP 271 ends and where COMP 272 begins. Even a two-session preview -- a `TreeNode` with `left`/`right` instead of `next`, and one traversal -- would close a meaningful part of that gap without displacing anything else this term covered.

### Testing was demonstrated in the verification sections but never taught as a habit

Every assignment this term ships with expected-output comments students check by eye (`# expected: True`), but the course never introduced `assert` or `unittest` the way COMP 170 dedicated its own week 8 to three levels of testing. `comp170su26/improvements.md`'s own end-of-term reflection flagged the same absence for COMP 170 and recommended seeding the habit early rather than teaching it as a single dense week; that same fix would help COMP 271 for the identical reason -- several of this term's bugs (the resize `int()`/`math.ceil()` bug in week 3, the infinite-loop `cursor.get_next()` bug in week 6) were exactly the kind of failure a one-line `assert` would have caught immediately, before the bug reached a live class demo.

### The reading table is missing a citation the final assignment needed

Writing `week99/last_assignment.md` needed a citation for hashing and for Python's `dict`, and `../../comp-271-su26/CLAUDE.md`'s reading tables have no Lubanovic chapter for either -- despite hashing being an entire week (week 11) of live class content. This is the same pattern `comp170su26/improvements.md` named for COMP 170: "the reading table gets updated when an assignment needs a citation, not when a topic is first taught in class." The fix suggested there applies here too -- add the reading-table row the same day a topic is introduced in class, not the day an assignment needs to cite it. This session added the row as part of Step 4 below, marked as a new citation and cross-checked against COMP 170's own already-verified table for the same book, rather than being invented outright -- but a two-minute check against the physical or PDF text (`blubanovic08.pdf`, `blubanovic11.pdf` in this folder do not cover Chapter 9) is still worth doing before the reading table is trusted for a future term.

### The student-facing repo has no content table at all

`../../comp-170-su26/CLAUDE.md` maintains a week-by-week "Current content" table listing every file and topic per week. `../../comp-271-su26/CLAUDE.md` has never had one -- it documents the Mississippi progression, the assignment/submission conventions, and the reading tables, but nothing that inventories what each `week01/` through `week11/` directory actually contains. This session added that table as part of Step 4 below, reconstructed from the actual repository contents rather than from any prior draft, since none existed to check against.

### A few end-of-term hygiene items

- `week07/` contains stray build artifacts (`Node.class`, `Node.java`, `backup.assignment.md`) alongside the Python assignment materials -- likely a scratch comparison against the Java equivalent COMP 272 will use, but worth a deliberate keep-or-remove decision before the repo is handed to a future term.
- `week11/` never received a formal `week11-assignment.md` -- the synchronous term ended mid-topic, on hashing, with `hash_strings.py` and `HotelAlphabetical.py` left as in-class scratch material rather than a posted assignment. `week99/last_assignment.md` and its companion `simple_hash_assignment.py` fill that gap now, using those two scratch files as the direct basis for the final assignment's hash-function discussion. For next term, worth deciding up front whether the last live week gets a real posted assignment or is explicitly framed as a capstone demo with no standalone submission, the same open question `comp170su26/improvements.md` raised for COMP 170's own week 11.
- Several `__pycache__/` directories (`week02/`, `week05/`, `week06/`, `week07/`) are present in the working tree; confirm `.gitignore` is actually excluding them from commits rather than relying on them simply never having been staged.

---

## 2. These Claude Sessions

### The private folder's plan files and the student repo's session notes overlap heavily -- and that overlap is a feature, not a redundancy

Nearly every `weekNN-plan.md` in this folder maps closely onto the `weekNN-assignment.md` and dated class notes that ended up in the student-facing repo, which made cross-checking fast: reading the plan for a week and then the actual session notes for that week reliably surfaced the same design decisions from two angles, and disagreements between the two (where the plan proposed something class didn't end up doing) were a useful signal of where the live class deviated from the written plan. Worth explicitly noting as a reason to keep writing both documents rather than treating one as redundant with the other.

### CLAUDE.md conventions did most of the work, the same way they did for COMP 170

Matching assignment structure, citing only established reading-table links, distinguishing "method" (this private folder) from the actually-correct mixed method/function usage already present in the student repo (COMP 271's OOP-heavy content genuinely uses "method" for class methods and "function" for the rare standalone one, like `pasta_recipe()` in week 1 -- so no override was needed there, unlike a first pass might assume), and following the exact "How to Submit" / "How Your Work Is Evaluated" templates verbatim -- all of that came directly from `../../comp-271-su26/CLAUDE.md` and `redesign-foundational-sequence/CLAUDE.md`, not from guessing. The `homework_design.md` operational prompt in this folder, in particular, made writing `simple_hash_assignment.py`'s stub comments and `last_assignment.md`'s "Contract" sections fast, because it specifies the exact structure (one return statement, delegation notes, verification with expected output) an assignment in this course should have, independent of which week it is.

### The Output section of the end-of-term prompt undercounted its own file list

`end-of-term-prompt.md`'s Output section says "Five new files" but lists only four paths. Given this repo's established convention that a `weekNN-assignment.md` ships with a companion `.py` stub (stated explicitly in `../../comp-271-su26/CLAUDE.md`'s Assignments section), the most likely intended fifth file is the `SimpleHash` stub itself -- `simple_hash_assignment.py` -- which this session added at `../../comp-271-su26/week99/simple_hash_assignment.py` alongside `last_assignment.md`. That inference is flagged here rather than treated as certain; worth a quick confirmation from the instructor that a companion stub was the intended fifth file, and not, say, a second reflection document or an additional edited file this session missed.

### Where a citation had to be inferred rather than verified

Two citations in `week99/15-week-outline.md` are flagged inline as needing instructor confirmation: the pigeonhole principle / hash function citation for the new Week 14 (no established source in `../../comp-271-su26/CLAUDE.md`'s tables covers it), and the Lubanovic Chapter 9 "Dictionaries and Sets" citation for the new Week 15, which is a new citation for this repo's table even though the same chapter number is already verified in `comp170su26/week99/15-week-outline.md` for the same book. Both are marked as placeholders in the outline itself, consistent with this repo's standing rule against inventing URLs or page numbers -- worth a direct check against the physical book or a PDF excerpt before either citation is trusted for a future term's assignment.

### Naming the exact file that already contains the hard thinking saves real time

The single most efficient part of this session was discovering `homework_design.md` and `proposal_158_159/topics-141-163-170.md` already sitting in this folder, unprompted -- the first gave a ready-made template for the `SimpleHash` assignment's stub comments and Part structure, and the second had already done the downstream-gap analysis (sorting, trees, testing) this reflection's Section 1 leans on, rather than requiring it to be reconstructed from scratch. The same lesson `comp170su26/improvements.md` drew from its own session: when a request (or, in this case, the repository itself) points at the file that already did the hard thinking, the output is noticeably better and arrives with less back-and-forth than when that file has to be discovered by trial and error.

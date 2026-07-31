# COMP 271 -- A 15-Week Outline of the Same Material

This is not a new curriculum. It is the actual Summer 2026 COMP 271 -- the same arc from a fixed-capacity array wrapped in a first class, through linked structures, stacks and queues, recursion, graphs, file-backed structures, and hashing -- repaced from 11 compressed weeks into a standard 15-week semester. No programming topic here is beyond what students in `../../comp-271-su26/` actually learned; the extra four weeks buy breathing room on the densest stretches, and every week now carries a small linux/system thread and a small math thread alongside the programming, instead of those threads showing up only where they happened to fit in the original 11 weeks.

**Reading legend:**
- **Lubanovic** -- Bill Lubanovic, *Introducing Python*, 3rd ed. Chapter numbers match the citations already established in `../../comp-271-su26/CLAUDE.md`'s Reading Materials tables; a chapter cited there for the first time in this document is marked *(new citation)*.
- **docs.python.org** -- the official Python tutorial and library reference, cited exactly as it already appears in `../../comp-271-su26/CLAUDE.md`.
- **TLCL** -- William Shotts, *The Linux Command Line*, 6th ed. (linuxcommand.org, free) -- the same source already in the student-facing Shell and Editor Resources table, used here for the weekly linux/system thread beyond what that table's terminal/Vim links already cover.
- **notes** -- original course material (this repository, or a new in-class handout), used where no single textbook chapter or docs.python.org page covers the idea cleanly -- the same convention `comp170su26/week99/15-week-outline.md` uses.
- Where a citation is not yet confirmed against a source already in `../../comp-271-su26/CLAUDE.md`, it is marked *(placeholder -- flag for instructor)*, per this repo's standing rule against inventing links or chapter numbers.

A coverage map at the end shows exactly which original week each new week descends from.

---

## Week 1 -- Separating Data from Behavior, Logic from I/O
*(= original Week 1)*

- **Linux/System:** `pwd`, `ls`, `cd`, and vim fluency review -- COMP 271 assumes COMP 170's terminal habits, so week 1 is a quick fluency check (`vimtutor`, opening/editing/closing without hesitation) rather than a first introduction.
- **Programming:** the Mississippi progression (`mississippi.py` -> `block_letters.py` -> `mississippi_horizontal.py`) as a concrete demonstration that letter shapes stored as data (a list of strings) can be printed horizontally, where letter shapes baked into `print()` calls cannot; `pasta.py` as a counter-example refactored into `get_guests()` / `pasta_recipe()` / `display_recipe()` / `main()`.
- **Math:** none beyond the arithmetic inside `pasta_recipe()` -- this week's "math" is really a design idea (a pure function has no side effects) more than a numeric one.
- **Reading:** Shell and Editor Resources table (linuxcommand.org, OpenVim, `vimtutor`) in `../../comp-271-su26/CLAUDE.md`.

---

## Week 2 -- Arrays, Objects, and the First Class
*(= original Week 2)*

- **Linux/System:** `du -h` on a directory as a hands-on way to see that files -- like arrays -- occupy a fixed, measurable amount of space, a physical parallel to "an array is a contiguous block of memory."
- **Programming:** true arrays (fixed size, single type) versus Python's dynamic list; classes as blueprints and objects as instances; `__init__`, `self`, and the first `DynamicArray` with four sentinel `-1` slots and `add_zip_code()`.
- **Math:** the sentinel pattern as a simple case of a piecewise-defined rule -- "this slot's value is $-1$ if empty, otherwise the stored item" -- a first, informal encounter with a function defined by cases, which will reappear formally in week 11's hash function.
- **Reading:** Lubanovic Ch. 8 (Lists), Ch. 11 (Objects and classes); docs.python.org -- Classes (full chapter), A First Look at Classes, Class and Instance Variables.

---

## Week 3 -- Resizing and Magic Numbers
*(= original Week 3, part 1)*

- **Linux/System:** `history | grep` as a first taste of searching accumulated state for a pattern -- the same "look for a match" idea `resize()`'s copy loop will formalize into code.
- **Programming:** `resize()`'s three steps (allocate double, copy, replace); naming the **magic number** code smell and replacing bare literals with `DEFAULT_CAPACITY` and `RESIZE_BY`; the move from a procedural version needing `global` to a class-based version using `self`.
- **Math:** doubling as a geometric sequence -- capacity after $k$ resizes is $c_0 \cdot 2^k$ -- and why doubling keeps the *amortized* cost of `add()` low even though any single resize costs $\mathcal O(n)$ (the full formal amortized-analysis argument is out of scope; the intuition that "expensive operations get rarer as the array grows" is the target here).
- **Reading:** docs.python.org -- Modules (full chapter), Mathematics in the standard library.

---

## Week 4 -- Debugging a Resize Bug, and Encapsulation
*(= original Week 3, part 2)*

- **Linux/System:** `python3 -i` (interactive mode after running a script) as a lightweight debugger -- inspect `self._capacity` and `self._resize_by` directly after a crash, the same kind of interactive check that led to diagnosing `int(3 * 1.1) == 3` in class.
- **Programming:** the `int()`-truncation bug and its fix with `math.ceil()`; percentage-based resizing as an alternative to doubling; renaming `_zip_codes` to `_underlying`, and the single- versus double-underscore privacy convention.
- **Math:** floor versus ceiling as two different roundings of the same real number, $\lfloor 3.3 \rfloor = 3$ versus $\lceil 3.3 \rceil = 4$ -- the exact distinction the bug hinged on -- and why "always round up" is the correct policy whenever the rounded value is a required minimum (a capacity), not a mere estimate.
- **Reading:** docs.python.org -- Private Variables, Mathematics in the standard library; Lubanovic Ch. 12 (Modules and packages).

---

## Week 5 -- Dunder Methods, Bounds Checking, and Delegation
*(= original Week 4)*

- **Linux/System:** `echo $?` immediately after a command as a parallel to a method's return value -- both are a signal the caller inspects to decide what happened, without needing to see the command's or method's internals.
- **Programming:** `__str__` and `__len__` as dunder methods Python wires to built-in behavior; the negative-index trap in `get()` and its `index >= 0` fix; refactoring `contains()` to delegate to `index_of()`; the shift-and-clear `remove()` algorithm; generalizing `_underlying` from `list[int]` to `list`.
- **Math:** the half-open interval $[0, \text{size})$ as the precise statement of "a valid index" -- the same interval notation that will describe a hash table's valid slot range in week 14, and the load-factor threshold's valid range in week 15.
- **Reading:** docs.python.org -- Class and Instance Variables, Private Variables, More on Lists.

---

## Week 6 -- Contracts, Composition, and the First Linked Node
*(= original Week 5)*

- **Linux/System:** `man python3` and `python3 --help` as an example of a documented contract -- the same idea an abstract base class enforces for a Python class, just for a command-line program instead.
- **Programming:** the data-structure contract (`contains`, `index_of`, `index_of_all`, `count`, `remove`) as an abstract base class; `FellowshipRoster` as composition ("has a" `DynamicArray`) rather than inheritance; docstrings, magic-value constants, `str.join()` over repeated concatenation; `station.py` as the first object whose field points to another object of the same class.
- **Math:** a contract as a set of required properties, the way a mathematical structure (a group, in the fullest generality) is defined by the operations it must support rather than by what it is made of -- an informal preview of "interface over implementation" as a mathematical, not just programming, idea.
- **Reading:** docs.python.org -- `abc` -- Abstract Base Classes, `str.join`, Classes (full chapter); Lubanovic Ch. 11 -- Inheritance.

---

## Week 7 -- Linked Traversal, Tail Pointers, and Big O
*(= original Week 6)*

- **Linux/System:** `find . -name "*.py"` as a linear scan through a directory tree -- directly parallel to the $\mathcal O(n)$ traversal needed to find the end of a `Trainline` before a `_tail` pointer is added.
- **Programming:** traversal-based `add()` and its $\mathcal O(n)$ cost; the `_tail` pointer bringing `add()` to $\mathcal O(1)$; Big O as an upper bound versus Big Theta as a tight bound; implementing the full data-structure contract on `Trainline`; `__iter__` via `yield`.
- **Math:** formal definitions, $f(n) \in \mathcal O(g(n))$ when $f(n) \leq c \cdot g(n)$ for some constant $c$, and $f(n) \in \Theta(g(n))$ when $c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$; the rice-on-a-chessboard and museum-heist examples for exponential and factorial growth.
- **Reading:** docs.python.org -- Classes (full chapter); `abc` -- Abstract Base Classes.

---

## Week 8 -- Generic Nodes and a Doubly Linked List
*(= original Week 7, part 1)*

- **Linux/System:** symbolic links (`ln -s`) as a filesystem's own version of a pointer -- two names, one underlying target, exactly the relationship a node's `next` field has to the node it points to.
- **Programming:** `Node` generalized with `TypeVar`/`Generic` and `from __future__ import annotations`; `DoubleLinkedList`'s constructor; the slow/fast cursor technique for finding a list's middle node in one pass; maintaining a count field so the middle is reachable without any traversal.
- **Math:** the staircase argument behind the slow/fast cursor -- if the fast cursor covers $2k$ steps while the slow one covers $k$, the slow cursor is at position $\lfloor n/2 \rfloor$ exactly when the fast one reaches the end -- stated as a short invariant, not just demonstrated by example.
- **Reading:** docs.python.org -- Type hints (`typing` module), Classes (full chapter).

---

## Week 9 -- Discontinuity, Cycles, and Reversal in O(1) and O(n)
*(= original Week 7, part 2)*

- **Linux/System:** `readlink -f` following a chain of symbolic links to its final target -- a real command whose job is exactly cycle-avoidance, the same hazard `has_loop_bidirectional` is built to detect.
- **Programming:** `add()` completing the doubly linked list; detecting a broken bidirectional link (`is_continuous`); detecting a cycle in $\mathcal O(1)$ by inspecting a well-maintained `_tail` (`has_loop_unidirectional`) or a ring-wired head/tail pair (`has_loop_bidirectional`); reversing a forward-only list in place by rewiring pointers, not rebuilding.
- **Math:** a cycle in a linked structure as a graph-theoretic idea stated early -- a sequence of nodes with a repeated visit -- previewing the vertex/edge vocabulary week 11 introduces formally for general graphs.
- **Reading:** docs.python.org -- Type hints (`typing` module), Classes (full chapter).

---

## Week 10 -- O(1) Ends, Recursion, and a Stack/Queue Superclass
*(= original Week 8)*

- **Linux/System:** the shell's own call stack, visible in a recursive `find` traversal or in `bash -x` tracing nested function calls -- a concrete, inspectable stack next to the Python call stack a recursive factorial uses.
- **Programming:** removing the head or tail of a doubly linked list in three constant-time steps; recursion and the maximum-recursion-depth crash as a bridge to the call stack; `push`/`pop`, `enqueue`/`dequeue`, `peek`, `is_empty`; `BoundedCollection` as a shared superclass for `Stack` and `Queue` via inheritance, distinguished only by which end of `self._items` each `_add` call targets.
- **Math:** the recursive definition $n! = n \times (n - 1)!$ with base case $0! = 1$, and a short recurrence-relation framing of its own cost -- $T(n) = T(n-1) + \mathcal O(1)$, unrolling to $T(n) = \mathcal O(n)$ -- the course's first explicit recurrence, in miniature.
- **Reading:** docs.python.org -- Classes (full chapter); Lubanovic Ch. 11 -- Inheritance.

---

## Week 11 -- Circular Buffers and Graph Reachability
*(= original Week 9)*

- **Linux/System:** `date` and the 24-hour clock as a working example of modular arithmetic in daily use, a direct parallel to `(position + 1) % capacity` in a circular buffer.
- **Programming:** the array-shifting pitfall (a left-to-right shift-right loop propagating one value, fixed by reversing the loop); circular queues and circular stacks via front/back pointers and modulo arithmetic; graphs as vertices and edges; the adjacency list and adjacency matrix representations; `naive_reachability`'s traversal loop.
- **Math:** periodic boundary conditions and modular arithmetic, $n \bmod m \in \{0, 1, \dots, m-1\}$ for every $n$; a graph's adjacency matrix as a symmetric $n \times n$ matrix (for an undirected graph) with a zero diagonal.
- **Reading:** docs.python.org -- Classes (full chapter), More on Lists.

---

## Week 12 -- Reachability That Stops Early, and a Queue Backed by a File
*(= original Week 9, remainder, + original Week 10, part 1)*

- **Linux/System:** `tail -f` on a growing file as a live illustration of "stop watching the moment the condition you care about is met" -- exactly the design goal of `better_reachability`'s early-stopping while condition.
- **Programming:** `better_reachability`'s single additional piece of state (a found-yet boolean) folded into the while condition instead of a `break`; designing a file-backed queue -- an empty queue as a zero-byte file, one item per line, `enqueue()` as append, `dequeue()` as read-first-line-then-rewrite-the-rest-to-a-temp-file.
- **Math:** counting iterations as a proxy for cost when wall-clock time is too noisy to measure on small inputs -- the same distinction class drew between "shorter" (fewer iterations in the worst case) and an actual stopwatch benchmark.
- **Reading:** docs.python.org -- More on Lists; Lubanovic Ch. 20 (Files).

---

## Week 13 -- Magic Values in a File-Backed Queue, and a File-Backed Stack
*(= original Week 10, part 2)*

- **Linux/System:** `cat`, a text editor, or `less` to inspect a queue/stack's backing file directly after each operation -- confirming by eye that `push()` really did put the new value on the file's first line, the same verification step the week 10 assignment asks students to do by hand.
- **Programming:** replacing hard-coded file names and capacities with named constants (`DEFAULT_FILE_NAME`, `DEFAULT_CAPACITY`); `enqueue()`/`dequeue()` completed; rewriting a file-backed stack so its top lives at the file's *first* line instead of its last, moving the "read one line ahead" complexity from `pop()`/`peek()` into `push()`.
- **Math:** Python's lack of a `final` keyword versus Java's compile-time enforcement (demonstrated with `Final.java` in class) as a concrete example of a *convention* versus a *guarantee* -- the same distinction that separates a documented invariant from a provably enforced one.
- **Reading:** Lubanovic Ch. 20 (Files); Computer file (Wikipedia); Memory & Storage Timeline (Computer History Museum).

---

## Week 14 -- Hash Functions, Collisions, and Chaining
*(= original Week 11, part 1)*

- **Linux/System:** `sha256sum` on a file as a real, professional-grade hash function -- an immediate, concrete answer to "why would anyone need a function that turns arbitrary data into a fixed-size number," next to the toy first-letter hash built in class.
- **Programming:** assigning a hotel room from the first letter of a last name for $\mathcal O(1)$ lookup, and the wasted-room problem that comes with it; linear probing as a first collision strategy, and why it degrades as more keys collide; chaining -- a linked list hanging off every array slot -- recognized as an array of the linked lists already built in week 7.
- **Math:** the pigeonhole principle as the formal reason collisions are unavoidable once the number of possible keys exceeds the number of array slots -- named explicitly here, where the original 11-week course only demonstrated the consequence (Temeeka's "Glass" and Alex's "Garcia" both hashing to the same room) without naming the underlying principle.
- **Reading:** *(placeholder -- flag for instructor: no docs.python.org or Lubanovic citation for hash functions or the pigeonhole principle is currently established in `../../comp-271-su26/CLAUDE.md`'s reading tables; this week's material was taught from original course notes and the in-class hotel-room demonstration.)*

---

## Week 15 -- Hash Tables, Load Factor, and Python's `dict`
*(= original Week 11, part 2)*

- **Linux/System:** `df -h` and the free-space warning threshold most systems use (commonly around 80-90% full) as a real-world load-factor policy -- the same "resize before you're completely full" reasoning behind a hash table's 70% threshold.
- **Programming:** why summing or multiplying ASCII codes makes a weak hash function (predictable periodicities, near-universal evenness for products); `abs()` on a hash code to guard against negative wraparound; inserting new chain nodes at the head for $\mathcal O(1)$ insertion; the load-factor threshold and resize-and-rehash policy; naming Python's `dict` as exactly this structure. Closes with the final assignment, `SimpleHash` (`../../comp-271-su26/week99/last_assignment.md`), which asks students to implement this entire structure themselves.
- **Math:** the load factor $\alpha = \frac{\text{slots used}}{\text{capacity}}$ as the single number that governs the expected chain length (and therefore expected lookup cost) of a hash table -- stated explicitly here, where the original course used the 70% figure without naming $\alpha$ as its own quantity.
- **Reading:** Lubanovic Ch. 9 -- Dictionaries and Sets *(new citation -- already established in `comp170su26/week99/15-week-outline.md` for the same chapter of the same book; flag for instructor to add this row to `../../comp-271-su26/CLAUDE.md`'s reading table, since it has not previously appeared there)*.

---

## Coverage Map

| New week(s) | Original week | What carries over unchanged |
|---|---|---|
| 1 | Week 1 | Separating data from behavior, Mississippi progression, `pasta.py` refactor |
| 2 | Week 2 | Arrays vs. lists, OOP intro, first `DynamicArray` |
| 3-4 | Week 3 | Resize, magic numbers, `math.ceil` bug, encapsulation, naming |
| 5 | Week 4 | Dunder methods, bounds checking, delegation, `remove` |
| 6 | Week 5 | Contracts (`abc`), composition, docstrings, string immutability, node preview |
| 7 | Week 6 | Traversal, tail pointer, Big O/Theta, contract on a linked list, `__iter__` |
| 8-9 | Week 7 | Generic `Node`, doubly linked list, O(1) middle node, discontinuity/loop detection, reversal |
| 10 | Week 8 | O(1) head/tail removal, recursion, `BoundedCollection`/`Stack`/`Queue` |
| 11-12 | Week 9 | Circular buffers, graphs, adjacency list/matrix, reachability (naive and early-stopping) |
| 13 | Week 10 | File-backed queue and stack |
| 14-15 | Week 11 | Hashing, probing, chaining, load factor, resizing, `dict` |

Four blocks absorb the four extra weeks (original Weeks 3, 7, 9, and 11); every other original week keeps its original one-week footprint. No new programming topic was added anywhere in this table -- only linux/system and math threads, which the original 11-week course carried explicitly in only a handful of weeks (mainly Week 6's Big O session and Week 9's modular-arithmetic session), now run through all fifteen.

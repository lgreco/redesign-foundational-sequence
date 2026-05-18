# COMP 170 — Week 1: Your First Python Program
## Tools: Bash Shell + Vim

---

## Goals for the Week

By the end of Week 1, students will be able to:

- Open a terminal and navigate the filesystem using basic Bash commands
- Create, edit, and save a Python file using Vim
- Run a Python script from the command line
- Read and explain a simple Python program line by line
- Recognize and fix a basic syntax error

---

## Day 1 — The Terminal Is a Tool, Not Magic

### Concepts
- What is a program? What does "running code" mean?
- The operating system, the shell, and the terminal: how they relate
- Why we start with the command line before any GUI or IDE

### Demo: First Contact with Bash
```
$ whoami
$ pwd
$ ls
$ ls -l
$ mkdir comp170
$ cd comp170
$ pwd
```

### Key Ideas
- The prompt (`$`) means the shell is waiting for a command
- Every command is a small program
- The filesystem is a tree; `pwd` shows where you are in it

### Student Activity
Navigate to their home directory, create a `comp170/` folder, and confirm it exists with `ls`.

---

## Day 2 — Vim: A Minimal Editor

### Concepts
- What is a text editor? Why not Word or Google Docs?
- Plain text vs. formatted text
- Vim's modal design: **Normal mode** vs. **Insert mode**

### The Two Modes Students Must Know Today

| Mode | How to enter | What you can do |
|---|---|---|
| Normal | Press `Esc` | Move, delete, save, quit |
| Insert | Press `i` | Type text |

### Demo: Creating a File in Vim
```
$ vim hello.py
```
Inside Vim:
```
i                  ← enter Insert mode
(type your code)
Esc                ← return to Normal mode
:w                 ← save (write)
:q                 ← quit
```
Shorthand: `:wq` saves and quits in one step.

### The File to Create
```python
print("Hello, World!")
```

### Common Stumbling Blocks (address directly)
- "I can't type anything" → you are in Normal mode; press `i`
- "I can't get out" → press `Esc`, then `:q!` to quit without saving
- "I saved but I don't know where the file went" → use `ls` to check; `pwd` to confirm location

### Student Activity
Create `hello.py` in their `comp170/` folder using Vim. Save and quit. Confirm the file exists with `ls`.

---

## Day 3 — Running Python; Reading the Program

### Concepts
- The Python interpreter: what it does, how to invoke it
- The difference between writing code and running code
- Reading a program as instructions given to a machine

### Demo: Running the Script
```
$ python3 hello.py
Hello, World!
```

### Taking the Program Apart

Walk through `print("Hello, World!")` one piece at a time:

| Piece | What it is |
|---|---|
| `print` | A built-in function — a named action Python knows how to perform |
| `(` `)` | Parentheses mark the input(s) we are passing to the function |
| `"Hello, World!"` | A string — text data, delimited by quotation marks |

### Introduce a Deliberate Error
Change the file to:
```python
print("Hello, World!"
```
Run it. Read the error message together:
```
SyntaxError: '(' was never closed
```
Key lesson: **error messages are helpful, not hostile**. They tell you what went wrong and where.

Fix the error. Run again. Celebrate.

### Student Activity
Edit `hello.py` to print their own name instead of "Hello, World!". Run it. Then introduce and fix one syntax error on purpose.

---

## Day 4 — Extending the Program; The Edit–Run Loop

### Concepts
- Programs as sequences of instructions
- Variables: giving a name to a value
- The edit–save–run cycle as the basic unit of programming work

### Demo: A Slightly Longer Program
```python
name = "Leo"
print("Hello,", name)
print("Welcome to COMP 170.")
```

Walk through the execution line by line:
1. Line 1 stores the string `"Leo"` under the name `name`
2. Line 2 calls `print` with two arguments; Python puts a space between them automatically
3. Line 3 prints a second line of output

### The Edit–Run Loop
```
vim hello.py   →   make a change   →   :wq   →   python3 hello.py   →   read output   →   repeat
```
This loop is the core of all programming work, regardless of language or tool.

### Student Activity
Extend `hello.py` to print three lines of output: a greeting, their major, and the current year. Use at least one variable.

---

## Day 5 — Review, Questions, and the Bigger Picture

### Review
- Bash commands covered: `pwd`, `ls`, `mkdir`, `cd`, `python3`
- Vim commands covered: `i`, `Esc`, `:w`, `:q`, `:wq`, `:q!`
- Python covered: `print()`, string literals, variables, sequential execution

### Discussion: Why This Workflow?
- Professional programmers spend most of their time in a terminal
- Understanding the shell demystifies what IDEs and notebooks do for you
- Vim is available on every Unix system; knowing the basics is a survival skill

### Looking Ahead
- Next week: arithmetic, expressions, user input with `input()`
- The programs will get longer; the Bash + Vim workflow stays the same

### Lab / Take-Home
Write a Python script `intro.py` that prints a short self-introduction (name, year, one interesting fact). The script must use at least two variables and produce at least three lines of output. Submit by running it in the terminal and showing the output.

---

## Reference Card for Students

### Bash
```
pwd          print working directory
ls           list files
mkdir name   create a directory
cd name      change into a directory
cd ..        go up one level
python3 f    run the Python script f
```

### Vim
```
i            enter Insert mode (start typing)
Esc          return to Normal mode
:w           save
:q           quit
:wq          save and quit
:q!          quit without saving (discard changes)
```

### Python
```python
print("text")          print a string to the screen
print("a", "b")        print multiple values, separated by a space
name = "value"         create a variable called name
print(name)            print the value stored in name
```

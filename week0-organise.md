# Week 0: Tidy Files Like a Programmer: OneDrive & Python Project Structure

## Learning Objectives
- Create a consistent folder hierarchy in OneDrive for school subjects
- Apply good naming conventions (no "New folder (3)", no "final_FINAL")
- Build a simple Python app with an industry-style structure
- Use `import` to run code from their own modules via a `main.py`

## Success Criteria
- OneDrive has subject folders and sensible subfolders
- Python project runs by executing `main.py`
- Student can explain why we import code instead of copying/pasting it

## 1. OneDrive Organisation (15–20 mins)

### Teacher Input
Explain: programmers waste time when files are messy. Good organisation = fewer mistakes, faster work, easier collaboration.

### Student Task: Create a Standard OneDrive Structure
In Documents / School (or similar), create:
- `00_inbox` (dumping ground, temporary)
- `Computer_Science`
- `Maths`
- `English`
- `Science`
- `Other_Subjects` (optional)

Inside each subject, create:
- `01_classwork`
- `02_homework`
- `03_assessments`
- `04_revision`
- `99_resources` (teacher handouts, sheets)

### Rules
- No spaces in folder names (use `_`)
- Start with numbers for ordering
- Never use "misc", "stuff", "new folder", "final final"

### Mini Naming Standard
Good: `python_lists_notes.docx`, `network_quiz_scores.xlsx`

Bad: `notes.docx`, `python work latest.docx`, `FINAL(2).docx`

### Quick Check (5 mins)
Ask pupils to show:
- Their `Computer_Science` folder
- One file renamed properly using the pattern below:

File naming pattern:
```
topic_shortdescription_yyyymmdd.ext
```

Example: `python_imports_practice_20260212.py`

## 2. Python Project Structure (25–30 mins)

### Teacher Input: "A Python Project is Just Organised Folders"
Make the direct link:
- OneDrive subject folders = "projects"
- Subfolders = "parts of a program"
- Good names = `import` works + humans can find things

### Class Creates a Project Folder
Inside their CS OneDrive folder:
```
python_projects/hello_app/
```

### Project Structure (Simple Industry-Style)
```
hello_app/
│  main.py
│  README.md
└─ hello_app/
   │  __init__.py
   │  messages.py
   └─ utils.py
```

### Why This Structure Works
- `main.py` is the "run this" file
- `hello_app/` (inner folder) is the package (reusable code)
- Files like `messages.py` and `utils.py` are modules with clear roles
- Names are lowercase + underscores → predictable, professional

## 3. Coding — Modules and Imports (15 mins)

### Step-by-Step Code (Students Type)

1. `hello_app/messages.py`

```python
def greeting(name):
    return f"Hello, {name}!"
```

2. `hello_app/utils.py`

```python
def ask_name():
    return input("Enter your name: ").strip()
```

3. `main.py` (in the outer folder)

```python
from hello_app.utils import ask_name
from hello_app.messages import greeting

def main():
    name = ask_name()
    print(greeting(name))

if __name__ == "__main__":
    main()
```

### Run It
Students run only `main.py`.

### Teaching Point (Quick Oral Check)
Ask: "Why not just write everything in `main.py`?"

Expected answers:
- Easier to find code
- Less duplication
- Easier to test and reuse
- Teams can work on different files

## Practice Exercises

### Exercise 1: File Renaming
Rename these "bad" files into good names:
- `test.py`
- `python work.py`
- `import thing final.py`

### Exercise 2: New Module
Create a new module:
- Add `hello_app/formatting.py` with a function `shout(text)` that returns the text in uppercase
- Import it in `main.py` and use it on the greeting

```python
# Your code here
```

## Key Concepts to Remember

- **File naming**: use lowercase and underscores, no spaces
- **Folder structure**: numbered prefixes keep folders ordered
- **`main.py`** is the entry point — the file you run
- **Packages** are folders with `__init__.py` — they group related modules
- **Modules** are individual `.py` files with specific roles
- **`import`** lets you reuse code instead of copying and pasting

## Common Mistakes to Avoid

1. Using spaces in file or folder names
2. Naming files "final", "misc", or "new folder"
3. Putting all code in one file instead of using modules
4. Forgetting `__init__.py` in the package folder
5. Running `messages.py` or `utils.py` directly instead of `main.py`

## Extension Challenge

Extend the `hello_app` project:
1. Add `hello_app/formatting.py` with a `shout(text)` function that returns text in uppercase
2. Update `main.py` to use `shout()` on the greeting output
3. Create a second project folder for a different app using the same structure

```python
# Your code here
```

# Week 0: Tidy Files Like a Programmer: OneDrive & Python Project Structure

## Navigation
⬅️ [Back to Overview](README.md) | ➡️ [Next: Basics](week1-basics.md)

---

## Learning Objectives
- Create a consistent folder hierarchy in OneDrive for school subjects.
- Apply good naming conventions (no "New folder (3)", no "final_FINAL").
- Build a simple Python app with an industry-style structure.
- Use `import` to run code from their own modules via a `main.py`.

## Success Criteria
- OneDrive has subject folders and sensible subfolders.
- A Python project runs by executing `main.py`.
- Students can explain why we import code instead of copying and pasting it.

---

## 1. Organise Your Files in OneDrive

Programmers waste time when files are messy. A clear structure reduces mistakes, makes work easier to find, and helps everyone collaborate.

In `Documents / School` (or a similar area), create:

- `00_inbox` (temporary dumping ground)
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
- `99_resources`

### Naming rules
- Use underscores instead of spaces.
- Start folders with numbers to keep them organised.
- Avoid names like `misc`, `stuff`, `new folder`, or `final final`.

### Good and bad file names
**Good:** `python_lists_notes.docx`, `network_quiz_scores.xlsx`  
**Bad:** `notes.docx`, `python work latest.docx`, `FINAL(2).docx`

### File naming pattern
`topic_shortdescription_yyyymmdd.ext`  
Example: `python_imports_practice_20260212.py`

### Quick check
Ask students to show:
- their `Computer_Science` folder
- one file renamed using the pattern above

---

## 2. Mirror That Structure in a Python Project

A Python project works best when its files are organised in a predictable way. The same idea applies to OneDrive: tidy folders help people find and reuse code.

Inside their CS folder, create a project such as:

```text
python_projects/hello_app/
```

Use this simple industry-style structure:

```text
hello_app/
│  main.py
│  README.md
└─ hello_app/
   │  __init__.py
   │  messages.py
   └─ utils.py
```

### Why this structure works
- `main.py` is the file that runs the program.
- The inner `hello_app/` folder is the package, where reusable code lives.
- Files like `messages.py` and `utils.py` are modules with clear roles.
- Lowercase names with underscores are easier to read and more professional.

---

## 3. Coding: Modules and Imports

### 1) `hello_app/messages.py`

```python
def greeting(name):
    return f"Hello, {name}!"
```

### 2) `hello_app/utils.py`

```python
def ask_name():
    return input("Enter your name: ").strip()
```

### 3) `main.py` (in the outer folder)

```python
from hello_app.utils import ask_name
from hello_app.messages import greeting


def main():
    name = ask_name()
    print(greeting(name))


if __name__ == "__main__":
    main()
```

### Run it
Students run only `main.py`.

This keeps the main program simple while the code for input and greeting is stored in separate modules. That makes it easier to reuse and maintain.

---

## Mini Challenge
Create a second function in `utils.py` called `ask_age()` and use it in `main.py` to print a friendly message such as:

```python
print(f"Nice to meet you, {name}! You are {age} years old.")
```

---

## Key Concepts to Remember
- **File naming**: use lowercase and underscores; avoid spaces.
- **Project structure**: keep code organised into folders and modules.
- **`main.py`**: the file used to start the program.
- **Imports**: let Python access code from another file without copying it.
- **Good organisation**: makes programs easier to read, test, and extend.

---

## Navigation
⬅️ [Back to Overview](README.md) | ➡️ [Next: Basics](week1-basics.md)

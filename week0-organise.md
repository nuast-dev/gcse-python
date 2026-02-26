Tidy Files Like a Programmer
OneDrive & Python Project Structure
Lesson Title
Tidy Files Like a Programmer: OneDrive & Python Project Structure
Learning goals
Students will be able to:
1.	Create a consistent folder hierarchy in OneDrive for school subjects.
2.	Apply good naming conventions (no “New folder (3)”, no “final_FINAL”).
3.	Build a simple Python app with an industry-style structure.
4.	Use import to run code from their own modules via a main.py.
Success criteria
•	OneDrive has subject folders + sensible subfolders
•	Python project runs by executing main.py
•	Student can explain why we import code instead of copying/pasting it
Part 1 (15–20 mins): OneDrive “Refactor”
Teacher input (2–3 mins)
Explain: programmers waste time when files are messy. Good organisation = fewer mistakes, faster work, easier collaboration.
Student task: create a standard OneDrive structure
In Documents / School (or similar), create:
•	00_inbox (dumping ground, temporary)
•	Computer_Science
•	Maths
•	English
•	Science
•	Other_Subjects (optional)
Inside each subject, create:
•	01_classwork
•	02_homework
•	03_assessments
•	04_revision
•	99_resources (teacher handouts, sheets)

Rules
•	No spaces in folder names (use _)
•	Start with numbers for ordering
•	Never use “misc”, “stuff”, “new folder”, “final final”
Mini naming standard (put on board)
Good: python_lists_notes.docx, network_quiz_scores.xlsx
Bad: notes.docx, python work latest.docx, FINAL(2).docx
Quick check (5 mins)
Ask pupils to show:
•	Their Computer_Science folder
•	One file renamed properly using the pattern below:
File naming pattern:
topic_shortdescription_yyyymmdd.ext
Example: python_imports_practice_20260212.py

Part 2 (25–30 mins): Mirror that structure in a Python project
Teacher input (5 mins): “A Python project is just organised folders”
Make the direct link:
•	OneDrive subject folders = “projects”
•	Subfolders = “parts of a program”
•	Good names = import works + humans can find things
Class creates a project folder
Inside their CS OneDrive folder:
python_projects/hello_app/
Project structure (simple industry-style)
hello_app/
│  main.py
│  README.md
└─ hello_app/
   │  __init__.py
   │  messages.py
   └─ utils.py

Why this structure works
•	main.py is the “run this” file
•	hello_app/ (inner folder) is the package (reusable code)
•	Files like messages.py and utils.py are modules with clear roles
•	Names are lowercase + underscores → predictable, professional


Part 3 (15 mins): Coding — modules + imports
Step-by-step code (students type)
1)	`hello_app/messages.py`

def greeting(name):
    return f"Hello, {name}!"
2) `hello_app/utils.py`

def ask_name():
    return input("Enter your name: ").strip()
3) `main.py` (in the outer folder)

from hello_app.utils import ask_name
from hello_app.messages import greeting

def main():
    name = ask_name()
    print(greeting(name))

if __name__ == "__main__":
    main()

Run it
Students run only main.py.
Teaching point (quick oral check)
Ask: “Why not just write everything in main.py?”
Expected answers:
•	easier to find code
•	less duplication
•	easier to test and reuse
•	teams can work on different files
Part 4 (10 mins): Organisation “challenge mode”
Give them messy items (realistic) and have them fix it.



Quick practical challenges
5.	Rename these “bad” files into good names:
•	test.py
•	python work.py
•	import thing final.py
6.	Create a new module:
•	hello_app/formatting.py with a function shout(text) that returns uppercase.
•	Import it in main.py and use it on the greeting.

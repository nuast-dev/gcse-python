# Student Work Directory

Welcome to your student work package! This directory is organized as a Python package where you'll complete your weekly exercises.

## 📁 Directory Structure

```
student_work/
├── __init__.py                 # Makes this a Python package
├── README.md                   # This file
├── main.py                     # Main file to run your functions
├── week1_basics/              # Week 1 exercises
│   ├── __init__.py
│   └── exercises.py           # Your Week 1 solutions
├── week2_conditionals/        # Week 2 exercises
│   ├── __init__.py
│   └── exercises.py           # Your Week 2 solutions
├── week3_loops/               # Week 3 exercises
│   ├── __init__.py
│   └── exercises.py           # Your Week 3 solutions
├── week4_strings/             # Week 4 exercises
│   ├── __init__.py
│   └── exercises.py           # Your Week 4 solutions
├── week5_lists/               # Week 5 exercises
│   ├── __init__.py
│   └── exercises.py           # Your Week 5 solutions
├── week6_functions/           # Week 6 exercises
│   ├── __init__.py
│   └── exercises.py           # Your Week 6 solutions
├── week7_files/               # Week 7 exercises
│   ├── __init__.py
│   └── exercises.py           # Your Week 7 solutions
└── week8_algorithms/          # Week 8 exercises
    ├── __init__.py
    └── exercises.py           # Your Week 8 solutions
```

## 🚀 Getting Started

### 1. Working on Exercises

Each week has its own folder where you'll write your exercise solutions:

1. Navigate to the week folder (e.g., `week1_basics`)
2. Create or edit `exercises.py`
3. Write your functions and code
4. Test your code as you go

### 2. Example: Creating a Function

In `week1_basics/exercises.py`:
```python
def greet_user(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def calculate_age(birth_year):
    """Calculate age from birth year."""
    current_year = 2026
    return current_year - birth_year
```

### 3. Running Your Code

#### Option A: Run from main.py
Use the `main.py` file to import and run your functions:

```python
# Import from weekly modules
from student_work.week1_basics.exercises import greet_user, calculate_age

# Run your functions
print(greet_user("Alice"))
print(calculate_age(2010))
```

Run from the repository root:
```bash
python student_work/main.py
```

#### Option B: Run directly
You can also run your exercises directly:
```bash
python student_work/week1_basics/exercises.py
```

#### Option C: Use Python REPL
```python
>>> from student_work.week1_basics.exercises import greet_user
>>> greet_user("Bob")
'Hello, Bob!'
```

## 📚 Weekly Topics

- **Week 1**: Basics - I/O, Variables, Types, Casting, Arithmetic
- **Week 2**: Conditionals - If/elif/else, Boolean Logic
- **Week 3**: Loops - For/while, Counters, Sentinel values
- **Week 4**: Strings - Indexing, Slicing, Methods, Validation
- **Week 5**: Lists - Methods, Traversal, Statistics
- **Week 6**: Functions - Parameters, Return, Decomposition
- **Week 7**: Files - Read/Write, Processing, CSV data
- **Week 8**: Algorithms - Searching, Sorting, Problem Solving

## 💡 Best Practices

1. **One function per exercise**: Keep functions focused and simple
2. **Use docstrings**: Document what your functions do
3. **Test thoroughly**: Try different inputs to verify your code works
4. **Follow naming conventions**: Use `snake_case` for functions and variables
5. **Keep it organized**: Put related functions in the same week folder

## 🧪 Testing Your Code

Add simple test cases at the bottom of your exercise files:

```python
if __name__ == "__main__":
    # Test your functions
    print(greet_user("Alice"))  # Expected: Hello, Alice!
    print(calculate_age(2010))  # Expected: 16
```

Then run: `python student_work/week1_basics/exercises.py`

## 📝 Tips

- Start with Week 1 and progress sequentially
- Complete all exercises before moving to the next week
- Review the course materials in the main repository
- Refer to weekly markdown files for detailed instructions
- Ask for help if you get stuck!

## 🎯 Learning Goals

By organizing your work this way, you'll learn to:
- Structure Python projects professionally
- Work with packages and modules
- Import and reuse code across files
- Build a portfolio of your progress
- Prepare for real-world Python development

---

**Happy coding! 🐍**

For detailed weekly lessons, see the markdown files in the repository root:
- [Week 1: Basics](../week1-basics.md)
- [Week 2: Conditionals](../week2-conditionals.md)
- [Week 3: Loops](../week3-loops.md)
- [Week 4: Strings](../week4-strings.md)
- [Week 5: Lists](../week5-lists.md)
- [Week 6: Functions](../week6-functions.md)
- [Week 7: Files](../week7-files.md)
- [Week 8: Algorithms](../week8-algorithms.md)

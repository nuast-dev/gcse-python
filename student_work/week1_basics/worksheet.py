#!/usr/bin/python3
"""
========================================================================
GCSE Python — Week 1 Worksheet
Topics: print(), input(), variables, data types, type casting,
        arithmetic operators, order of operations, f-strings
========================================================================

HOW TO USE THIS WORKSHEET
--------------------------
1. Read each task carefully.
2. Write your code where you see:
       # +++your code here+++
3. Run the file to check your answers:
       python worksheet.py
4. A score summary will appear at the bottom.
5. Fix any failing tasks and run again.

Good luck — you've got this! 🐍


------------------------------------------------------------------------
TEACHER NOTE
------------------------------------------------------------------------
This worksheet contains 11 self-marking tasks for Week 1.

How it works
  • Each task is a Python function students complete (task_1, add_five, …).
  • Corresponding check_task_N() functions call the student's code,
    compare results against expected values, and print ✓ or ✗.
  • run_all_tests() (at the bottom) runs every check in order and
    prints a final score.
  • Students only need to fill in code marked +++your code here+++.
    Everything else is already wired up.

Splitting tasks for individual lessons
  • Each task is clearly delimited by a comment banner so it can be
    copied into a separate file or IDE snippet.
  • The self-marking helpers (_check, _score, _total) are small enough
    to copy alongside each task.

Week 1 skills assessed — task by task
  Task 1  — print() / returning a string value
  Task 2  — variables (str, int); returning multiple values as a tuple
  Task 3  — checking types with type().__name__
  Task 4  — simulated input() (string parameter); string concatenation
  Task 5  — type casting: int() to fix a TypeError (fix-the-code)
  Task 6  — arithmetic operators: *, -, //
  Task 7  — order of operations / BIDMAS (prediction task)
  Task 8  — exponentiation (**); arithmetic
  Task 9  — f-strings; division; percentage calculation
  Task 10 — f-strings with :.2f; combining arithmetic and formatting
  Task 11 — type casting float(); arithmetic; f-strings (extension)
------------------------------------------------------------------------
"""

# ============================================================
# Task 1 — Say Hello                    [print / string output]
# ============================================================
# Your job: complete the function so it RETURNS the string:
#   "Hello, World!"
#
# Example:
#   task_1()  →  "Hello, World!"
#
# Tip: use a return statement — we test the returned value,
# not what is printed directly to the screen.

def task_1():
    # +++your code here+++
    return "CHANGE ME"


# ============================================================
# Task 2 — Personal Details                      [variables]
# ============================================================
# Your job: inside the function below, change the two variables:
#   name  → your first name as a string
#   age   → your age as a whole number (int)
# Then return them together as a tuple: (name, age)
#
# Example (if your name is Sam and you are 15):
#   task_2()  →  ("Sam", 15)

def task_2():
    name = "CHANGE ME"   # ← replace with your first name
    age = 0              # ← replace with your age
    return (name, age)


# ============================================================
# Task 3 — Spot the Type               [data types / type()]
# ============================================================
# Four values are stored in variables below.
# Your job: fill in their type names as strings using
#   type(value).__name__
# and return them in a list: [type_a, type_b, type_c, type_d]
#
# The four values are: 42, 3.14, "hello", True
#
# Expected return: ["int", "float", "str", "bool"]
#
# Tip:   type(42).__name__  →  "int"

def task_3():
    a = 42
    b = 3.14
    c = "hello"
    d = True
    type_a = "CHANGE ME"   # +++your code here+++
    type_b = "CHANGE ME"   # +++your code here+++
    type_c = "CHANGE ME"   # +++your code here+++
    type_d = "CHANGE ME"   # +++your code here+++
    return [type_a, type_b, type_c, type_d]


# ============================================================
# Task 4 — Welcome Message              [simulated input()]
# ============================================================
# When a student runs a real program they would write:
#   name = input("What is your name? ")
# Here we pass the name as a parameter to make it testable.
#
# Your job: given name_str (a string, as if typed by the user),
# return a welcome message in exactly this format:
#   "Welcome, Alice!"
#
# Examples:
#   greet("Alice")   →  "Welcome, Alice!"
#   greet("Jordan")  →  "Welcome, Jordan!"
#
# Tip: you can use an f-string or string concatenation.

def greet(name_str):
    # +++your code here+++
    return "CHANGE ME"


# ============================================================
# Task 5 — Fix the Code                      [type casting]
# ============================================================
# The function below is BROKEN. It tries to add 5 to a number
# but the number arrives as a string (just like input() gives you).
#
# Fix the ONE broken line so the function works correctly.
#
# Examples:
#   add_five("10")  →  15
#   add_five("3")   →  8
#
# Hint: cast number_str to an int before doing the arithmetic.

def add_five(number_str):
    result = number_str + 5   # BUG: fix this line +++
    return result


# ============================================================
# Task 6 — Sweet Shop             [arithmetic operators: * - //]
# ============================================================
# A sweet shop sells bags of sweets.
# Your job: complete the function.
#
# Given:
#   price_each  — price of one bag in pence (int)
#   num_bags    — number of bags to buy (int)
#
# Calculate and return a TUPLE:
#   (total_cost, change_from_200, bags_for_pound)
# where:
#   total_cost      = price_each * num_bags
#   change_from_200 = 200 - total_cost    (change from £2.00, in pence)
#   bags_for_pound  = 100 // price_each   (whole bags you can buy with £1)
#
# Example:
#   sweet_shop(35, 4)  →  (140, 60, 2)

def sweet_shop(price_each, num_bags):
    # +++your code here+++
    return (0, 0, 0)


# ============================================================
# Task 7 — Prediction Task      [order of operations / BIDMAS]
# ============================================================
# Look at these five calculations WITHOUT running them first.
# Work out what Python will produce for each one, then replace
# the zeros below with your predictions.
#
#   a = 2 + 3 * 4        →  ?
#   b = (2 + 3) * 4      →  ?
#   c = 10 - 2 ** 3      →  ?
#   d = 10 % 3           →  ?
#   e = 17 // 3          →  ?
#
# Return a tuple: (a, b, c, d, e)
#
# Reminder — Python follows BIDMAS:
#   Brackets → Indices (**) → Divide / Multiply → Add / Subtract
# % (modulus) and // (floor division) have the same priority as * and /.

def task_7_predict():
    a = 0   # ← replace with your prediction for  2 + 3 * 4
    b = 0   # ← replace with your prediction for  (2 + 3) * 4
    c = 0   # ← replace with your prediction for  10 - 2 ** 3
    d = 0   # ← replace with your prediction for  10 % 3
    e = 0   # ← replace with your prediction for  17 // 3
    return (a, b, c, d, e)


# ============================================================
# Task 8 — Powers and Volumes          [exponentiation: **]
# ============================================================
# Your job: complete the function.
#
# Given a length (int or float), calculate:
#   area   = length ** 2   (area of a square with that side)
#   volume = length ** 3   (volume of a cube with that side)
#
# Return a TUPLE: (area, volume)
#
# Examples:
#   square_cube(4)  →  (16, 64)
#   square_cube(3)  →  (9, 27)

def square_cube(length):
    # +++your code here+++
    return (0, 0)


# ============================================================
# Task 9 — Report Card                       [f-strings]
# ============================================================
# Your job: complete the function so it returns a formatted
# report card line using an f-string.
#
# Given:
#   name   — student name (str)
#   score  — marks achieved (int)
#   total  — total marks available (int)
#
# Return a string in exactly this format:
#   "Alice scored 42/50 (84.0%)"
#
# Steps:
#   1. Calculate  percentage = score / total * 100
#   2. Build and return the f-string
#
# Use {percentage:.1f} to show one decimal place.
#
# Examples:
#   report_card("Alice", 42, 50)  →  "Alice scored 42/50 (84.0%)"
#   report_card("Ben", 18, 25)    →  "Ben scored 18/25 (72.0%)"

def report_card(name, score, total):
    percentage = score / total * 100
    # +++your code here (write the return statement with f-string)+++
    return "CHANGE ME"


# ============================================================
# Task 10 — Sale Tag              [f-strings + arithmetic]
# ============================================================
# A shop is having a summer sale.
# Your job: complete the function.
#
# Given:
#   item_name  — name of the item (str)
#   full_price — original price in £ (float)
#   discount   — discount as a whole-number percentage, e.g. 20 = 20%
#
# Calculate:
#   saving     = full_price * discount / 100
#   sale_price = full_price - saving
#
# Return a string in exactly this format (prices to 2 decimal places):
#   "Trainers: was £49.99, now £39.99 (saving £10.00)"
#
# Examples:
#   sale_price_tag("Trainers", 49.99, 20)
#       →  "Trainers: was £49.99, now £39.99 (saving £10.00)"
#   sale_price_tag("Jacket", 60.00, 25)
#       →  "Jacket: was £60.00, now £45.00 (saving £15.00)"

def sale_price_tag(item_name, full_price, discount):
    saving = full_price * discount / 100
    sale_price = full_price - saving
    # +++your code here (write the return statement with f-string)+++
    return "CHANGE ME"


# ============================================================
# Task 11 — Extension Challenge      [all Week 1 skills]
# ============================================================
# Write a function that works like a temperature converter.
#
# Given:
#   celsius_str — a temperature as a STRING (as if from input())
#
# Steps:
#   1. Cast celsius_str to a float
#   2. Convert to Fahrenheit:  F = C * 9/5 + 32
#   3. Convert to Kelvin:      K = C + 273.15
#   4. Return a string using f-strings with 1 decimal place each
#
# Format (all three values to 1 d.p.):
#   "20.0°C = 68.0°F = 293.2K"
#
# Examples (Python's float precision means Kelvin may differ from pen-and-paper maths):
#   temp_converter("20")   →  "20.0°C = 68.0°F = 293.1K"
#   temp_converter("100")  →  "100.0°C = 212.0°F = 373.1K"
#   temp_converter("0")    →  "0.0°C = 32.0°F = 273.1K"
#
# Tip: use {value:.1f} inside an f-string for one decimal place.

def temp_converter(celsius_str):
    # +++your code here+++
    return "CHANGE ME"


# ============================================================
#                    SELF-MARKING SYSTEM
#     (You do not need to edit anything below this line.)
# ============================================================

_score = 0
_total = 0


def _check(label, passed, hint=""):
    """Record one test result and print a pass/fail line."""
    global _score, _total
    _total += 1
    if passed:
        _score += 1
        print(f"  \u2713  {label}")
    else:
        msg = f"  \u2717  {label}"
        if hint:
            msg += f"  \u2190 {hint}"
        print(msg)


def check_task_1():
    print("\nTask 1 \u2014 Say Hello")
    result = task_1()
    _check(
        "Returns 'Hello, World!'",
        result == "Hello, World!",
        "Make sure you return exactly: Hello, World!",
    )


def check_task_2():
    print("\nTask 2 \u2014 Personal Details")
    result = task_2()
    ok_tuple = isinstance(result, tuple) and len(result) == 2
    _check("Returns a tuple of two values", ok_tuple)
    if ok_tuple:
        name, age = result
        _check(
            "name is a non-empty string (not 'CHANGE ME')",
            isinstance(name, str) and name not in ("CHANGE ME", "") and len(name) > 0,
            "Set name to your actual first name",
        )
        _check(
            "age is an integer (0 < age < 120)",
            isinstance(age, int) and 0 < age < 120,
            "Set age to your actual age as a whole number",
        )


def check_task_3():
    print("\nTask 3 \u2014 Spot the Type")
    result = task_3()
    _check(
        "Returns ['int', 'float', 'str', 'bool']",
        result == ["int", "float", "str", "bool"],
        "Use type(value).__name__ for each variable",
    )


def check_task_4():
    print("\nTask 4 \u2014 Welcome Message")
    _check(
        "greet('Alice') \u2192 'Welcome, Alice!'",
        greet("Alice") == "Welcome, Alice!",
    )
    _check(
        "greet('Jordan') \u2192 'Welcome, Jordan!'",
        greet("Jordan") == "Welcome, Jordan!",
    )


def check_task_5():
    print("\nTask 5 \u2014 Fix the Code (type casting)")
    try:
        r1 = add_five("10")
        _check("add_five('10') \u2192 15", r1 == 15, "Cast number_str to int() before adding")
        r2 = add_five("3")
        _check("add_five('3') \u2192 8", r2 == 8)
    except TypeError:
        _check("add_five('10') \u2192 15", False, "Still a TypeError \u2014 wrap number_str with int()")
        _check("add_five('3') \u2192 8", False)


def check_task_6():
    print("\nTask 6 \u2014 Sweet Shop")
    _check("sweet_shop(35, 4) \u2192 (140, 60, 2)", sweet_shop(35, 4) == (140, 60, 2))
    _check("sweet_shop(25, 3) \u2192 (75, 125, 4)", sweet_shop(25, 3) == (75, 125, 4))
    _check("sweet_shop(50, 2) \u2192 (100, 100, 2)", sweet_shop(50, 2) == (100, 100, 2))


def check_task_7():
    print("\nTask 7 \u2014 Prediction Task (order of operations)")
    correct = (14, 20, 2, 1, 5)
    result = task_7_predict()
    _check(
        "All five predictions correct: (14, 20, 2, 1, 5)",
        result == correct,
        "Check BIDMAS: \u00d7 before +, ** before \u2212, // and % share priority with *",
    )


def check_task_8():
    print("\nTask 8 \u2014 Powers and Volumes")
    _check("square_cube(4) \u2192 (16, 64)", square_cube(4) == (16, 64))
    _check("square_cube(3) \u2192 (9, 27)", square_cube(3) == (9, 27))
    _check("square_cube(2) \u2192 (4, 8)", square_cube(2) == (4, 8))


def check_task_9():
    print("\nTask 9 \u2014 Report Card (f-strings)")
    cases = [("Alice", 42, 50), ("Ben", 18, 25), ("Priya", 25, 25)]
    for name, score, total in cases:
        pct = score / total * 100
        expected = f"{name} scored {score}/{total} ({pct:.1f}%)"
        _check(
            f"report_card('{name}', {score}, {total}) \u2192 '{expected}'",
            report_card(name, score, total) == expected,
            "Use an f-string with {percentage:.1f}",
        )


def check_task_10():
    print("\nTask 10 \u2014 Sale Tag (mini-program)")
    cases = [("Trainers", 49.99, 20), ("Jacket", 60.00, 25), ("Cap", 8.00, 50)]
    for item, price, disc in cases:
        saving = price * disc / 100
        sale = price - saving
        expected = f"{item}: was \u00a3{price:.2f}, now \u00a3{sale:.2f} (saving \u00a3{saving:.2f})"
        _check(
            f"sale_price_tag('{item}', {price}, {disc})",
            sale_price_tag(item, price, disc) == expected,
            "Use :.2f for money amounts inside your f-string",
        )


def check_task_11():
    print("\nTask 11 \u2014 Extension: Temperature Converter")
    for c_str in ["20", "100", "0", "-10"]:
        c = float(c_str)
        f_val = c * 9 / 5 + 32
        k_val = c + 273.15
        expected = f"{c:.1f}\u00b0C = {f_val:.1f}\u00b0F = {k_val:.1f}K"
        _check(
            f"temp_converter('{c_str}') \u2192 '{expected}'",
            temp_converter(c_str) == expected,
            "Cast to float, calculate F and K, then use :.1f in f-string",
        )


def run_all_tests():
    """Run every check function and display the final score."""
    global _score, _total
    _score = 0
    _total = 0

    print("=" * 60)
    print("  GCSE Python \u2014 Week 1 Worksheet   \U0001f40d  Self-Marking")
    print("=" * 60)

    check_task_1()
    check_task_2()
    check_task_3()
    check_task_4()
    check_task_5()
    check_task_6()
    check_task_7()
    check_task_8()
    check_task_9()
    check_task_10()
    check_task_11()

    print()
    print("=" * 60)
    print(f"  SCORE: {_score} / {_total}")
    if _score == _total:
        print("  Outstanding! All tasks complete! \U0001f389")
    elif _score >= _total * 0.8:
        print("  Great work \u2014 almost there! \U0001f31f")
    elif _score >= _total * 0.5:
        print("  Good effort \u2014 keep going! \U0001f4aa")
    else:
        print("  Keep trying \u2014 you can do it! \U0001f680")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()

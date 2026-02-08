# Week 2: If/Elif/Else, Comparisons, Boolean Logic, and Range Checks

## Learning Objectives
- Use if/elif/else statements for decision making
- Apply comparison operators correctly
- Understand and use boolean logic (AND, OR, NOT)
- Perform range checks and complex conditions
- Write clean, readable conditional code

## 1. Comparison Operators

### Basic Comparisons
```python
# Equal to
5 == 5  # True
5 == 3  # False

# Not equal to
5 != 3  # True
5 != 5  # False

# Greater than
10 > 5  # True
5 > 10  # False

# Less than
5 < 10  # True
10 < 5  # False

# Greater than or equal to
10 >= 10  # True
10 >= 5   # True

# Less than or equal to
5 <= 10  # True
5 <= 5   # True
```

### Comparing Strings
```python
"apple" == "apple"  # True
"Apple" == "apple"  # False (case-sensitive)

"apple" < "banana"  # True (alphabetical order)
"zebra" > "apple"   # True
```

## 2. If Statements

### Simple If Statement
```python
age = 16

if age >= 16:
    print("You can get a National Insurance number")
    print("You can work part-time")
```

### If-Else Statement
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### If-Elif-Else Statement
```python
score = int(input("Enter your test score: "))

if score >= 90:
    print("Grade: A*")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")
```

## 3. Boolean Logic

### AND Operator
Both conditions must be True
```python
age = 16
has_id = True

if age >= 16 and has_id:
    print("You can apply for a job")

# Multiple AND conditions
score = 75
attendance = 95

if score >= 70 and attendance >= 90:
    print("Excellent performance!")
```

### OR Operator
At least one condition must be True
```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# Multiple OR conditions
grade = "A"

if grade == "A*" or grade == "A" or grade == "B":
    print("Well done!")
```

### NOT Operator
Inverts the boolean value
```python
is_raining = False

if not is_raining:
    print("You don't need an umbrella")

logged_in = True

if not logged_in:
    print("Please log in")
else:
    print("Welcome back!")
```

### Combining Operators
```python
age = 16
student = True
has_card = True

if (age >= 16 and age < 18) and (student or has_card):
    print("You qualify for youth discount")

# Use parentheses to control order of evaluation
if (score >= 80 or extra_credit >= 10) and attendance >= 90:
    print("Bonus points awarded!")
```

## 4. Range Checks

### Checking if Value is in Range
```python
age = int(input("Enter your age: "))

# Method 1: Using AND
if age >= 13 and age <= 19:
    print("You are a teenager")

# Method 2: Chained comparison (more Pythonic)
if 13 <= age <= 19:
    print("You are a teenager")
```

### Multiple Range Checks
```python
temperature = 22

if temperature < 0:
    print("Freezing")
elif 0 <= temperature < 10:
    print("Cold")
elif 10 <= temperature < 20:
    print("Cool")
elif 20 <= temperature < 30:
    print("Warm")
else:
    print("Hot")
```

### Checking Outside a Range
```python
age = int(input("Enter your age: "))

if age < 13 or age > 19:
    print("You are not a teenager")

# Alternative using NOT
if not (13 <= age <= 19):
    print("You are not a teenager")
```

## 5. Common Patterns

### Validating Input
```python
age = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Invalid age entered")
else:
    print("Age accepted:", age)
```

### Multiple Conditions with Variables
```python
username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "student"
correct_password = "python123"

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid credentials")
```

### Nested If Statements
```python
age = int(input("Enter your age: "))

if age >= 16:
    has_license = input("Do you have a license? (yes/no): ")
    if has_license == "yes":
        print("You can drive")
    else:
        print("You need to get a license")
else:
    print("You are too young to drive")
```

## Practice Exercises

### Exercise 1: Grade Classifier
Write a program that:
1. Asks for a test score (0-100)
2. Validates the score is in range
3. Outputs the grade using this scale:
   - 90-100: A*
   - 80-89: A
   - 70-79: B
   - 60-69: C
   - 50-59: D
   - 0-49: F

```python
# Your code here
```

### Exercise 2: Leap Year Checker
A year is a leap year if:
- It's divisible by 4 AND
- Either not divisible by 100 OR divisible by 400

Write a program that checks if a year is a leap year.

```python
# Your code here
```

### Exercise 3: Ticket Price Calculator
Calculate cinema ticket price based on:
- Age under 12: £5
- Age 12-17: £7
- Age 18-64: £10
- Age 65+: £6
- Add £3 if it's a 3D movie
- Add £2 if it's a weekend (Saturday/Sunday)

```python
# Your code here
```

### Exercise 4: Password Validator
Check if a password is valid. A password must:
- Be at least 8 characters long
- Contain at least one digit
- Not be "password" or "12345678"

(Hint: Use `any(char.isdigit() for char in password)` to check for digits)

```python
# Your code here
```

### Exercise 5: BMI Calculator with Categories
Calculate BMI (weight / height²) and categorize:
- Under 18.5: Underweight
- 18.5-24.9: Normal
- 25-29.9: Overweight
- 30+: Obese

```python
# Your code here
```

### Exercise 6: Triangle Validator
Check if three sides can form a valid triangle.
A triangle is valid if:
- All sides are positive
- Sum of any two sides > third side

```python
# Your code here
```

## Key Concepts to Remember

- **Comparison operators**: ==, !=, <, >, <=, >=
- **Boolean operators**: and, or, not
- **and** requires ALL conditions to be True
- **or** requires AT LEAST ONE condition to be True
- **not** inverts the boolean value
- Use **chained comparisons** for range checks: `0 <= x <= 100`
- **Indentation** is crucial - all code in the if block must be indented
- **elif** is checked only if previous conditions are False
- **else** executes when all conditions are False

## Common Mistakes to Avoid

1. Using `=` instead of `==` for comparison
2. Forgetting the colon `:` after if/elif/else
3. Incorrect indentation
4. Confusing `and` and `or` logic
5. Not considering all possible cases
6. Unnecessary nested ifs that could be combined with `and`/`or`
7. Not validating input ranges

## Extension Challenge

Create a "School Attendance Monitor" that:
1. Asks for student name
2. Asks for number of days present (out of 190)
3. Asks for number of late arrivals
4. Calculates attendance percentage
5. Provides feedback:
   - 95%+: Excellent attendance
   - 90-94.9%: Good attendance
   - 85-89.9%: Satisfactory attendance (warning if late > 5)
   - Below 85%: Poor attendance (requires meeting)
6. If late arrivals > 10: Additional warning message

```python
# Your code here
```

## Truth Tables Reference

### AND Truth Table
| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

### OR Truth Table
| A     | B     | A or B  |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |

### NOT Truth Table
| A     | not A |
|-------|-------|
| True  | False |
| False | True  |

# Week 6: Functions - Parameters, Return, Decomposition, and Testing

## Learning Objectives
- Define and call functions
- Use parameters and arguments effectively
- Return values from functions
- Apply problem decomposition
- Write basic function tests
- Understand scope and documentation

## 1. Function Basics

### Defining and Calling Functions
```python
# Function with no parameters
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!

# Function with parameter
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!
```

### Why Use Functions?
- **Reusability**: Write once, use many times
- **Organization**: Break complex problems into smaller parts
- **Maintainability**: Easier to update and fix
- **Readability**: Makes code easier to understand

## 2. Parameters and Arguments

### Single Parameter
```python
def square(number):
    result = number ** 2
    print(f"The square of {number} is {result}")

square(5)   # The square of 5 is 25
square(10)  # The square of 10 is 100
```

### Multiple Parameters
```python
def calculate_area(length, width):
    area = length * width
    print(f"Area: {area}")

calculate_area(5, 3)   # Area: 15
calculate_area(10, 7)  # Area: 70
```

### Default Parameters
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Charlie", "Good morning")  # Good morning, Charlie!
```

### Keyword Arguments
```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

# Positional arguments
describe_person("Alice", 16, "London")

# Keyword arguments (order doesn't matter)
describe_person(age=16, city="London", name="Alice")
describe_person(name="Bob", city="Manchester", age=17)
```

## 3. Return Values

### Basic Return
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Use directly in expressions
total = add(10, 20) + add(5, 15)
print(total)  # 50
```

### Return vs Print
```python
# Function that prints (can't be used in expressions)
def print_square(n):
    print(n ** 2)

# Function that returns (can be used anywhere)
def calculate_square(n):
    return n ** 2

# This works
result = calculate_square(5) + calculate_square(3)
print(result)  # 34

# This doesn't work well
result = print_square(5) + print_square(3)  # Prints 25 and 9, then error
```

### Returning Multiple Values
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

# Unpack return values
minimum, maximum = get_min_max([23, 45, 12, 67, 34])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 12, Max: 67

def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average

sum_val, count_val, avg_val = calculate_stats([10, 20, 30, 40])
print(f"Sum: {sum_val}, Count: {count_val}, Average: {avg_val}")
```

### Early Return
```python
def is_valid_age(age):
    if age < 0 or age > 120:
        return False
    return True

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
```

## 4. Function Documentation

### Docstrings
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)
```

### Comments in Functions
```python
def calculate_grade(score):
    """Convert a numeric score to a letter grade."""
    
    # Validate input
    if score < 0 or score > 100:
        return "Invalid"
    
    # Determine grade based on score
    if score >= 90:
        return "A*"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
```

## 5. Problem Decomposition

### Breaking Down Complex Problems
```python
# Bad: Everything in one place
score = int(input("Enter score: "))
if score >= 90:
    print("Grade: A*")
elif score >= 80:
    print("Grade: A")
# ... more code ...

# Good: Decomposed into functions
def get_score():
    """Get and validate score from user."""
    while True:
        score = int(input("Enter score (0-100): "))
        if 0 <= score <= 100:
            return score
        print("Invalid score. Try again.")

def calculate_grade(score):
    """Convert score to letter grade."""
    if score >= 90:
        return "A*"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def main():
    """Main program."""
    score = get_score()
    grade = calculate_grade(score)
    print(f"Grade: {grade}")

main()
```

### Example: Student Management System
```python
def add_student(students, name, score):
    """Add a student to the list."""
    students.append({"name": name, "score": score})

def calculate_average(students):
    """Calculate average score of all students."""
    if len(students) == 0:
        return 0
    total = sum(student["score"] for student in students)
    return total / len(students)

def find_top_student(students):
    """Find student with highest score."""
    if len(students) == 0:
        return None
    
    top = students[0]
    for student in students:
        if student["score"] > top["score"]:
            top = student
    return top

def display_students(students):
    """Display all students with their scores."""
    for student in students:
        print(f"{student['name']}: {student['score']}")

# Main program
students = []
add_student(students, "Alice", 85)
add_student(students, "Bob", 92)
add_student(students, "Charlie", 78)

print("All Students:")
display_students(students)
print(f"\nAverage: {calculate_average(students):.1f}")
print(f"Top Student: {find_top_student(students)['name']}")
```

## 6. Scope

### Local vs Global Variables
```python
# Global variable
name = "Global"

def function1():
    # Local variable (only exists in this function)
    name = "Local"
    print(name)  # Local

function1()  # Output: Local
print(name)  # Output: Global

# Function parameters are local variables
def greet(name):
    print(name)  # Uses parameter (local)

name = "Alice"
greet("Bob")  # Output: Bob
print(name)    # Output: Alice
```

### Modifying Global Variables
```python
# Bad practice - avoid if possible
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1

# Better approach - use parameters and return
def increment(counter):
    return counter + 1

counter = 0
counter = increment(counter)
print(counter)  # 1
```

## 7. Basic Testing

### Manual Testing
```python
def add(a, b):
    """Add two numbers."""
    return a + b

# Test cases
print("Test 1:", add(2, 3) == 5)        # Should be True
print("Test 2:", add(-1, 1) == 0)       # Should be True
print("Test 3:", add(0, 0) == 0)        # Should be True
print("Test 4:", add(100, 200) == 300)  # Should be True
```

### Test Function Pattern
```python
def is_even(n):
    """Check if number is even."""
    return n % 2 == 0

def test_is_even():
    """Test the is_even function."""
    assert is_even(4) == True, "4 should be even"
    assert is_even(7) == False, "7 should be odd"
    assert is_even(0) == True, "0 should be even"
    assert is_even(-2) == True, "-2 should be even"
    print("All tests passed!")

test_is_even()
```

### Testing with Different Inputs
```python
def calculate_grade(score):
    """Convert score to grade."""
    if score >= 90:
        return "A*"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"

def test_calculate_grade():
    """Test grade calculation."""
    # Boundary tests
    assert calculate_grade(90) == "A*", "90 should be A*"
    assert calculate_grade(89) == "A", "89 should be A"
    assert calculate_grade(80) == "A", "80 should be A"
    assert calculate_grade(79) == "B", "79 should be B"
    assert calculate_grade(70) == "B", "70 should be B"
    assert calculate_grade(69) == "C", "69 should be C"
    
    # Extreme values
    assert calculate_grade(100) == "A*", "100 should be A*"
    assert calculate_grade(0) == "C", "0 should be C"
    
    print("All grade tests passed!")

test_calculate_grade()
```

## Practice Exercises

### Exercise 1: Temperature Converter
Write functions to:
1. Convert Celsius to Fahrenheit
2. Convert Fahrenheit to Celsius
3. Test both functions with known values

```python
# Your code here
```

### Exercise 2: Circle Calculator
Create functions for a circle:
1. calculate_area(radius) - returns area
2. calculate_circumference(radius) - returns circumference
3. display_circle_info(radius) - displays both
Use π = 3.14159

```python
# Your code here
```

### Exercise 3: List Statistics
Write functions that take a list of numbers:
1. find_max(numbers) - return maximum
2. find_min(numbers) - return minimum
3. calculate_average(numbers) - return average
4. count_above_average(numbers) - return count
Don't use built-in max() or min()

```python
# Your code here
```

### Exercise 4: Password Validator
Create a password validation system:
1. has_digit(password) - check for digit
2. has_uppercase(password) - check for uppercase
3. is_long_enough(password) - check length >= 8
4. is_valid_password(password) - check all criteria
5. Test all functions

```python
# Your code here
```

### Exercise 5: Grade System
Build a complete grade system:
1. get_score() - input with validation
2. calculate_grade(score) - return letter grade
3. get_grade_points(grade) - A*=5, A=4, B=3, C=2, D=1, F=0
4. main() - orchestrate the program
5. Write tests for calculate_grade()

```python
# Your code here
```

### Exercise 6: Shopping Cart
Create shopping cart functions:
1. add_item(cart, item, price) - add to cart
2. calculate_total(cart) - return total
3. apply_discount(total, percentage) - apply discount
4. calculate_tax(total, rate) - calculate tax
5. display_receipt(cart, total, tax, final) - show receipt

```python
# Your code here
```

### Exercise 7: Palindrome Checker
Write and test:
1. reverse_string(text) - return reversed string
2. is_palindrome(text) - check if palindrome
3. test_palindrome() - test with multiple cases

```python
# Your code here
```

### Exercise 8: Number Analyzer
Create functions to analyze a number:
1. is_prime(n) - check if prime
2. get_factors(n) - return list of factors
3. sum_of_digits(n) - sum all digits
4. is_perfect_square(n) - check if perfect square
Test all functions

```python
# Your code here
```

## Key Concepts to Remember

- **def**: Keyword to define a function
- **Parameters**: Variables in function definition
- **Arguments**: Values passed when calling function
- **return**: Send value back to caller
- **Docstrings**: Documentation in triple quotes
- **Scope**: Where variables can be accessed
- **Decomposition**: Breaking problems into smaller functions
- **Testing**: Verify functions work correctly
- **DRY**: Don't Repeat Yourself - use functions

## Function Design Principles

1. **Single Responsibility**: Each function should do one thing well
2. **Clear Names**: Use descriptive function names
3. **Small Functions**: Keep functions short and focused
4. **Avoid Side Effects**: Functions shouldn't modify global state
5. **Return Values**: Prefer return over print for flexibility
6. **Document**: Use docstrings and comments
7. **Test**: Write tests for your functions

## Common Mistakes to Avoid

1. Forgetting to call function with ()
2. Not returning a value when you need one
3. Using print instead of return
4. Modifying global variables inside functions
5. Not testing edge cases
6. Functions that are too long or do too much
7. Poor naming (use verbs for functions)
8. Forgetting that parameters are local variables

## Extension Challenge

Create a "Student Grade Management System" with these functions:

**Data Management:**
1. add_student(students, name, scores)
2. remove_student(students, name)
3. find_student(students, name)

**Calculations:**
4. calculate_student_average(scores)
5. calculate_class_average(students)
6. get_letter_grade(score)

**Analysis:**
7. find_top_student(students)
8. count_by_grade(students)
9. get_students_above(students, threshold)

**Display:**
10. display_student(student)
11. display_all_students(students)
12. display_statistics(students)

**Testing:**
13. test_all_functions()

**Main Program:**
14. main() - menu system to use all functions

```python
# Your code here
```

## Testing Checklist

When testing functions, check:
- ✓ Normal inputs (typical values)
- ✓ Boundary values (minimum, maximum)
- ✓ Edge cases (zero, negative, empty)
- ✓ Invalid inputs (wrong type, out of range)
- ✓ Multiple scenarios

# Week 1: I/O, Variables, Types, Casting, Arithmetic, and Formatting

## Learning Objectives
- Understand basic input and output operations
- Work with variables and data types
- Perform type casting between different data types
- Use arithmetic operators effectively
- Format output for better readability

## 1. Input and Output

### Output with print()
```python
print("Hello, World!")
print("Welcome to Python Programming")

# Multiple values
print("Name:", "Alice", "Age:", 16)

# Using sep parameter
print("Python", "is", "fun", sep="-")

# Using end parameter
print("Python", end="\n\n")
print("is", end="\n\n")
print("fun", end="\n\n")
```

### Input from User
```python
name = input("Enter your name: ")
print("Hello,", name)

# Input always returns a string
age = input("Enter your age: ")
print("Your age is", age)
```

## 2. Variables and Data Types

### Basic Data Types
```python
# Integer
age = 16
score = 95

# Float
height = 1.65
temperature = 23.5

# String
name = "Alice"
school = 'Python Academy'

# Boolean
is_student = True
has_passed = False
```

### Checking Types
```python
age = 16
print(type(age))  # <class 'int'>

height = 1.65
print(type(height))  # <class 'float'>

name = "Alice"
print(type(name))  # <class 'str'>

is_student = True
print(type(is_student))  # <class 'bool'>
```

## 3. Type Casting

### Converting Between Types
```python
# String to Integer
age_str = "16"
age = int(age_str)
print(age + 1)  # 17

# String to Float
height_str = "1.65"
height = float(height_str)
print(height + 0.05)  # 1.7

# Integer to String
score = 95
score_str = str(score)
print("Your score is " + score_str)

# Float to Integer (truncates decimal)
price = 19.99
whole_price = int(price)
print(whole_price)  # 19
```

### Input with Type Casting
```python
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print("In 5 years, you'll be", age + 5)
```

## 4. Arithmetic Operators

### Basic Operations
```python
# Addition
result = 10 + 5  # 15

# Subtraction
result = 10 - 5  # 5

# Multiplication
result = 10 * 5  # 50

# Division (always returns float)
result = 10 / 3  # 3.3333...

# Integer Division (floor division)
result = 10 // 3  # 3

# Modulus (remainder)
result = 10 % 3  # 1

# Exponentiation
result = 2 ** 3  # 8
```

### Order of Operations (BIDMAS/PEMDAS)
```python
result = 2 + 3 * 4  # 14 (multiplication first)
result = (2 + 3) * 4  # 20 (parentheses first)
result = 10 + 5 * 2 - 3  # 17
```

### Compound Assignment Operators
```python
score = 10
score += 5  # score = score + 5 → 15
score -= 3  # score = score - 3 → 12
score *= 2  # score = score * 2 → 24
score //= 4  # score = score // 4 → 6
```

## 5. String Formatting

### Concatenation
```python
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)  # Alice Smith
```

### Using Comma Separation
```python
name = "Alice"
age = 16
print("Name:", name, "Age:", age)
```

### F-strings (Python 3.6+)
```python
name = "Alice"
age = 16
height = 1.65

print(f"Name: {name}")
print(f"{name} is {age} years old")
print(f"Height: {height}m")

# With expressions
print(f"Next year, {name} will be {age + 1}")
```

### Format Method
```python
name = "Alice"
age = 16
print("Name: {}, Age: {}".format(name, age))
print("Age: {1}, Name: {0}".format(name, age))
```

### Formatting Numbers
```python
pi = 3.14159265359

# 2 decimal places
print(f"Pi: {pi:.2f}")  # 3.14

# 4 decimal places
print(f"Pi: {pi:.4f}")  # 3.1416

price = 19.5
print(f"Price: £{price:.2f}")  # Price: £19.50
```

## Practice Exercises

### Exercise 1: Personal Details
Write a program that:
1. Asks for name, age, and height
2. Calculates age in 10 years
3. Displays all information formatted nicely

```python
# Your code here
```

### Exercise 2: Simple Calculator
Create a calculator that:
1. Asks for two numbers
2. Performs addition, subtraction, multiplication, and division
3. Displays results with 2 decimal places

```python
# Your code here
```

### Exercise 3: Price Calculator
Write a program that:
1. Asks for item price and quantity
2. Calculates total cost
3. Calculates change from £50
4. Displays all values as currency (£X.XX)

```python
# Your code here
```

### Exercise 4: Temperature Converter
Create a program that:
1. Asks for temperature in Celsius
2. Converts to Fahrenheit (F = C * 9/5 + 32)
3. Displays both temperatures with 1 decimal place

```python
# Your code here
```

### Exercise 5: Circle Calculator
Write a program that:
1. Asks for circle radius
2. Calculates area (π * r²)
3. Calculates circumference (2 * π * r)
4. Displays results with 2 decimal places
(Use 3.14159 for π)

```python
# Your code here
```

## Key Concepts to Remember

- **input()** always returns a string - use type casting for numbers
- **int()** converts to integer, **float()** converts to decimal
- **Division (/)** always returns a float, use **//** for integer division
- **Modulus (%)** gives the remainder of division
- **F-strings** are the modern way to format strings in Python
- Always format currency and measurements appropriately

## Common Mistakes to Avoid

1. Forgetting to cast input to int/float
2. Using + with string and number without conversion
3. Integer division when you need decimal results
4. Not considering order of operations in calculations
5. Forgetting to format decimal places for money

## Extension Challenge

Create a "Receipt Generator" that:
1. Asks for 3 item names and prices
2. Calculates subtotal
3. Adds 20% VAT
4. Displays a formatted receipt with:
   - Each item and price
   - Subtotal
   - VAT amount
   - Total
   - All prices formatted as £X.XX

```python
# Your code here
```

# Week 3: For/While Loops, Counters/Totals, Sentinel Loops, and Break

## Learning Objectives
- Use for loops to iterate over ranges and sequences
- Use while loops for condition-based repetition
- Implement counters and running totals
- Understand and use sentinel values
- Control loop flow with break and continue

## 1. For Loops

### Basic For Loop with Range
```python
# Print numbers 0 to 4
for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4
```

### Range with Start and Stop
```python
# Print numbers 1 to 5
for i in range(1, 6):
    print(i)

# Output: 1, 2, 3, 4, 5
```

### Range with Step
```python
# Even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)

# Output: 0, 2, 4, 6, 8, 10

# Count down from 10 to 1
for i in range(10, 0, -1):
    print(i)

# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### Practical For Loop Examples
```python
# Times table
number = 7
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")

# Sum of first 10 numbers
total = 0
for i in range(1, 11):
    total += i
print(f"Sum: {total}")  # 55
```

## 2. While Loops

### Basic While Loop
```python
count = 1
while count <= 5:
    print(count)
    count += 1

# Output: 1, 2, 3, 4, 5
```

### While Loop with Input
```python
password = ""
while password != "python":
    password = input("Enter password: ")
print("Access granted!")
```

### Countdown Example
```python
time = 10
while time > 0:
    print(f"{time} seconds remaining")
    time -= 1
print("Time's up!")
```

## 3. Counters and Running Totals

### Counter Pattern
```python
# Count how many numbers are positive
count = 0
for i in range(5):
    number = int(input("Enter a number: "))
    if number > 0:
        count += 1

print(f"Positive numbers: {count}")
```

### Running Total Pattern
```python
# Calculate total of numbers entered
total = 0
for i in range(5):
    number = int(input("Enter a number: "))
    total += number

print(f"Total: {total}")
```

### Counter and Total Combined
```python
# Count and sum positive numbers only
count = 0
total = 0

for i in range(5):
    number = int(input("Enter a number: "))
    if number > 0:
        count += 1
        total += number

if count > 0:
    average = total / count
    print(f"Positive numbers: {count}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
else:
    print("No positive numbers entered")
```

## 4. Sentinel Values

### Sentinel Loop Pattern
A sentinel value signals the end of input (e.g., -1, "quit", 0)

```python
# Using -1 as sentinel
total = 0
count = 0

number = int(input("Enter a number (-1 to stop): "))
while number != -1:
    total += number
    count += 1
    number = int(input("Enter a number (-1 to stop): "))

if count > 0:
    print(f"Total: {total}")
    print(f"Average: {total / count:.2f}")
```

### String Sentinel Example
```python
# Using "quit" as sentinel
total_price = 0
item_count = 0

item = input("Enter item price (or 'quit' to finish): ")
while item.lower() != "quit":
    price = float(item)
    total_price += price
    item_count += 1
    item = input("Enter item price (or 'quit' to finish): ")

print(f"Items: {item_count}")
print(f"Total: £{total_price:.2f}")
```

### Validation with Sentinel
```python
# Keep asking until valid input or quit
age = input("Enter age (or 'quit'): ")
while age.lower() != "quit":
    age_num = int(age)
    if 0 <= age_num <= 120:
        print(f"Age {age_num} is valid")
        break
    else:
        print("Invalid age!")
        age = input("Enter age (or 'quit'): ")
```

## 5. Break and Continue

### Break Statement
Exits the loop immediately
```python
# Find first number divisible by 7
for i in range(1, 100):
    if i % 7 == 0:
        print(f"First number divisible by 7: {i}")
        break

# Search for a value
target = 42
found = False

for i in range(1, 101):
    if i == target:
        print(f"Found {target}!")
        found = True
        break

if not found:
    print(f"{target} not found")
```

### Continue Statement
Skips the rest of the current iteration
```python
# Print odd numbers only
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# Output: 1, 3, 5, 7, 9
```

### Break with While Loop
```python
# Login with maximum attempts
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == "secret":
        print("Login successful!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining")
        else:
            print("Account locked!")
```

## 6. Nested Loops

### Basic Nested Loop
```python
# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # New line after each row
```

### Pattern Printing
```python
# Right triangle of stars
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****
```

## Practice Exercises

### Exercise 1: Times Table Generator
Write a program that:
1. Asks for a number
2. Displays the times table from 1 to 12
3. Example: 7 x 1 = 7, 7 x 2 = 14, ...

```python
# Your code here
```

### Exercise 2: Number Guessing Game
Create a game where:
1. Computer picks a number from 1-100
2. Player has 7 attempts to guess
3. After each guess, tell if too high/low
4. Display "You win!" or "You lose!" at the end

```python
import random
target = random.randint(1, 100)
# Your code here
```

### Exercise 3: Average Calculator with Sentinel
Write a program that:
1. Asks for test scores (0-100)
2. Uses -1 as sentinel to stop
3. Validates each score is in range
4. Calculates and displays average
5. Shows how many scores were entered

```python
# Your code here
```

### Exercise 4: Prime Number Checker
Check if a number is prime:
1. Ask for a number
2. Test if it's divisible by any number from 2 to n-1
3. Use break to exit early if divisible
4. Display "Prime" or "Not Prime"

```python
# Your code here
```

### Exercise 5: Shopping Cart Total
Create a shopping cart calculator:
1. Ask for item prices (use 0 to finish)
2. Keep running total
3. Count number of items
4. Display:
   - Number of items
   - Subtotal
   - VAT (20%)
   - Total

```python
# Your code here
```

### Exercise 6: Factorial Calculator
Calculate factorial using a loop:
1. Ask for a number n
2. Calculate n! = n × (n-1) × (n-2) × ... × 1
3. Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

```python
# Your code here
```

### Exercise 7: Password Strength Checker
Check password strength with a loop:
1. Keep asking for password until it meets all criteria:
   - At least 8 characters
   - Contains a digit
   - Contains uppercase letter
2. Give feedback on what's missing
3. Maximum 5 attempts

```python
# Your code here
```

### Exercise 8: Pattern Printer
Print this pattern using nested loops:
```
1
22
333
4444
55555
```

```python
# Your code here
```

## Key Concepts to Remember

- **for loop**: Use when you know how many iterations needed
- **while loop**: Use when iterations depend on a condition
- **range(stop)**: 0 to stop-1
- **range(start, stop)**: start to stop-1
- **range(start, stop, step)**: start to stop-1, incrementing by step
- **Counters**: Start at 0, increment with += 1
- **Running totals**: Start at 0, add with += value
- **Sentinel value**: Special value to signal end of input
- **break**: Exit loop immediately
- **continue**: Skip to next iteration
- **Nested loops**: Loop inside another loop

## Common Mistakes to Avoid

1. Forgetting to increment counter in while loop (infinite loop)
2. Off-by-one errors in range (remember it's exclusive)
3. Not initializing counters/totals before loop
4. Using `=` instead of `==` in while conditions
5. Forgetting to handle case when no values are entered (division by zero)
6. Infinite loops - always ensure loop condition can become False
7. Not indenting loop body correctly

## Loop Control Flow Diagram

```
for loop:
    Start → Check if more items → Execute body → Next item → Check if more items → End

while loop:
    Start → Check condition → Execute body → Check condition → End

break:
    Execute loop → Condition met → break → Exit loop immediately

continue:
    Execute loop → Condition met → continue → Skip rest, next iteration
```

## Extension Challenge

Create a "Class Grade Analyzer" that:
1. Asks for number of students
2. For each student:
   - Ask for name
   - Ask for score (validate 0-100)
3. Calculate and display:
   - Class average
   - Highest score and student name
   - Lowest score and student name
   - Number of students passing (50+)
   - Pass rate percentage
4. Use appropriate loops, counters, and totals

```python
# Your code here
```

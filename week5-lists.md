# Week 5: Lists - Create, Update, Methods, Traverse, Max/Min/Average

## Learning Objectives
- Create and initialize lists
- Access and modify list elements
- Use list methods effectively
- Traverse lists with loops
- Calculate statistics (max, min, average, sum)
- Work with 2D lists

## 1. Creating Lists

### Empty and Simple Lists
```python
# Empty list
empty = []

# List with values
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "Hello", 3.14, True]
```

### Creating Lists with Patterns
```python
# Using range
numbers = list(range(5))          # [0, 1, 2, 3, 4]
numbers = list(range(1, 11))      # [1, 2, 3, ..., 10]
numbers = list(range(0, 11, 2))   # [0, 2, 4, 6, 8, 10]

# List of zeros
zeros = [0] * 5                   # [0, 0, 0, 0, 0]

# List of same value
scores = [100] * 3                # [100, 100, 100]
```

### Creating Lists with Input
```python
# Fixed number of inputs
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Using list comprehension (advanced)
numbers = [int(input("Enter number: ")) for i in range(5)]
```

## 2. Accessing List Elements

### Indexing
```python
fruits = ["apple", "banana", "cherry", "date"]

# Positive indexing
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[3])   # date

# Negative indexing
print(fruits[-1])  # date (last)
print(fruits[-2])  # cherry (second from end)
```

### Slicing
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[0:5])    # [0, 1, 2, 3, 4]
print(numbers[5:])     # [5, 6, 7, 8, 9]
print(numbers[:5])     # [0, 1, 2, 3, 4]
print(numbers[-3:])    # [7, 8, 9]
print(numbers[::2])    # [0, 2, 4, 6, 8]
print(numbers[::-1])   # [9, 8, 7, ..., 0] (reversed)
```

## 3. Modifying Lists

### Changing Elements
```python
fruits = ["apple", "banana", "cherry"]

# Change single element
fruits[1] = "blueberry"
print(fruits)  # ["apple", "blueberry", "cherry"]

# Change last element
fruits[-1] = "date"
print(fruits)  # ["apple", "blueberry", "date"]
```

### Adding Elements
```python
# append() - add to end
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]

# insert() - add at specific position
fruits.insert(1, "blueberry")
print(fruits)  # ["apple", "blueberry", "banana", "cherry"]

# extend() - add multiple elements
fruits.extend(["date", "elderberry"])
print(fruits)  # ["apple", ..., "date", "elderberry"]
```

### Removing Elements
```python
fruits = ["apple", "banana", "cherry", "banana"]

# remove() - remove first occurrence
fruits.remove("banana")
print(fruits)  # ["apple", "cherry", "banana"]

# pop() - remove and return last element
last = fruits.pop()
print(last)    # "banana"
print(fruits)  # ["apple", "cherry"]

# pop(index) - remove at specific position
first = fruits.pop(0)
print(first)   # "apple"
print(fruits)  # ["cherry"]

# clear() - remove all elements
fruits.clear()
print(fruits)  # []
```

## 4. List Methods

### Essential Methods
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - sort in place
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# reverse() - reverse in place
numbers.reverse()
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# count() - count occurrences
print(numbers.count(1))  # 2

# index() - find first occurrence position
print(numbers.index(5))  # 2

# copy() - create a copy
numbers_copy = numbers.copy()
```

### Sorting Examples
```python
# Ascending order
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # [1, 2, 5, 8, 9]

# Descending order
numbers.sort(reverse=True)
print(numbers)  # [9, 8, 5, 2, 1]

# Alphabetical
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(names)  # ["Alice", "Bob", "Charlie"]
```

## 5. Traversing Lists

### Using For Loop
```python
numbers = [10, 20, 30, 40, 50]

# Iterate through values
for num in numbers:
    print(num)

# Iterate with index
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

# Using enumerate()
for index, value in enumerate(numbers):
    print(f"Index {index}: {value}")
```

### Common Traversal Patterns
```python
# Sum all elements
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")  # 150

# Count specific values
scores = [85, 90, 75, 90, 88, 90]
count = 0
for score in scores:
    if score == 90:
        count += 1
print(f"Count of 90s: {count}")  # 3

# Find values meeting condition
ages = [15, 17, 16, 18, 14, 19]
adults = 0
for age in ages:
    if age >= 18:
        adults += 1
print(f"Adults: {adults}")  # 2
```

## 6. Built-in Functions for Lists

### Statistical Functions
```python
numbers = [23, 45, 12, 67, 34, 89, 15]

# Sum
total = sum(numbers)
print(f"Sum: {total}")  # 285

# Length
count = len(numbers)
print(f"Count: {count}")  # 7

# Maximum
highest = max(numbers)
print(f"Max: {highest}")  # 89

# Minimum
lowest = min(numbers)
print(f"Min: {lowest}")  # 12

# Average
average = sum(numbers) / len(numbers)
print(f"Average: {average:.2f}")  # 40.71
```

### Checking Membership
```python
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list")

if "orange" not in fruits:
    print("Orange is not in the list")
```

## 7. List Operations

### Combining Lists
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation with +
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Repetition with *
repeated = list1 * 3
print(repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## 8. Common List Algorithms

### Linear Search
```python
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # Return index if found
    return -1  # Not found

numbers = [10, 20, 30, 40, 50]
position = linear_search(numbers, 30)
print(position)  # 2
```

### Find Maximum with Position
```python
scores = [85, 92, 78, 95, 88]

max_score = scores[0]
max_index = 0

for i in range(1, len(scores)):
    if scores[i] > max_score:
        max_score = scores[i]
        max_index = i

print(f"Highest score: {max_score} at position {max_index}")
```

### Filter List
```python
# Get all values above threshold
numbers = [45, 23, 67, 12, 89, 34, 15, 78]
threshold = 50

above_threshold = []
for num in numbers:
    if num > threshold:
        above_threshold.append(num)

print(above_threshold)  # [67, 89, 78]
```

## 9. Working with 2D Lists

### Creating 2D Lists
```python
# 3x3 grid of zeros
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

# Student grades [name, math, english, science]
students = [
    ["Alice", 85, 90, 88],
    ["Bob", 78, 82, 80],
    ["Charlie", 92, 88, 95]
]
```

### Accessing 2D Lists
```python
students = [
    ["Alice", 85, 90, 88],
    ["Bob", 78, 82, 80]
]

# Access row
print(students[0])  # ["Alice", 85, 90, 88]

# Access element
print(students[0][0])  # Alice
print(students[0][1])  # 85 (Alice's math score)
```

### Traversing 2D Lists
```python
students = [
    ["Alice", 85, 90, 88],
    ["Bob", 78, 82, 80],
    ["Charlie", 92, 88, 95]
]

# Print all students with averages
for student in students:
    name = student[0]
    scores = student[1:]
    average = sum(scores) / len(scores)
    print(f"{name}: {average:.1f}")
```

## Practice Exercises

### Exercise 1: Grade Statistics
Write a program that:
1. Creates a list of 5 test scores (input from user)
2. Calculates and displays:
   - Highest score
   - Lowest score
   - Average score
   - Number of scores above average

```python
# Your code here
```

### Exercise 2: List Operations Menu
Create a menu system that allows:
1. Add a number to list
2. Remove a number from list
3. Display the list
4. Display list statistics (sum, average, min, max)
5. Exit

```python
# Your code here
```

### Exercise 3: Shopping List Manager
Create a shopping list program:
1. Add items to list
2. Remove items from list
3. Display list with numbers
4. Clear entire list
5. Search for an item
Use a menu system

```python
# Your code here
```

### Exercise 4: Top Scores
Write a program that:
1. Asks for 10 game scores
2. Displays the top 3 scores
3. Shows the average of the top 3

```python
# Your code here
```

### Exercise 5: Remove Duplicates
Create a program that:
1. Creates a list of numbers (including duplicates)
2. Removes all duplicates
3. Displays the unique numbers in sorted order

```python
# Your code here
```

### Exercise 6: Temperature Tracker
Track weekly temperatures:
1. Input 7 daily temperatures
2. Display:
   - Highest temperature and day
   - Lowest temperature and day
   - Average temperature
   - Days above average

```python
# Your code here
```

### Exercise 7: Student Grade Manager
Create a student management system:
1. Store students as [name, math, english, science]
2. Calculate average for each student
3. Find student with highest average
4. Display all students with grades

```python
# Your code here
```

### Exercise 8: List Reversal
Write a program that reverses a list WITHOUT using reverse() or slicing:
1. Ask for numbers to add to list
2. Manually reverse the list using a loop
3. Display original and reversed list

```python
# Your code here
```

## Key Concepts to Remember

- **Lists are mutable**: Can be changed after creation
- **Indexing**: Starts at 0, negative indices from end
- **append()**: Add single element to end
- **remove()**: Remove first occurrence of value
- **pop()**: Remove and return element
- **sort()**: Sorts list in place
- **len()**: Returns number of elements
- **sum()**: Returns sum of all numbers
- **max()/min()**: Returns highest/lowest value
- **in**: Check if value exists in list
- **for item in list**: Iterate through values
- **for i in range(len(list))**: Iterate with indices

## Common List Methods Quick Reference

```python
numbers = [3, 1, 4, 1, 5]

numbers.append(9)      # Add to end
numbers.insert(0, 2)   # Insert at position
numbers.remove(1)      # Remove first occurrence
numbers.pop()          # Remove and return last
numbers.pop(0)         # Remove at index
numbers.sort()         # Sort ascending
numbers.reverse()      # Reverse order
numbers.count(1)       # Count occurrences
numbers.index(4)       # Find position
numbers.clear()        # Remove all elements
numbers.copy()         # Create a copy
```

## Common Mistakes to Avoid

1. Index out of range (accessing index >= length)
2. Modifying list while iterating over it
3. Forgetting that sort() and reverse() modify in place
4. Using = to copy (creates reference, not copy - use copy())
5. Confusing append() with extend()
6. Not checking if list is empty before finding max/min
7. Off-by-one errors when using indices

## Extension Challenge

Create a "Exam Results Analyzer" that:
1. Stores data for multiple students: [name, [scores]]
2. Each student has 5 exam scores
3. Calculate and display for each student:
   - Average score
   - Best score
   - Worst score
   - Grade (A*: 90+, A: 80-89, B: 70-79, C: 60-69, D: 50-59, F: <50)
4. Display overall statistics:
   - Class average
   - Highest scoring student
   - Number of students per grade
5. Allow sorting by: name, average score, or best score

```python
# Your code here
```

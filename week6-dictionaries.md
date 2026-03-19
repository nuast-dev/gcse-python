# Week 6: Dictionaries - Create, Access, Update, Methods, and Traversal

## Learning Objectives
- Create and initialise dictionaries
- Access and modify dictionary values
- Use dictionary methods effectively
- Traverse dictionaries with loops
- Work with nested dictionaries

## 1. Creating Dictionaries

### Empty and Simple Dictionaries
```python
# Empty dictionary
empty = {}

# Dictionary with values
person = {"name": "Alice", "age": 16, "city": "London"}

# Alternative using dict()
person = dict(name="Alice", age=16, city="London")
```

### Dictionaries with Different Value Types
```python
student = {
    "name": "Bob",
    "age": 17,
    "scores": [85, 90, 78],
    "passed": True,
    "average": 84.3
}
```

## 2. Accessing Dictionary Values

### Using Keys
```python
person = {"name": "Alice", "age": 16, "city": "London"}

# Access by key
print(person["name"])   # Alice
print(person["age"])    # 16

# Using get() - safer (returns None if key missing)
print(person.get("name"))         # Alice
print(person.get("email"))        # None
print(person.get("email", "N/A")) # N/A (default value)
```

### Checking for Keys
```python
person = {"name": "Alice", "age": 16}

if "name" in person:
    print("Name exists:", person["name"])

if "email" not in person:
    print("No email stored")
```

## 3. Modifying Dictionaries

### Adding and Updating Values
```python
person = {"name": "Alice", "age": 16}

# Add new key-value pair
person["city"] = "London"
print(person)  # {"name": "Alice", "age": 16, "city": "London"}

# Update existing value
person["age"] = 17
print(person)  # {"name": "Alice", "age": 17, "city": "London"}
```

### Removing Values
```python
person = {"name": "Alice", "age": 16, "city": "London"}

# del - remove by key
del person["city"]
print(person)  # {"name": "Alice", "age": 16}

# pop() - remove and return value
age = person.pop("age")
print(age)     # 16
print(person)  # {"name": "Alice"}

# clear() - remove all items
person.clear()
print(person)  # {}
```

## 4. Dictionary Methods

### Essential Methods
```python
student = {"name": "Alice", "age": 16, "grade": "A"}

# keys() - all keys
print(student.keys())    # dict_keys(["name", "age", "grade"])

# values() - all values
print(student.values())  # dict_values(["Alice", 16, "A"])

# items() - all key-value pairs
print(student.items())   # dict_items([("name", "Alice"), ...])
```

### Updating with Another Dictionary
```python
person = {"name": "Alice", "age": 16}
extra = {"city": "London", "age": 17}

# update() - merge dictionaries (overwrites duplicates)
person.update(extra)
print(person)  # {"name": "Alice", "age": 17, "city": "London"}
```

### Copying a Dictionary
```python
original = {"name": "Alice", "age": 16}

# copy() - create a shallow copy
copy = original.copy()
copy["name"] = "Bob"

print(original["name"])  # Alice (unchanged)
print(copy["name"])      # Bob
```

## 5. Traversing Dictionaries

### Iterating Over Keys
```python
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

for name in scores:
    print(name)

# Same as:
for name in scores.keys():
    print(name)
```

### Iterating Over Values
```python
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

for score in scores.values():
    print(score)
```

### Iterating Over Key-Value Pairs
```python
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

for name, score in scores.items():
    print(f"{name}: {score}")
```

### Common Traversal Patterns
```python
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 90}

# Find highest scorer
top_name = None
top_score = -1
for name, score in scores.items():
    if score > top_score:
        top_score = score
        top_name = name
print(f"Top scorer: {top_name} with {top_score}")

# Count students who passed (>=70)
passed = 0
for score in scores.values():
    if score >= 70:
        passed += 1
print(f"Passed: {passed}")

# Calculate class average
total = sum(scores.values())
average = total / len(scores)
print(f"Average: {average:.1f}")
```

## 6. Nested Dictionaries

### Creating Nested Dictionaries
```python
# Student with multiple pieces of information
student = {
    "name": "Alice",
    "grades": {
        "maths": 85,
        "english": 90,
        "science": 88
    },
    "contact": {
        "email": "alice@example.com",
        "phone": "07700900000"
    }
}
```

### Accessing Nested Values
```python
student = {
    "name": "Alice",
    "grades": {"maths": 85, "english": 90, "science": 88}
}

# Access nested value
print(student["grades"]["maths"])    # 85
print(student["grades"]["english"])  # 90

# Using get() safely
maths = student.get("grades", {}).get("maths", 0)
print(maths)  # 85
```

### Dictionary of Dictionaries
```python
students = {
    "alice": {"age": 16, "grade": "A"},
    "bob":   {"age": 17, "grade": "B"},
    "charlie": {"age": 16, "grade": "A"}
}

# Access a student's data
print(students["alice"]["grade"])  # A

# Traverse all students
for name, info in students.items():
    print(f"{name.capitalize()}: age {info['age']}, grade {info['grade']}")
```

## 7. Dictionaries vs Lists

| Feature | List | Dictionary |
|---------|------|------------|
| Access by | Index (0, 1, 2…) | Key ("name", "age"…) |
| Order | Preserved | Preserved (Python 3.7+) |
| Duplicates | Allowed | Keys must be unique |
| Best for | Ordered sequences | Labelled data |

```python
# List: ordered data, access by position
scores = [85, 90, 78]
print(scores[0])  # 85

# Dictionary: labelled data, access by name
student = {"maths": 85, "english": 90, "science": 78}
print(student["maths"])  # 85
```

## Practice Exercises

### Exercise 1: Phonebook
Create a phonebook program:
1. Store contacts as name → phone number
2. Allow the user to add, look up, and delete contacts
3. Display all contacts in alphabetical order

```python
# Your code here
```

### Exercise 2: Word Frequency Counter
Write a program that:
1. Asks the user to enter a sentence
2. Counts how many times each word appears
3. Displays the results sorted by frequency (highest first)

```python
# Your code here
```

### Exercise 3: Student Grade Tracker
Create a grade tracker that:
1. Stores each student's name and a list of scores
2. Calculates and displays the average score for each student
3. Finds the student with the highest average

```python
# Your code here
```

### Exercise 4: Inventory System
Build a simple shop inventory:
1. Store item name → quantity and price
2. Allow adding stock, selling items, and checking stock levels
3. Display total inventory value

```python
# Your code here
```

### Exercise 5: Letter Frequency
Write a program that:
1. Takes a string from the user
2. Counts the frequency of each letter (ignore spaces, case-insensitive)
3. Displays letters and their counts

```python
# Your code here
```

### Exercise 6: Translation Dictionary
Create a simple English → French translator:
1. Store English words as keys with French translations as values
2. Ask the user to enter an English word
3. Display the translation, or a message if not found

```python
# Your code here
```

## Key Concepts to Remember

- **Dictionaries store key-value pairs**: Each key maps to a value
- **Keys must be unique**: Duplicate keys overwrite the previous value
- **Access with []**: `d["key"]` raises an error if key is missing
- **Use get()**: `d.get("key", default)` is safer — returns default if missing
- **keys()**: Returns all keys
- **values()**: Returns all values
- **items()**: Returns all key-value pairs (use with `for k, v in d.items()`)
- **del d[key]**: Remove a key-value pair
- **pop(key)**: Remove and return a value
- **in**: Check if a key exists — `"key" in d`

## Dictionary Quick Reference

```python
d = {"a": 1, "b": 2}

d["c"] = 3          # Add / update
del d["a"]          # Delete key
d.pop("b")          # Remove and return value
d.get("x", 0)       # Safe access with default
d.keys()            # All keys
d.values()          # All values
d.items()           # All key-value pairs
d.update({"d": 4})  # Merge another dict
d.copy()            # Shallow copy
d.clear()           # Remove all items
len(d)              # Number of key-value pairs
"c" in d            # Check if key exists
```

## Common Mistakes to Avoid

1. Using a key that does not exist (use `get()` or check with `in` first)
2. Confusing `keys()`, `values()`, and `items()`
3. Expecting dictionaries to behave like lists (no integer index)
4. Forgetting that keys must be immutable (strings, numbers, tuples — not lists)
5. Modifying a dictionary while iterating over it (iterate a copy instead)
6. Assuming `.copy()` deep-copies nested dictionaries (it does not)

## Extension Challenge

Create a "Student Records System" that:
1. Stores each student as a nested dictionary: name, age, and a dict of subject scores
2. Allows adding new students and updating scores
3. Calculates each student's average across all subjects
4. Finds the top student overall and the top student per subject
5. Displays a formatted report showing all students and their grades

```python
# Your code here
```

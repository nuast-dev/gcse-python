# Week 7: Files - Read/Write Text, Strip, Split, File→List Processing

## Learning Objectives
- Open and close files safely
- Read from text files
- Write to text files
- Process file data with strip() and split()
- Convert file contents to lists for processing
- Handle file errors
- Work with CSV-style data

## 1. File Basics

### Opening and Closing Files
```python
# Open file for reading
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Better approach: using with statement (automatic close)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# File automatically closed after with block
```

### File Modes
```python
"r"  # Read (default) - file must exist
"w"  # Write - creates new or overwrites existing
"a"  # Append - adds to end of file
"r+" # Read and write
```

## 2. Reading Files

### Reading Entire File
```python
# Read all content as single string
with open("story.txt", "r") as file:
    content = file.read()
    print(content)
```

### Reading Line by Line
```python
# Method 1: Using readline()
with open("data.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)

# Method 2: Using for loop (best for large files)
with open("data.txt", "r") as file:
    for line in file:
        print(line, end="")  # end="" because line includes \n

# Method 3: Read all lines into list
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Remove \n
```

### Reading into List
```python
# Read all lines into a list
with open("names.txt", "r") as file:
    names = file.readlines()

# Clean up the list (remove \n)
names = [name.strip() for name in names]
print(names)

# Or manually
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.strip())
```

## 3. Writing Files

### Writing Text
```python
# Write mode (overwrites existing file)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")

# Write multiple lines
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### Append Mode
```python
# Append to end of file
with open("log.txt", "a") as file:
    file.write("New log entry\n")

# Append multiple times
with open("log.txt", "a") as file:
    file.write("Entry 1\n")
    file.write("Entry 2\n")
    file.write("Entry 3\n")
```

### Writing from List
```python
# Write list to file
names = ["Alice", "Bob", "Charlie"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Alternative using join
with open("names.txt", "w") as file:
    file.write("\n".join(names) + "\n")
```

## 4. Processing File Data

### Using strip()
```python
# Remove whitespace and newlines
with open("data.txt", "r") as file:
    for line in file:
        clean_line = line.strip()  # Remove \n and spaces
        print(clean_line)

# Read numbers from file
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        number = int(line.strip())
        total += number
    print(f"Total: {total}")
```

### Using split()
```python
# Split comma-separated values
# File content: "Alice,16,London"
with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        name = data[0]
        age = data[1]
        city = data[2]
        print(f"{name} is {age} years old from {city}")

# Split by different separator
# File content: "apple:banana:cherry"
with open("fruits.txt", "r") as file:
    line = file.readline().strip()
    fruits = line.split(":")
    print(fruits)  # ["apple", "banana", "cherry"]
```

### Combining strip() and split()
```python
# Process CSV-style data
# File format: name,score
with open("scores.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        name = parts[0]
        score = int(parts[1])
        print(f"{name}: {score}")
```

## 5. File to List Processing

### Reading Numbers into List
```python
# File: numbers.txt (one number per line)
numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        numbers.append(number)

# Calculate statistics
print(f"Total: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
```

### Reading CSV Data into List of Lists
```python
# File: students.csv
# Format: name,age,grade
students = []

with open("students.csv", "r") as file:
    for line in file:
        data = line.strip().split(",")
        name = data[0]
        age = int(data[1])
        grade = data[2]
        students.append([name, age, grade])

# Process the data
for student in students:
    print(f"{student[0]} is {student[1]} years old, grade {student[2]}")
```

### Reading CSV into List of Dictionaries
```python
# File: students.csv
# Format: name,age,score
students = []

with open("students.csv", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        student = {
            "name": parts[0],
            "age": int(parts[1]),
            "score": int(parts[2])
        }
        students.append(student)

# Process
for student in students:
    print(f"{student['name']}: {student['score']}")

# Calculate average
avg = sum(s["score"] for s in students) / len(students)
print(f"Average score: {avg:.1f}")
```

## 6. Error Handling

### Handling File Not Found
```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found!")

# With more specific handling
filename = input("Enter filename: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: {filename} does not exist")
except Exception as e:
    print(f"Error: {e}")
```

### Checking if File Exists
```python
import os

filename = "data.txt"
if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)
else:
    print(f"{filename} does not exist")
```

## 7. Practical Examples

### Example 1: Grade Book System
```python
def save_grades(students, filename):
    """Save student grades to file."""
    with open(filename, "w") as file:
        for student in students:
            line = f"{student['name']},{student['score']}\n"
            file.write(line)

def load_grades(filename):
    """Load student grades from file."""
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                students.append({
                    "name": name,
                    "score": int(score)
                })
    except FileNotFoundError:
        print("No existing grade file found")
    return students

# Usage
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92}
]
save_grades(students, "grades.txt")

loaded = load_grades("grades.txt")
for student in loaded:
    print(f"{student['name']}: {student['score']}")
```

### Example 2: Score Statistics
```python
def analyze_scores(filename):
    """Read scores and calculate statistics."""
    scores = []
    
    with open(filename, "r") as file:
        for line in file:
            score = int(line.strip())
            scores.append(score)
    
    if len(scores) == 0:
        print("No scores found")
        return
    
    print(f"Number of scores: {len(scores)}")
    print(f"Average: {sum(scores) / len(scores):.2f}")
    print(f"Highest: {max(scores)}")
    print(f"Lowest: {min(scores)}")
    print(f"Range: {max(scores) - min(scores)}")

# Usage
analyze_scores("test_scores.txt")
```

### Example 3: Shopping List Manager
```python
def add_item(filename, item):
    """Add item to shopping list."""
    with open(filename, "a") as file:
        file.write(item + "\n")

def view_list(filename):
    """Display shopping list."""
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            if len(items) == 0:
                print("Shopping list is empty")
            else:
                print("Shopping List:")
                for i, item in enumerate(items, 1):
                    print(f"{i}. {item.strip()}")
    except FileNotFoundError:
        print("No shopping list found")

def clear_list(filename):
    """Clear shopping list."""
    with open(filename, "w") as file:
        file.write("")

# Usage
add_item("shopping.txt", "Milk")
add_item("shopping.txt", "Bread")
add_item("shopping.txt", "Eggs")
view_list("shopping.txt")
```

## Practice Exercises

### Exercise 1: Name List Manager
Write a program that:
1. Reads names from "names.txt"
2. Displays all names
3. Allows adding new names
4. Saves back to file

```python
# Your code here
```

### Exercise 2: Number Statistics
Create a program that:
1. Reads numbers from "numbers.txt" (one per line)
2. Calculates and displays:
   - Count
   - Sum
   - Average
   - Maximum
   - Minimum
3. Writes statistics to "stats.txt"

```python
# Your code here
```

### Exercise 3: Student Grade Analyzer
Read from "students.csv" (name,score format):
1. Load all student data
2. Calculate class average
3. Find highest scoring student
4. Count students passing (score >= 50)
5. Write results to "report.txt"

```python
# Your code here
```

### Exercise 4: Log File Processor
Process a log file:
1. Read "access.log"
2. Count lines containing "ERROR"
3. Count lines containing "WARNING"
4. Write summary to "log_summary.txt"

```python
# Your code here
```

### Exercise 5: Temperature Tracker
Create temperature tracking system:
1. Read temperatures from "temps.txt"
2. Calculate average, max, min
3. Count days above average
4. Append new temperature to file
5. Display updated statistics

```python
# Your code here
```

### Exercise 6: Contact Book
Build a contact manager:
1. Load contacts from "contacts.csv" (name,phone,email)
2. Search for contact by name
3. Add new contact
4. Display all contacts
5. Save back to file

```python
# Your code here
```

### Exercise 7: Word Counter
Create word frequency counter:
1. Read text file
2. Count occurrences of each word
3. Display top 10 most common words
4. Write results to "word_counts.txt"

```python
# Your code here
```

### Exercise 8: Grade Book System
Complete grade management system:
1. Load students and scores from CSV
2. Add new student and scores
3. Update existing student scores
4. Calculate averages and grades
5. Save to file
6. Generate report file with statistics

```python
# Your code here
```

## Key Concepts to Remember

- **with statement**: Automatically closes files
- **strip()**: Remove whitespace and newlines
- **split()**: Convert string to list
- **"r" mode**: Reading (file must exist)
- **"w" mode**: Writing (overwrites file)
- **"a" mode**: Appending (adds to end)
- **readline()**: Read one line
- **readlines()**: Read all lines into list
- **for line in file**: Best for large files
- Always use **strip()** when reading lines
- Use **try/except** for file operations

## File Processing Pattern

```python
# Standard pattern for file processing
data = []

# Read and process
with open("input.txt", "r") as file:
    for line in file:
        # Clean the line
        clean_line = line.strip()
        
        # Split if needed
        parts = clean_line.split(",")
        
        # Process and store
        processed = process_data(parts)
        data.append(processed)

# Write results
with open("output.txt", "w") as file:
    for item in data:
        file.write(str(item) + "\n")
```

## Common Mistakes to Avoid

1. Not closing files (use with statement)
2. Forgetting to strip() newlines
3. Using wrong file mode
4. Not handling FileNotFoundError
5. Trying to write to file opened in read mode
6. Not converting strings to int/float when needed
7. Forgetting to add \n when writing lines
8. Overwriting files accidentally with "w" mode

## CSV File Format

```
# Simple CSV
name,age,city
Alice,16,London
Bob,17,Manchester

# Reading CSV
with open("data.csv", "r") as file:
    for line in file:
        name, age, city = line.strip().split(",")
        print(f"{name} is {age} from {city}")
```

## Extension Challenge

Create a "Student Records System" with file persistence:

**Features:**
1. Load student records from "students.csv"
   - Format: name,math,english,science
2. Menu system:
   - Add new student
   - Update student scores
   - Delete student
   - View all students
   - View statistics
   - Search student
   - Save and exit

**Calculations:**
- Individual student averages
- Subject averages
- Overall class average
- Grade distribution

**Reports:**
- Generate "report.txt" with full statistics
- Generate "honors.txt" with students averaging 85+
- Generate "warning.txt" with students averaging <50

**Error Handling:**
- Invalid file format
- Missing files
- Invalid input

```python
# Your code here
```

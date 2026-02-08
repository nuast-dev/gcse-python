# Week 4: Strings - Indexing, Slicing, Methods, Iteration, and Validation

## Learning Objectives
- Access characters using indexing
- Extract substrings using slicing
- Use string methods effectively
- Iterate through strings
- Validate and process string input

## 1. String Basics

### Creating Strings
```python
name = "Python"
message = 'Hello, World!'
multiline = """This is a
multi-line
string"""

# Empty string
empty = ""
```

### String Length
```python
word = "Python"
length = len(word)
print(length)  # 6

name = input("Enter your name: ")
print(f"Your name has {len(name)} characters")
```

## 2. String Indexing

### Accessing Characters by Position
```python
word = "Python"

# Positive indexing (from start)
print(word[0])  # P
print(word[1])  # y
print(word[5])  # n

# Negative indexing (from end)
print(word[-1])  # n (last character)
print(word[-2])  # o (second from end)
print(word[-6])  # P (first character)
```

### Index Examples
```python
text = "Hello"
# Index:  0 1 2 3 4
# Char:   H e l l o
# Index: -5-4-3-2-1

first = text[0]      # H
last = text[-1]      # o
middle = text[2]     # l
```

### Common Index Operations
```python
email = "student@school.com"

# Get first character
first_char = email[0]  # s

# Get last character
last_char = email[-1]  # m

# Get character at specific position
at_symbol = email[7]  # @
```

## 3. String Slicing

### Basic Slicing Syntax
`string[start:stop:step]`

```python
text = "Python Programming"

# From index 0 to 5 (exclusive)
print(text[0:6])  # Python

# From index 7 onwards
print(text[7:])  # Programming

# Up to index 6 (exclusive)
print(text[:6])  # Python

# Last 3 characters
print(text[-3:])  # ing

# Everything except last 3
print(text[:-3])  # Python Program
```

### Slicing with Step
```python
text = "Python"

# Every second character
print(text[::2])  # Pto

# Reverse string
print(text[::-1])  # nohtyP

# From index 1 to end, step 2
print(text[1::2])  # yhn
```

### Practical Slicing Examples
```python
date = "15/03/2024"

# Extract day, month, year
day = date[0:2]      # 15
month = date[3:5]    # 03
year = date[6:]      # 2024

print(f"Day: {day}, Month: {month}, Year: {year}")
```

## 4. String Methods

### Case Conversion
```python
text = "Hello World"

print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World
print(text.capitalize()) # Hello world
print(text.swapcase())   # hELLO wORLD
```

### Checking Case
```python
text = "HELLO"
print(text.isupper())  # True
print(text.islower())  # False

text = "hello"
print(text.islower())  # True
```

### Finding and Counting
```python
text = "Python Programming"

# Find position of substring
pos = text.find("Pro")    # 7
pos = text.find("Java")   # -1 (not found)

# Count occurrences
count = text.count("m")   # 2
count = text.count("ing") # 1
```

### Checking Content
```python
# Check if all characters are letters
"Hello".isalpha()    # True
"Hello123".isalpha() # False

# Check if all characters are digits
"12345".isdigit()    # True
"123.45".isdigit()   # False

# Check if alphanumeric
"Hello123".isalnum() # True
"Hello 123".isalnum()# False (space)

# Check if all whitespace
"   ".isspace()      # True
```

### String Starts/Ends
```python
filename = "report.pdf"

if filename.endswith(".pdf"):
    print("PDF file")

url = "https://example.com"

if url.startswith("https"):
    print("Secure connection")
```

### Stripping Whitespace
```python
text = "  Hello World  "

print(text.strip())   # "Hello World"
print(text.lstrip())  # "Hello World  "
print(text.rstrip())  # "  Hello World"

# Useful for cleaning input
name = input("Enter name: ").strip()
```

### Replacing Text
```python
text = "Hello World"

new_text = text.replace("World", "Python")
print(new_text)  # Hello Python

# Replace all occurrences
text = "aaa bbb aaa"
print(text.replace("aaa", "xxx"))  # xxx bbb xxx
```

### Splitting and Joining
```python
# Split into list
sentence = "Python is fun"
words = sentence.split()
print(words)  # ['Python', 'is', 'fun']

# Split by specific separator
date = "15/03/2024"
parts = date.split("/")
print(parts)  # ['15', '03', '2024']

# Join list into string
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)  # Python is fun

csv = ",".join(["Alice", "16", "London"])
print(csv)  # Alice,16,London
```

## 5. Iterating Through Strings

### Basic Iteration
```python
word = "Python"

for char in word:
    print(char)

# Output: P y t h o n (each on new line)
```

### Iteration with Index
```python
word = "Python"

for i in range(len(word)):
    print(f"Index {i}: {word[i]}")

# Output:
# Index 0: P
# Index 1: y
# ...
```

### Using enumerate()
```python
word = "Python"

for index, char in enumerate(word):
    print(f"{index}: {char}")

# Output:
# 0: P
# 1: y
# ...
```

### Counting Characters
```python
text = input("Enter text: ")
vowel_count = 0

for char in text.lower():
    if char in "aeiou":
        vowel_count += 1

print(f"Vowels: {vowel_count}")
```

## 6. String Validation

### Validating Input
```python
# Check if name is valid (letters and spaces only)
name = input("Enter name: ")

is_valid = True
for char in name:
    if not (char.isalpha() or char.isspace()):
        is_valid = False
        break

if is_valid and len(name) > 0:
    print("Valid name")
else:
    print("Invalid name")
```

### Email Validation (Basic)
```python
email = input("Enter email: ")

# Simple checks
has_at = "@" in email
has_dot = "." in email
no_spaces = " " not in email

if has_at and has_dot and no_spaces and len(email) >= 5:
    print("Email format looks valid")
else:
    print("Invalid email format")
```

### Password Strength Check
```python
password = input("Enter password: ")

# Check criteria
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
long_enough = len(password) >= 8

if has_digit and has_upper and has_lower and long_enough:
    print("Strong password")
else:
    print("Weak password")
    if not long_enough:
        print("- Need at least 8 characters")
    if not has_digit:
        print("- Need at least one digit")
    if not has_upper:
        print("- Need at least one uppercase letter")
    if not has_lower:
        print("- Need at least one lowercase letter")
```

## Practice Exercises

### Exercise 1: String Analyzer
Write a program that:
1. Asks for a sentence
2. Displays:
   - Total characters (including spaces)
   - Total words
   - Total vowels
   - Total consonants

```python
# Your code here
```

### Exercise 2: Name Formatter
Create a name formatter that:
1. Asks for full name (e.g., "john smith")
2. Outputs in title case (e.g., "John Smith")
3. Extracts and displays first and last name separately

```python
# Your code here
```

### Exercise 3: Palindrome Checker
Write a program that:
1. Asks for a word
2. Checks if it's a palindrome (reads same forwards and backwards)
3. Examples: "radar", "level", "noon"
(Ignore case)

```python
# Your code here
```

### Exercise 4: Caesar Cipher
Create a simple Caesar cipher that:
1. Asks for a message
2. Shifts each letter by 3 positions
3. Example: "ABC" → "DEF"
(Only shift letters, keep other characters same)

```python
# Your code here
```

### Exercise 5: Username Validator
Validate username with these rules:
- 5-15 characters long
- Only letters, numbers, and underscores
- Must start with a letter
- Not all numbers

```python
# Your code here
```

### Exercise 6: Word Counter
Count occurrences of a specific word in a sentence:
1. Ask for a sentence
2. Ask for a word to search
3. Count how many times it appears (case-insensitive)

```python
# Your code here
```

### Exercise 7: Initials Generator
Create an initials generator:
1. Ask for full name (e.g., "John Robert Smith")
2. Extract and display initials (e.g., "JRS")
3. Make all initials uppercase

```python
# Your code here
```

### Exercise 8: Phone Number Formatter
Format phone numbers:
1. Ask for 11-digit phone number
2. Validate it's all digits
3. Format as: (XXXXX) XXX-XXX
4. Example: "01234567890" → "(01234) 567-890"

```python
# Your code here
```

## Key Concepts to Remember

- **Indexing**: Starts at 0, negative indices count from end
- **Slicing**: `[start:stop:step]` - stop is exclusive
- **Immutable**: Strings cannot be changed, methods return new strings
- **len()**: Returns number of characters
- **in**: Check if substring exists: `"cat" in "caterpillar"`
- **String methods** return new strings, don't modify original
- **Case-sensitive**: "A" != "a" unless converted
- **Iteration**: Can loop through characters with `for char in string`

## Common String Methods Quick Reference

```python
text = "  Hello World  "

text.upper()          # "  HELLO WORLD  "
text.lower()          # "  hello world  "
text.strip()          # "Hello World"
text.replace("o", "0")# "  Hell0 W0rld  "
text.split()          # ["Hello", "World"]
text.startswith("  ") # True
text.endswith("  ")   # True
text.find("World")    # 8
text.count("l")       # 3
text.isalpha()        # False (has spaces)
text.isdigit()        # False
```

## Common Mistakes to Avoid

1. Index out of range (accessing index >= length)
2. Forgetting strings are immutable
3. Using wrong case in comparisons
4. Forgetting to strip() input (extra spaces)
5. Confusing `find()` return value (-1 means not found)
6. Using `=` to modify string (create new string instead)
7. Off-by-one errors in slicing

## Extension Challenge

Create a "Text Statistics Tool" that:
1. Asks for a paragraph of text
2. Analyzes and displays:
   - Total characters (with and without spaces)
   - Total words
   - Total sentences (count periods, !, ?)
   - Longest word and its length
   - Most common character (excluding spaces)
   - Percentage of text that is letters vs numbers vs other
3. Format all output neatly

```python
# Your code here
```

## String Slicing Cheat Sheet

```python
text = "Python"
# Indices: 0=P, 1=y, 2=t, 3=h, 4=o, 5=n

text[0:3]   # "Pyt"  (start to stop-1)
text[:3]    # "Pyt"  (from beginning)
text[3:]    # "hon"  (to end)
text[-3:]   # "hon"  (last 3 chars)
text[:-3]   # "Pyt"  (except last 3)
text[::2]   # "Pto"  (every 2nd char)
text[::-1]  # "nohtyP" (reverse)
```

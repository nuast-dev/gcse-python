# Week 8: Algorithms and Mixed GCSE Level Problems

## Learning Objectives
- Apply all previous concepts to solve complex problems
- Implement common algorithms
- Practice problem-solving strategies
- Combine multiple programming concepts
- Prepare for GCSE exam scenarios

## 1. Searching Algorithms

### Linear Search
```python
def linear_search(data, target):
    """
    Search for target in data list.
    Returns index if found, -1 if not found.
    """
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Example usage
numbers = [23, 45, 12, 67, 34, 89, 15]
position = linear_search(numbers, 67)
if position != -1:
    print(f"Found at index {position}")
else:
    print("Not found")
```

### Binary Search (Sorted Lists Only)
```python
def binary_search(data, target):
    """
    Search for target in sorted list using binary search.
    Much faster than linear search for large lists.
    """
    left = 0
    right = len(data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage
numbers = [12, 15, 23, 34, 45, 67, 89]  # Must be sorted!
position = binary_search(numbers, 34)
print(f"Found at index {position}")
```

## 2. Sorting Algorithms

### Bubble Sort
```python
def bubble_sort(data):
    """
    Sort list using bubble sort algorithm.
    Compares adjacent elements and swaps if needed.
    """
    n = len(data)
    
    for i in range(n):
        # Track if any swaps made
        swapped = False
        
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                # Swap elements
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        
        # If no swaps, list is sorted
        if not swapped:
            break
    
    return data

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers.copy())
print(sorted_numbers)
```

### Selection Sort
```python
def selection_sort(data):
    """
    Sort list using selection sort.
    Finds minimum element and moves to beginning.
    """
    n = len(data)
    
    for i in range(n):
        # Find minimum in remaining unsorted part
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        
        # Swap minimum to current position
        data[i], data[min_idx] = data[min_idx], data[i]
    
    return data

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = selection_sort(numbers.copy())
print(sorted_numbers)
```

## 3. Validation Algorithms

### Credit Card Validation (Luhn Algorithm)
```python
def validate_credit_card(card_number):
    """
    Validate credit card using Luhn algorithm.
    """
    # Remove spaces and convert to list of digits
    digits = [int(d) for d in card_number.replace(" ", "")]
    
    # Double every second digit from right
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    # Sum all digits
    total = sum(digits)
    
    # Valid if sum is divisible by 10
    return total % 10 == 0

# Example
card = "4532 1488 0343 6467"
print(f"Valid: {validate_credit_card(card)}")
```

### Email Validation
```python
def validate_email(email):
    """
    Validate email format.
    """
    # Check basic requirements
    if len(email) < 5:
        return False
    
    # Must have exactly one @
    if email.count("@") != 1:
        return False
    
    # Split into local and domain
    parts = email.split("@")
    local = parts[0]
    domain = parts[1]
    
    # Check local part
    if len(local) == 0:
        return False
    
    # Check domain
    if len(domain) < 3 or "." not in domain:
        return False
    
    # Check for spaces
    if " " in email:
        return False
    
    return True

# Example
print(validate_email("student@school.com"))  # True
print(validate_email("invalid.email"))       # False
```

## 4. Data Processing Algorithms

### Find Mode (Most Common Value)
```python
def find_mode(data):
    """
    Find most frequently occurring value.
    """
    if len(data) == 0:
        return None
    
    # Count occurrences
    counts = {}
    for value in data:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    # Find maximum count
    max_count = max(counts.values())
    
    # Find value(s) with maximum count
    modes = [k for k, v in counts.items() if v == max_count]
    
    return modes[0] if len(modes) == 1 else modes

# Example
numbers = [1, 2, 2, 3, 3, 3, 4, 4]
print(f"Mode: {find_mode(numbers)}")  # 3
```

### Calculate Median
```python
def calculate_median(data):
    """
    Calculate median (middle value) of list.
    """
    if len(data) == 0:
        return None
    
    # Sort the data
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # If odd length, return middle value
    if n % 2 == 1:
        return sorted_data[n // 2]
    
    # If even length, return average of two middle values
    mid1 = sorted_data[n // 2 - 1]
    mid2 = sorted_data[n // 2]
    return (mid1 + mid2) / 2

# Example
numbers = [23, 45, 12, 67, 34]
print(f"Median: {calculate_median(numbers)}")  # 34
```

## 5. String Algorithms

### Anagram Checker
```python
def are_anagrams(word1, word2):
    """
    Check if two words are anagrams.
    """
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    # Check if same length
    if len(word1) != len(word2):
        return False
    
    # Sort and compare
    return sorted(word1) == sorted(word2)

# Example
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
```

### Caesar Cipher
```python
def caesar_encrypt(text, shift):
    """
    Encrypt text using Caesar cipher.
    """
    result = ""
    
    for char in text:
        if char.isalpha():
            # Get base (A or a)
            base = ord('A') if char.isupper() else ord('a')
            # Shift character
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    
    return result

def caesar_decrypt(text, shift):
    """
    Decrypt Caesar cipher.
    """
    return caesar_encrypt(text, -shift)

# Example
message = "Hello World"
encrypted = caesar_encrypt(message, 3)
print(f"Encrypted: {encrypted}")  # Khoor Zruog
decrypted = caesar_decrypt(encrypted, 3)
print(f"Decrypted: {decrypted}")  # Hello World
```

## 6. Number Algorithms

### Prime Number Checker
```python
def is_prime(n):
    """
    Check if number is prime.
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Find all primes up to n
def find_primes(n):
    """
    Find all prime numbers up to n.
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Example
print(find_primes(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### Fibonacci Sequence
```python
def fibonacci(n):
    """
    Generate first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

# Example
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Greatest Common Divisor (GCD)
```python
def gcd(a, b):
    """
    Find greatest common divisor using Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Example
print(gcd(48, 18))  # 6
print(gcd(100, 35))  # 5
```

## 7. Mixed Problem Examples

### Problem 1: Grade Statistics System
```python
def grade_statistics_system():
    """
    Complete grade management system.
    """
    students = []
    
    # Input students
    n = int(input("Number of students: "))
    for i in range(n):
        name = input(f"Student {i+1} name: ")
        score = int(input(f"Score for {name}: "))
        students.append({"name": name, "score": score})
    
    # Calculate statistics
    scores = [s["score"] for s in students]
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    # Find top student
    top_student = max(students, key=lambda s: s["score"])
    
    # Count grades
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for student in students:
        score = student["score"]
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[grade] += 1
    
    # Display results
    print("\n=== Statistics ===")
    print(f"Class Average: {average:.2f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Top Student: {top_student['name']} ({top_student['score']})")
    print("\nGrade Distribution:")
    for grade, count in grades.items():
        print(f"  {grade}: {count} students")
```

### Problem 2: Text Analysis Tool
```python
def analyze_text(text):
    """
    Comprehensive text analysis.
    """
    # Character statistics
    total_chars = len(text)
    no_space_chars = len(text.replace(" ", ""))
    letters = sum(c.isalpha() for c in text)
    digits = sum(c.isdigit() for c in text)
    spaces = text.count(" ")
    
    # Word statistics
    words = text.split()
    word_count = len(words)
    avg_word_length = sum(len(w) for w in words) / word_count if word_count > 0 else 0
    longest_word = max(words, key=len) if words else ""
    
    # Sentence count (approximate)
    sentences = text.count(".") + text.count("!") + text.count("?")
    
    # Character frequency
    char_freq = {}
    for char in text.lower():
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Most common character
    most_common = max(char_freq, key=char_freq.get) if char_freq else None
    
    # Display results
    print(f"Total characters: {total_chars}")
    print(f"Characters (no spaces): {no_space_chars}")
    print(f"Letters: {letters}")
    print(f"Digits: {digits}")
    print(f"Spaces: {spaces}")
    print(f"Words: {word_count}")
    print(f"Average word length: {avg_word_length:.1f}")
    print(f"Longest word: {longest_word} ({len(longest_word)} chars)")
    print(f"Sentences: {sentences}")
    if most_common:
        print(f"Most common letter: {most_common} ({char_freq[most_common]} times)")

# Example
text = "Python is a powerful programming language. It is easy to learn!"
analyze_text(text)
```

### Problem 3: Shopping System with Discounts
```python
def shopping_system():
    """
    Shopping cart with multiple discount rules.
    """
    cart = []
    
    print("=== Shopping System ===")
    print("Enter items (price and quantity)")
    print("Enter 0 to finish\n")
    
    while True:
        price = float(input("Item price (0 to finish): £"))
        if price == 0:
            break
        quantity = int(input("Quantity: "))
        cart.append({"price": price, "quantity": quantity})
    
    if len(cart) == 0:
        print("No items in cart")
        return
    
    # Calculate subtotal
    subtotal = sum(item["price"] * item["quantity"] for item in cart)
    
    # Apply discounts
    discount = 0
    discount_reason = ""
    
    # 10% off if over £50
    if subtotal >= 50:
        discount = subtotal * 0.10
        discount_reason = "10% off orders over £50"
    
    # 5% off if 5+ items
    total_items = sum(item["quantity"] for item in cart)
    if total_items >= 5:
        bulk_discount = subtotal * 0.05
        if bulk_discount > discount:
            discount = bulk_discount
            discount_reason = "5% off 5+ items"
    
    # Calculate final total
    total_after_discount = subtotal - discount
    vat = total_after_discount * 0.20
    final_total = total_after_discount + vat
    
    # Display receipt
    print("\n=== Receipt ===")
    print(f"Items: {len(cart)}")
    print(f"Total quantity: {total_items}")
    print(f"Subtotal: £{subtotal:.2f}")
    if discount > 0:
        print(f"Discount ({discount_reason}): -£{discount:.2f}")
        print(f"After discount: £{total_after_discount:.2f}")
    print(f"VAT (20%): £{vat:.2f}")
    print(f"Final Total: £{final_total:.2f}")
```

## Practice Problems

### Problem 1: Password Generator
Create a password generator that:
- Takes desired length as input
- Includes uppercase, lowercase, digits, and symbols
- Ensures at least one of each type
- Returns random password

### Problem 2: Attendance System
Build an attendance tracking system:
- Track daily attendance for students
- Calculate attendance percentage
- Identify students below 90%
- Save/load from file

### Problem 3: Quiz System
Create a quiz program:
- Load questions from file
- Ask user questions
- Track score
- Show final results with percentage
- Save high scores

### Problem 4: Bank Account System
Implement simple banking:
- Create account with initial balance
- Deposit money
- Withdraw money (with overdraft check)
- View transaction history
- Calculate interest
- Save account data to file

### Problem 5: Recipe Manager
Create recipe management system:
- Store recipes with ingredients and quantities
- Scale recipes up/down
- Search recipes by ingredient
- Calculate total cost
- Save/load recipes from file

### Problem 6: Voting System
Implement voting system:
- Register candidates
- Cast votes with validation
- Count votes
- Determine winner
- Handle ties
- Generate results report

### Problem 7: Library System
Build library management:
- Add/remove books
- Borrow/return books
- Track due dates
- Calculate late fees
- Search books
- Save/load library data

### Problem 8: Game Score Tracker
Create game leaderboard:
- Record player scores
- Sort by high score
- Track personal bests
- Calculate averages
- Show top 10
- Save/load scores

## Exam Tips

### Problem-Solving Strategy
1. **Read carefully**: Understand what's being asked
2. **Plan**: Break problem into steps
3. **Identify patterns**: What concepts are needed?
4. **Start simple**: Get basic version working first
5. **Test**: Try different inputs
6. **Refine**: Add features and handle edge cases

### Common Exam Topics
- **Validation**: Check inputs are valid
- **File handling**: Read/write data
- **Lists**: Store and process collections
- **Functions**: Break problems down
- **Loops**: Process multiple items
- **Conditionals**: Make decisions
- **Strings**: Text processing
- **Statistics**: Calculate averages, find min/max

### Code Quality Checklist
- ✓ Clear variable names
- ✓ Comments for complex logic
- ✓ Proper indentation
- ✓ Input validation
- ✓ Error handling
- ✓ Test with different inputs
- ✓ Functions for repeated code

## Extension Challenge

Create a "School Management System" that combines all concepts:

**Features:**
- Student management (add, remove, update)
- Grade tracking (multiple subjects)
- Attendance tracking
- Report generation
- Statistics calculation
- File persistence
- Search and filter
- Data validation
- Menu system

**Must include:**
- Functions for each major feature
- File I/O for data persistence
- Lists and dictionaries for data storage
- Sorting and searching algorithms
- Statistical calculations
- Input validation
- Error handling
- Clear user interface

```python
# Your complete implementation here
```

## Summary

Week 8 brings together everything from the previous 7 weeks:
- **Week 1-2**: Basic syntax and control flow
- **Week 3**: Loops for repetition
- **Week 4**: String processing
- **Week 5**: Lists for data storage
- **Week 6**: Functions for organization
- **Week 7**: Files for persistence
- **Week 8**: Algorithms to solve complex problems

You're now ready for GCSE Python programming challenges!

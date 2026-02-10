"""
Week 8 Exercises: Algorithms

Complete the exercises below. Each function should follow the specifications
provided in the docstrings.

Topics: Searching, Sorting, Validation, String/Number algorithms
"""


def linear_search(items, target):
    """
    Search for target in list using linear search.
    
    Args:
        items (list): List to search
        target: Item to find
        
    Returns:
        int: Index of target if found, -1 otherwise
        
    Example:
        >>> linear_search([10, 20, 30, 40], 30)
        2
        >>> linear_search([10, 20, 30, 40], 50)
        -1
    """
    # TODO: Implement this function
    pass


def bubble_sort(items):
    """
    Sort a list using bubble sort algorithm.
    
    Args:
        items (list): List to sort
        
    Returns:
        list: Sorted list
        
    Example:
        >>> bubble_sort([64, 34, 25, 12, 22])
        [12, 22, 25, 34, 64]
    """
    # TODO: Implement this function
    pass


def is_anagram(str1, str2):
    """
    Check if two strings are anagrams (contain same letters).
    Ignore case and spaces.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        bool: True if anagrams, False otherwise
        
    Example:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "world")
        False
    """
    # TODO: Implement this function
    pass


def caesar_cipher(text, shift):
    """
    Encrypt text using Caesar cipher (shift each letter by shift positions).
    Only shift letters, leave other characters unchanged.
    
    Args:
        text (str): Text to encrypt
        shift (int): Number of positions to shift
        
    Returns:
        str: Encrypted text
        
    Example:
        >>> caesar_cipher("abc", 1)
        'bcd'
        >>> caesar_cipher("xyz", 3)
        'abc'
    """
    # TODO: Implement this function
    pass


def find_gcd(a, b):
    """
    Find the Greatest Common Divisor of two numbers using Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: GCD of a and b
        
    Example:
        >>> find_gcd(48, 18)
        6
    """
    # TODO: Implement this function
    pass


# Test your functions here
if __name__ == "__main__":
    print("Testing Week 8 Exercises...")
    print()
    
    # Test linear_search
    # print(linear_search([10, 20, 30, 40], 30))
    
    # Test bubble_sort
    # print(bubble_sort([64, 34, 25, 12, 22]))
    
    # Test is_anagram
    # print(is_anagram("listen", "silent"))
    
    # Test caesar_cipher
    # print(caesar_cipher("abc", 1))
    
    # Test find_gcd
    # print(find_gcd(48, 18))

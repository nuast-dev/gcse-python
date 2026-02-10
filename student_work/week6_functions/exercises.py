"""
Week 6 Exercises: Functions

Complete the exercises below. Each function should follow the specifications
provided in the docstrings.

Topics: Parameters, Return values, Decomposition, Testing, Scope
"""


def factorial(n):
    """
    Calculate the factorial of a number (n!).
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    # TODO: Implement this function
    pass


def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if prime, False otherwise
        
    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    # TODO: Implement this function
    pass


def fibonacci(n):
    """
    Generate the nth Fibonacci number.
    The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, ...
    
    Args:
        n (int): Position in sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Example:
        >>> fibonacci(0)
        0
        >>> fibonacci(6)
        8
    """
    # TODO: Implement this function
    pass


def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).
    Formula: BMI = weight / (height^2)
    
    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters
        
    Returns:
        float: BMI value rounded to 1 decimal place
        
    Example:
        >>> calculate_bmi(70, 1.75)
        22.9
    """
    # TODO: Implement this function
    pass


# Test your functions here
if __name__ == "__main__":
    print("Testing Week 6 Exercises...")
    print()
    
    # Test factorial
    # print(factorial(5))
    
    # Test is_prime
    # print(is_prime(7))
    
    # Test fibonacci
    # print(fibonacci(10))
    
    # Test calculate_bmi
    # print(calculate_bmi(70, 1.75))

"""
Week 2 Exercises: Conditionals

Complete the exercises below. Each function should follow the specifications
provided in the docstrings.

Topics: If/elif/else, Comparisons, Boolean Logic, Range checks
"""


def check_grade(score):
    """
    Return the grade based on the score.
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
    
    Args:
        score (int): The test score
        
    Returns:
        str: The letter grade
        
    Example:
        >>> check_grade(85)
        'B'
    """
    # TODO: Implement this function
    pass


def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if even, False otherwise
        
    Example:
        >>> is_even(10)
        True
        >>> is_even(7)
        False
    """
    # TODO: Implement this function
    pass


def check_password_strength(password):
    """
    Check password strength based on length.
    Strong: 12+ characters, Medium: 8-11 characters, Weak: less than 8
    
    Args:
        password (str): The password to check
        
    Returns:
        str: 'Strong', 'Medium', or 'Weak'
        
    Example:
        >>> check_password_strength("abcd")
        'Weak'
    """
    # TODO: Implement this function
    pass


# Test your functions here
if __name__ == "__main__":
    print("Testing Week 2 Exercises...")
    print()
    
    # Test check_grade
    # print(check_grade(85))
    
    # Test is_even
    # print(is_even(10))
    
    # Test check_password_strength
    # print(check_password_strength("mypassword123"))

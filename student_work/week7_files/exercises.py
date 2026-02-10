"""
Week 7 Exercises: Files

Complete the exercises below. Each function should follow the specifications
provided in the docstrings.

Topics: Read/Write text files, Strip, Split, File processing, Error handling
"""


def read_file_lines(filename):
    """
    Read all lines from a file and return as a list.
    
    Args:
        filename (str): Path to the file
        
    Returns:
        list: List of lines (with newlines stripped)
        
    Example:
        >>> read_file_lines("data.txt")
        ['line 1', 'line 2', 'line 3']
    """
    # TODO: Implement this function
    pass


def write_to_file(filename, content):
    """
    Write content to a file. Creates file if it doesn't exist.
    
    Args:
        filename (str): Path to the file
        content (str): Content to write
        
    Returns:
        bool: True if successful, False otherwise
    """
    # TODO: Implement this function
    pass


def count_lines_in_file(filename):
    """
    Count the number of lines in a file.
    
    Args:
        filename (str): Path to the file
        
    Returns:
        int: Number of lines in the file
    """
    # TODO: Implement this function
    pass


def read_csv_file(filename):
    """
    Read a CSV file and return data as a list of lists.
    Assumes comma-separated values.
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        list: List of rows, each row is a list of values
        
    Example:
        >>> read_csv_file("data.csv")
        [['Name', 'Age', 'Score'], ['Alice', '16', '95'], ['Bob', '17', '87']]
    """
    # TODO: Implement this function
    pass


# Test your functions here
if __name__ == "__main__":
    print("Testing Week 7 Exercises...")
    print()
    
    # Create a test file
    # write_to_file("test.txt", "Hello, World!\nPython is fun!\n")
    
    # Test read_file_lines
    # print(read_file_lines("test.txt"))
    
    # Test count_lines_in_file
    # print(count_lines_in_file("test.txt"))

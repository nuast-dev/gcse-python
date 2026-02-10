#!/usr/bin/python3

"""
Week 1 Exercises: Basics

Complete the exercises below. Each function should follow the specifications
provided in the docstrings.

Topics: I/O, Variables, Types, Casting, Arithmetic, Formatting
"""

def greet_user(name):
  """
  Return a greeting message for the given name.

  Args:
      name (str): The user's name

  Returns:
      str: A greeting message

  Example:
      >>> greet_user("Alice")
      'Hello, Alice!'
  """
  # +++your code here+++
  return


def calculate_age(birth_year):
  """
  Calculate age from birth year (assuming current year is 2026).

  Args:
      birth_year (int): Year of birth

  Returns:
      int: Calculated age

  Example:
      >>> calculate_age(2010)
      16
  """
  # +++your code here+++
  return


def celsius_to_fahrenheit(celsius):
  """
  Convert temperature from Celsius to Fahrenheit.
  Formula: F = C * 9/5 + 32

  Args:
      celsius (float): Temperature in Celsius

  Returns:
      float: Temperature in Fahrenheit

  Example:
      >>> celsius_to_fahrenheit(0)
      32.0
      >>> celsius_to_fahrenheit(100)
      212.0
  """
  # +++your code here+++
  return


def format_currency(amount):
  """
  Format a number as currency (GBP) with 2 decimal places.

  Args:
      amount (float): The amount to format

  Returns:
      str: Formatted currency string

  Example:
      >>> format_currency(123.456)
      '£123.46'
  """
  # +++your code here+++
  return


def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def test_float(got, expected, tol=1e-6):
  if abs(got - expected) <= tol:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
  print("Testing Week 1 Exercises...")
  print()

  print("greet_user")
  test(greet_user("Alice"), "Hello, Alice!")
  test(greet_user("Simon"), "Hello, Simon!")

  print()
  print("calculate_age")
  test(calculate_age(2010), 16)
  test(calculate_age(2026), 0)

  print()
  print("celsius_to_fahrenheit")
  test_float(celsius_to_fahrenheit(0), 32.0)
  test_float(celsius_to_fahrenheit(100), 212.0)
  test_float(celsius_to_fahrenheit(25), 77.0)

  print()
  print("format_currency")
  test(format_currency(123.456), "£123.46")
  test(format_currency(99.99), "£99.99")
  test(format_currency(5), "£5.00")


if __name__ == "__main__":
  main()

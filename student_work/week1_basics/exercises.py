#!/usr/bin/python3

# Week 1 exercises: Basics
# Topics: I/O, variables, types, casting, arithmetic, formatting
#
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.


# A. greet_user
# Return a greeting message for the given name.
# Example: greet_user("Alice") -> "Hello, Alice!"
def greet_user(name):
  # +++your code here+++
  return


# B. calculate_age
# Calculate age from birth year (assuming current year is 2026).
# Example: calculate_age(2010) -> 16
def calculate_age(birth_year):
  # +++your code here+++
  return


# C. celsius_to_fahrenheit
# Convert temperature from Celsius to Fahrenheit.
# Formula: F = C * 9/5 + 32
# Examples:
#   celsius_to_fahrenheit(0) -> 32.0
#   celsius_to_fahrenheit(100) -> 212.0
def celsius_to_fahrenheit(celsius):
  # +++your code here+++
  return


# D. format_currency
# Format a number as currency (GBP) with 2 decimal places.
# Example: format_currency(123.456) -> "£123.46"
def format_currency(amount):
  # +++your code here+++
  return


# E. check_type
# Return the type name of the given value as a string.
# Examples:
#   check_type(42) -> "int"
#   check_type(3.14) -> "float"
#   check_type("hello") -> "str"
#   check_type(True) -> "bool"
def check_type(value):
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
  print("Testing Week 1 exercises...")
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

  print()
  print("check_type")
  test(check_type(42), "int")
  test(check_type(3.14), "float")
  test(check_type("hello"), "str")
  test(check_type(True), "bool")
  test(check_type(False), "bool")


if __name__ == "__main__":
  main()

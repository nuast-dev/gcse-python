#!/usr/bin/python3

# Week 1 basics exercises (Part 2)
# Topics: casting input-like strings, arithmetic, exponentiation, formatting,
#         real-world mini problems (temp convert, circle, receipt)


# A. temp_fahrenheit
# Given c_str (string), convert to float and return Fahrenheit as float
# F = C * 9/5 + 32
def temp_fahrenheit(c_str):
  # +++your code here+++
  return


# B. circle_area
# Given radius_str (string), convert to float and return area (float)
# Use pi = 3.14159
# Area = pi * r**2
def circle_area(radius_str):
  # +++your code here+++
  return


# C. circle_circumference
# Given radius_str (string), convert to float and return circumference (float)
# Use pi = 3.14159
# Circumference = 2 * pi * r
def circle_circumference(radius_str):
  # +++your code here+++
  return


# D. change_from_50
# Given price_str and qty_str as strings:
# 1) cast them
# 2) total = price * qty
# 3) change = 50 - total
# Return a tuple: (total_as_currency, change_as_currency)
# Currency format must be £X.XX
def change_from_50(price_str, qty_str):
  # +++your code here+++
  return


# E. receipt_3_items
# Given three item names and prices as strings:
# item1, price1_str, item2, price2_str, item3, price3_str
#
# Compute:
# subtotal = sum(prices)
# vat = subtotal * 0.20
# total = subtotal + vat
#
# Return a multi-line string exactly like:
# Item: <item1> - £<p1>
# Item: <item2> - £<p2>
# Item: <item3> - £<p3>
# Subtotal: £<subtotal>
# VAT: £<vat>
# Total: £<total>
#
# All money must be 2dp. Use f-strings.
def receipt_3_items(item1, price1_str, item2, price2_str, item3, price3_str):
  # +++your code here+++
  return


# F. safe_divide
# Given a_str and b_str as strings, cast to float.
# If b is 0, return the string "Cannot divide by zero"
# Otherwise return the division result as a float.
def safe_divide(a_str, b_str):
  # +++your code here+++
  return


def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Helper for float comparisons (so students don’t fail due to tiny rounding issues)
def test_float(got, expected, tol=1e-6):
  if abs(got - expected) <= tol:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
  print('temp_fahrenheit')
  test_float(temp_fahrenheit('0'), 32.0)
  test_float(temp_fahrenheit('100'), 212.0)
  test_float(temp_fahrenheit('20'), 68.0)

  print()
  print('circle_area')
  test_float(circle_area('1'), 3.14159)
  test_float(circle_area('2'), 12.56636)

  print()
  print('circle_circumference')
  test_float(circle_circumference('1'), 6.28318)
  test_float(circle_circumference('2.5'), 15.70795)

  print()
  print('change_from_50')
  test(change_from_50('19.5', '2'), ('£39.00', '£11.00'))
  test(change_from_50('10', '5'), ('£50.00', '£0.00'))
  test(change_from_50('0.99', '3'), ('£2.97', '£47.03'))

  print()
  print('receipt_3_items')
  expected = (
    "Item: Pen - £1.20\n"
    "Item: Notebook - £2.50\n"
    "Item: Ruler - £0.80\n"
    "Subtotal: £4.50\n"
    "VAT: £0.90\n"
    "Total: £5.40"
  )
  test(receipt_3_items('Pen', '1.2', 'Notebook', '2.5', 'Ruler', '0.8'), expected)

  print()
  print('safe_divide')
  test_float(safe_divide('10', '4'), 2.5)
  test(safe_divide('10', '0'), 'Cannot divide by zero')


if __name__ == '__main__':
  main()

# Python Operators & Expressions

# Arithmetic Operators
print("Arithmetic Operators:")
a, b = 10, 3
print(f"{a} + {b} =", a + b)  # Addition
print(f"{a} - {b} =", a - b)  # Subtraction
print(f"{a} * {b} =", a * b)  # Multiplication
print(f"{a} / {b} =", a / b)  # Division
print(f"{a} % {b} =", a % b)  # Modulus
print(f"{a} ** {b} =", a ** b)  # Exponentiation
print("-" * 30)

# Comparison Operators
print("Comparison Operators:")
print(f"{a} == {b} ->", a == b)  # Equal to
print(f"{a} != {b} ->", a != b)  # Not equal to
print(f"{a} > {b} ->", a > b)    # Greater than
print(f"{a} < {b} ->", a < b)    # Less than
print(f"{a} >= {b} ->", a >= b)  # Greater than or equal to
print(f"{a} <= {b} ->", a <= b)  # Less than or equal to
print("-" * 30)

# Logical Operators
print("Logical Operators:")
x, y = True, False
print(f"{x} and {y} ->", x and y)  # AND
print(f"{x} or {y} ->", x or y)    # OR
print(f"not {x} ->", not x)        # NOT
print("-" * 30)

# Assignment Operators
print("Assignment Operators:")
c = 5
c += 3  # Equivalent to c = c + 3
print("c += 3 ->", c)
c -= 2  # Equivalent to c = c - 2
print("c -= 2 ->", c)
c *= 2  # Equivalent to c = c * 2
print("c *= 2 ->", c)
c /= 2  # Equivalent to c = c / 2
print("c /= 2 ->", c)
c **= 2  # Equivalent to c = c ** 2
print("c **= 2 ->", c)
print("-" * 30)

# Identity Operators
print("Identity Operators:")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("list1 is list2 ->", list1 is list2)  # True (Same object)
print("list1 is list3 ->", list1 is list3)  # False (Different object)
print("list1 is not list3 ->", list1 is not list3)  # True
print("-" * 30)

# Membership Operators
print("Membership Operators:")
numbers = [1, 2, 3, 4, 5]
print("3 in numbers ->", 3 in numbers)  # True
print("10 not in numbers ->", 10 not in numbers)  # True
print("-" * 30)

print("✅ Python Operators & Expressions Demonstration Completed!")

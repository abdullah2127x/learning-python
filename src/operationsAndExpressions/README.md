# Operations & Expressions in Python

Operations and expressions form the foundation of Python programming. They allow us to perform calculations, compare values, and manipulate data.

---

## Types of Operators

1. [Arithmetic Operators](#arithmetic-operators)
2. [Comparison Operators](#comparison-operators)
3. [Logical Operators](#logical-operators)
4. [Bitwise Operators](#bitwise-operators)
5. [Assignment Operators](#assignment-operators)
6. [Identity Operators](#identity-operators)
7. [Membership Operators](#membership-operators)

---

## Arithmetic Operators

Arithmetic operators perform mathematical operations on numerical values.

| Operator | Description    | Example  | Output |
| -------- | -------------- | -------- | ------ |
| `+`      | Addition       | `5 + 3`  | `8`    |
| `-`      | Subtraction    | `10 - 4` | `6`    |
| `*`      | Multiplication | `6 * 2`  | `12`   |
| `/`      | Division       | `10 / 2` | `5.0`  |
| `%`      | Modulus        | `10 % 3` | `1`    |
| `**`     | Exponentiation | `2 ** 3` | `8`    |

```python
# Example
x = 10
y = 3
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation
```

---

## Comparison Operators

Comparison operators compare values and return a Boolean result (`True` or `False`).

| Operator | Description           | Example  | Output |
| -------- | --------------------- | -------- | ------ |
| `==`     | Equal to              | `5 == 5` | `True` |
| `!=`     | Not equal to          | `5 != 3` | `True` |
| `>`      | Greater than          | `10 > 3` | `True` |
| `<`      | Less than             | `2 < 5`  | `True` |
| `>=`     | Greater than or equal | `5 >= 5` | `True` |
| `<=`     | Less than or equal    | `3 <= 5` | `True` |

```python
# Example
x = 10
y = 5
print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False
```

---

## Logical Operators

Logical operators combine multiple conditions and return a Boolean result.

| Operator | Description       | Example          | Output  |
| -------- | ----------------- | ---------------- | ------- |
| `and`    | Both True         | `True and False` | `False` |
| `or`     | At least one True | `True or False`  | `True`  |
| `not`    | Negates the value | `not True`       | `False` |

```python
# Example
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

---

## Assignment Operators

Assignment operators assign values to variables and modify them in place.

| Operator | Description           | Example   | Equivalent To |
| -------- | --------------------- | --------- | ------------- |
| `=`      | Assign                | `x = 5`   | `x = 5`       |
| `+=`     | Add & Assign          | `x += 3`  | `x = x + 3`   |
| `-=`     | Subtract & Assign     | `x -= 2`  | `x = x - 2`   |
| `*=`     | Multiply & Assign     | `x *= 2`  | `x = x * 2`   |
| `/=`     | Divide & Assign       | `x /= 2`  | `x = x / 2`   |
| `//=`    | Floor Divide & Assign | `x //= 2` | `x = x // 2`  |
| `%=`     | Modulus & Assign      | `x %= 2`  | `x = x % 2`   |
| `**=`    | Exponentiate & Assign | `x **= 2` | `x = x ** 2`  |

```python
# Example
x = 5
x += 3  # x = x + 3
print(x)  # 8
```

---

## Identity Operators

Identity operators check whether two variables refer to the same object in memory.

| Operator | Description      | Example      | Output       |
| -------- | ---------------- | ------------ | ------------ |
| `is`     | Same object      | `x is y`     | `True/False` |
| `is not` | Different object | `x is not y` | `True/False` |

```python
# Example
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)  # True
print(x is z)  # False
```

---

## Membership Operators

Membership operators check if a value exists within a sequence.

| Operator | Description    | Example                | Output |
| -------- | -------------- | ---------------------- | ------ |
| `in`     | Exists         | `5 in [1, 2, 3, 4, 5]` | `True` |
| `not in` | Does not exist | `10 not in [1, 2, 3]`  | `True` |

```python
# Example
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)   # True
print(10 not in numbers)  # True
```

---

This guide covers the fundamental operations and expressions in Python. Mastering these will help you write efficient and powerful code! 🚀

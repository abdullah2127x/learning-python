# Data Types

Data types define the type of data a variable can hold. They specify how the data is stored and what operations can be performed on it. Following are some common data types used in Python.

---

## Common Data Types In Python

1. [Numeric Types](#numeric-types)
2. [Sequence Types](#sequence-types)
3. [Mapping Types](#mapping-types)
4. [Set Types](#set-types)
5. [Boolean Type](#boolean-type)
6. [None Type](#none-type)

---

## Numeric Types

Numeric types represent numbers in Python. They are immutable, meaning their values cannot be changed after creation.

### 1. **Integer (`int`)**

- Represents whole numbers (positive or negative).
- Example: `x = 10`

### 2. **Float (`float`)**

- Represents decimal numbers.
- Example: `y = 10.5`

### 3. **Complex (`complex`)**

- Represents numbers with a real and imaginary part.
- Example: `z = 2 + 3j`

---

## Sequence Types

Sequence types represent ordered collections of items. They are iterable and support indexing.

### 1. **String (`str`)**

- Represents a sequence of characters enclosed in single or double quotes.

```Example:
    text = "Hello, World!"
    print(type(text))
```

### 2. **List (`list`)**

- Represents an ordered, mutable collection of items. We store the list in square brackets `[]` and can be apply all the list method. As we discuss list is mutable so we can make changes in list easily.

```Example:
    fruits = ["apple", "banana", "cherry"]
    print(type(fruits))
```

### 3. **Tuple (`tuple`)**

- Represents an ordered, immutable collection of items. It is store in paranthesis `()` and can not be change once created as it is immutable.

```Example:
    coordinates = (10, 20)
    coordinates.append(10) // error
    print(type(coordinates))
```

---

## Boolean Type

The Boolean type represents truth values.

### 1. **Boolean (`bool`)**

- Represents `True` or `False`.

```
    is_valid = True
    print(type(is_valid))
```

---

## Mapping Types

Mapping types store data in key-value pairs.

### 1. **Dictionary (`dict`)**

- Represents an unordered, mutable collection of key-value pairs.
- As in other languages, there is object. But in Python we called it Dictionary

```
    person = {"name": "John", "age": 30}
```

---

## Set Types

Set types represent unordered collections of unique items. It is stored in curly brackets `{}`. In this we just store the values not the key of the items.

### 1. **Set (`set`)**

- Represents an unordered, mutable collection of unique items.

```
    unique_numbers = {1, 2, 3}
```

### 2. **Frozen Set (`frozenset`)**

- Represents an unordered, immutable collection of unique items.

```
    immutable_set = frozenset({1, 2, 3})
```

---

## None Type

The None type represents the absence of a value. As we can not declare a variable without assigning a value

### **None (`NoneType`)**

- Represents a null or empty value.

```
    result = None
    print(result) //None

```

---

## Table Definition

These are the some basic data structures

| Data Type   | Example                             | Mutable |
| ----------- | ----------------------------------- | ------- |
| `int`       | `x = 10`                            | No      |
| `float`     | `y = 10.5`                          | No      |
| `complex`   | `z = 2 + 3j`                        | No      |
| `str`       | `text = "Hello"`                    | No      |
| `list`      | `fruits = ["apple"]`                | Yes     |
| `tuple`     | `coordinates = (10, 20)`            | No      |
| `dict`      | `person = {"name": "John"}`         | Yes     |
| `set`       | `unique_numbers = {1, 2}`           | Yes     |
| `frozenset` | `immutable_set = frozenset({1, 2})` | No      |
| `bool`      | `is_valid = True`                   | No      |
| `NoneType`  | `result = None`                     | N/A     |

---



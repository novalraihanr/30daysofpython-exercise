<!--toc:start-->

- [Comments](#comments)
  - [Single Line Comments](#single-line-comments)
  - [Multiline Comments](#multiline-comments)
- [Data types](#data-types)
  - [Number](#number)
  - [String](#string)
  - [Booleans](#booleans)
  - [List](#list)
  - [Dictionary](#dictionary)
  - [Tuple](#tuple)
  - [Set](#set)
- [Checking Data Types](#checking-data-types)

<!--toc:end-->

# Comments

Comments play a crucial role in enhancing code readability and allowing developers to leave notes within their code.

## Single Line Comments

```python
# This is the first comments
# This is the second comments
# This is the third comments
```

## Multiline Comments

```python
"""This is a Multiline comments
Multiline comment takes multiple lines.
python is eating this world
""""
```

# Data types

## Number

- Integer
  Example: -3, -2, -1, 0, 1, 2, 3

- Float
  Example: -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5

- Complex
  Example: 1 + j, 2 + 4j

## String

```python
'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challange'
```

## Booleans

```python
True # Is the light on? if it is on, then the value is True
False # Is the light on? If it is off, then the value is False
```

## List

Python list is an **ordered** collection which allows to store different data type items.

```python
[0, 1, 2, 3, 4, 5]
['Banana', 'Orange', 'Mango', 'Avocado']
['Banana', 10, False, 9.81]
```

## Dictionary

A Python dictionary object is an **unordered** collection of data in a key value pair format.

```python
{
  'first_name':'Asabeneh',
  'last_name':'Yetayeh',
  'country':'Finland',
  'age':250,
  'is_married':True,
  'skills':['JS', 'React', 'Node', 'Python']
}
```

## Tuple

A tuple is an **ordered** collection of different data types lie list but tuples can not be modified once they are created. They are **Immutable**

```python
{'Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya'}
```

## Set

A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an **ordered** collection of items. Like in Mathematics, set in Python stores only unique items.

```python
{2, 4, 3, 5}
{3.14, 9.81, 2.7}
```

# Checking Data Types

```python
print(type("foo"))
```

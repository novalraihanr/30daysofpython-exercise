# Built in functions

Built-in functions are globally available for your use that mean you can make use of the built-in functions without importing or configuring.
![Built-in Functions](../assets/builtin-functions.png)

# Variables

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen, are not allowed when naming a variable.

Python Variable Name Rules

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

Invalid variables names

```Python
first-name
first@name
first$name
num-1
1num
```

Python developers use snake case (snake_case) variable naming convention. When we assign a certain data type to a variable, it is called variable declaration. The equal sign is an assignment operator.

```python
first-name = 'Noval'
last-name = 'Ramadhan'
```

Print function takes unlimited number of arguments. An argument is a value which we can be passed or put inside the function parenthesis.

```python
print('Hello, World!')
print('Hello', ',', 'World', '!')
print(len('Hello, World!'))
```

## Declaring Multiple Variable in a Line

```python
first-name, last-name, country, age, is_married = 'Noval', 'Ramadhan', 'Indonesia', 20, True

print(first-name, last-name, country, age, is_married)
print('First name:', first-name)
print('Last name: ', last-name)
```

Getting user input using the input() built-in function.

```python
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
```

# Data Types

## Checking Data types and Casting

- Casting: Converting one data type to another data type. We use int(), float(), str(), list, set. When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string.

```python
# int to float
num_int = 10
print('num_int', num_int)
num_float = float(num_int)
print('num_float:', num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

# str to int or float
num_str = '10.6'
num_float = float(num_str)
num_int = int(num_float)
print('num_int', int(num_str))
print('num_float', float(num_str))
num_inst = inst(num_float)
print('num_int', int(num_int))

# str to list
first_name = 'Noval'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)
```

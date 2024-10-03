# Python Notes

## 1. For Loop in Python

A **`for` loop** in Python is used to iterate over a sequence (such as a list, tuple, string) or any other iterable object. It allows you to execute a block of code multiple times, once for each item in the sequence.

### Syntax:

```python
for variable in sequence:
    # Code block to execute
```

### Example:

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

**Output:**

```
apple
banana
cherry
```

### Using `range()` Function:

The `range()` function generates a sequence of numbers, which is often used with `for` loops.

```python
for i in range(5):
    print(i)
```

**Output:**

```
0
1
2
3
4
```

### Loop Control Statements:

- **`break`**: Exits the loop immediately.
- **`continue`**: Skips the current iteration and continues with the next one.
- **`pass`**: Does nothing; acts as a placeholder.

```python
for number in range(10):
    if number == 5:
        break  # Exit the loop when number is 5
    elif number % 2 == 0:
        continue  # Skip even numbers
    print(number)
```

**Output:**

```
1
3
```

---

## 2. Lists in Python

A **list** is a mutable, ordered collection of items in Python. Lists can contain elements of different data types.

### Creating Lists:

```python
# Empty list
my_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, 'hello', 3.14, True]
```

### Accessing Elements:

```python
# Zero-based indexing
first_item = numbers[0]     # 1
last_item = numbers[-1]     # 5
```

### Modifying Lists:

```python
# Changing an element
numbers[0] = 10             # [10, 2, 3, 4, 5]

# Adding elements
numbers.append(6)           # [10, 2, 3, 4, 5, 6]
numbers.insert(1, 15)       # [10, 15, 2, 3, 4, 5, 6]

# Removing elements
numbers.remove(3)           # Removes the first occurrence of 3
popped_item = numbers.pop() # Removes and returns the last item
del numbers[0]              # Deletes the first element
```

### Slicing Lists:

```python
subset = numbers[1:4]       # Elements from index 1 to 3
```

### Iterating Over Lists:

```python
for item in mixed_list:
    print(item)
```

**Output:**

```
1
hello
3.14
True
```

### List Comprehensions:

A concise way to create lists.

```python
squares = [x**2 for x in range(6)]
print(squares)              # [0, 1, 4, 9, 16, 25]
```

---

## 3. Modules in Python

Modules are Python files containing definitions and statements intended for use in other Python programs. They promote code reusability and organization.

### Importing Modules:

- **Import the entire module:**

```python
import math
print(math.sqrt(16))        # 4.0
```

- **Import specific functions or variables:**

```python
from math import pi, sin
print(pi)                   # 3.141592653589793
print(sin(pi/2))            # 1.0
```

- **Import with an alias:**

```python
import numpy as np
array = np.array([1, 2, 3])
```

### Creating Your Own Module:

Any Python file can be treated as a module. For example, if you have a file named `my_module.py`, you can import it:

```python
import my_module
```

Ensure that `my_module.py` is in the same directory as your script or in the Python path.

---

## 4. `tabulate` Function in `tabulate` Module

The `tabulate` module is a third-party library used to display tabular data in a visually appealing format.

### Installation:

```bash
pip install tabulate
```

### Basic Usage:

```python
from tabulate import tabulate

data = [['Alice', 24], ['Bob', 27], ['Charlie', 22]]
headers = ['Name', 'Age']

print(tabulate(data, headers=headers))
```

**Output:**

```
Name      Age
------  -----
Alice     24
Bob       27
Charlie   22
```

### Specifying Table Format:

```python
print(tabulate(data, headers=headers, tablefmt='grid'))
```

**Output:**

```
+----------+-------+
| Name     |   Age |
+==========+=======+
| Alice    |    24 |
+----------+-------+
| Bob      |    27 |
+----------+-------+
| Charlie  |    22 |
+----------+-------+
```

### Available Table Formats:

- `'plain'`
- `'simple'`
- `'grid'`
- `'fancy_grid'`
- `'pipe'`
- `'orgtbl'`
- `'psql'`
- `'rst'`
- `'mediawiki'`
- `'html'`
- `'latex'`

### Aligning Columns:

```python
print(tabulate(data, headers=headers, colalign=("left", "right")))
```

---

## 5. `colored` Function in `termcolor` Module

The `termcolor` module is used to print colored text in the terminal.

### Installation:

```bash
pip install termcolor
```

### Basic Usage:

```python
from termcolor import colored

print(colored('Hello, World!', 'green'))
```

**Output:**

The text `Hello, World!` will appear in green.

### Available Text Colors:

- `'grey'`
- `'red'`
- `'green'`
- `'yellow'`
- `'blue'`
- `'magenta'`
- `'cyan'`
- `'white'`

### Available Text Highlights:

- `'on_grey'`
- `'on_red'`
- `'on_green'`
- `'on_yellow'`
- `'on_blue'`
- `'on_magenta'`
- `'on_cyan'`
- `'on_white'`

### Adding Attributes:

- `'bold'`
- `'dark'`
- `'underline'`
- `'blink'`
- `'reverse'`
- `'concealed'`

### Examples:

```python
# Colored text with background
print(colored('Warning!', 'red', 'on_white'))

# Colored text with attributes
print(colored('Success!', 'green', attrs=['bold', 'underline']))
```

---

### Combining `tabulate` and `termcolor`

You can use both modules together to create colored tables.

```python
from tabulate import tabulate
from termcolor import colored

data = [
    [colored('Alice', 'cyan'), 24],
    [colored('Bob', 'yellow'), 27],
    [colored('Charlie', 'green'), 22]
]
headers = [colored('Name', 'magenta'), colored('Age', 'magenta')]

print(tabulate(data, headers=headers, tablefmt='grid'))
```

**Output:**

A grid-formatted table with colored headers and names.

---

## Summary

- **For Loops**: Essential for iterating over sequences.
- **Lists**: Mutable sequences used to store collections of items.
- **Modules**: Facilitate code organization and reuse; can import built-in or third-party modules.
- **`tabulate` Module**: Formats tabular data for display; supports various table formats.
- **`termcolor` Module**: Adds color to terminal text; supports text colors, highlights, and attributes.

These tools enhance the functionality and aesthetics of Python programs, making code more efficient and outputs more readable.
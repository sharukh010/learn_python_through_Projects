### Python Notes: Variables, Data Types, Operators, Input/Output, Typecasting, and Conditional Statements

#### 1. **Variables in Python**
Variables are containers for storing data values. Python does not require declaring the type of variable explicitly; the interpreter automatically identifies the type based on the value assigned.

- **Syntax:**
  ```python
  variable_name = value
  ```
- **Example:**
  ```python
  name = "Alice"
  age = 25
  price = 99.99
  ```

#### 2. **Data Types**
Python supports various data types to define the type of value a variable holds.

- **Integer (`int`)**: Represents whole numbers.
  ```python
  age = 25
  ```
- **String (`str`)**: Represents text data, enclosed within single, double, or triple quotes.
  ```python
  name = "Alice"
  ```
- **Float (`float`)**: Represents decimal numbers.
  ```python
  price = 99.99
  ```
- **Boolean (`bool`)**: Represents two values: `True` or `False`.
  ```python
  is_student = True
  ```

#### 3. **Arithmetic Operators**
Used to perform mathematical operations:

- `+` : Addition  
- `-` : Subtraction  
- `*` : Multiplication  
- `/` : Division (returns float)  
- `//` : Floor Division (returns integer)  
- `%` : Modulus (returns remainder)  
- `**` : Exponentiation (power)

**Example:**
```python
x = 10
y = 3

add = x + y        # 13
subtract = x - y   # 7
multiply = x * y   # 30
divide = x / y     # 3.33
floor_div = x // y # 3
modulus = x % y    # 1
power = x ** y     # 1000
```

#### 4. **Input and Output**
- **`input()` function:** Takes input from the user as a string.
  ```python
  name = input("Enter your name: ")
  ```
- **`print()` function:** Displays output to the user.
  ```python
  print("Hello, " + name)
  ```

#### 5. **Typecasting**
Converting one data type to another.

- **`int()`**: Converts a value to an integer.
  ```python
  number = int("10")  # Converts string to integer
  ```
- **`float()`**: Converts a value to a float.
  ```python
  price = float("99.99")  # Converts string to float
  ```
- **`str()`**: Converts a value to a string.
  ```python
  age_str = str(25)  # Converts integer to string
  ```

#### 6. **Relational Operators**
Used to compare two values and return a boolean (`True` or `False`).

- `==` : Equal to  
- `!=` : Not equal to  
- `>` : Greater than  
- `<` : Less than  
- `>=` : Greater than or equal to  
- `<=` : Less than or equal to  

**Example:**
```python
x = 5
y = 10

print(x == y)  # False
print(x < y)   # True
print(x != y)  # True
```

#### 7. **Conditional Statements**
Used to execute a block of code based on certain conditions.

- **`if` statement**: Executes a block of code if the condition is `True`.
  ```python
  age = 18
  if age >= 18:
      print("You are eligible to vote.")
  ```
- **`else` statement**: Executes a block of code if the condition in `if` is `False`.
  ```python
  if age >= 18:
      print("You are eligible to vote.")
  else:
      print("You are not eligible to vote.")
  ```
- **`match` statement**: Matches a value against multiple patterns (similar to `switch` in other languages).
  ```python
  command = "start"
  match command:
      case "start":
          print("Starting the system...")
      case "stop":
          print("Stopping the system...")
      case _:
          print("Unknown command")
  ```
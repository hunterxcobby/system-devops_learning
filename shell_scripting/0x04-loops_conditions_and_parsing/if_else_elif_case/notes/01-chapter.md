### 1. **`if` Statement:**
- The `if` statement is used to conditionally execute a block of code based on a specified condition.

**Syntax:**
```bash
if [ condition ]; then
    # Statements to be executed if the condition is true
fi
```

**Example:**
```bash
#!/bin/bash

# Simple if statement
number=10

if [ $number -eq 10 ]; then
    echo "The number is 10."
fi
```

### 2. **`else` Statement:**
- The `else` statement is used in conjunction with `if` to specify a block of code to be executed if the `if` condition is false.

**Syntax:**
```bash
if [ condition ]; then
    # Statements to be executed if the condition is true
else
    # Statements to be executed if the condition is false
fi
```

**Example:**
```bash
#!/bin/bash

# if-else statement
number=5

if [ $number -eq 10 ]; then
    echo "The number is 10."
else
    echo "The number is not 10."
fi
```

### 3. **`elif` Statement:**
- The `elif` statement is used to check additional conditions if the previous `if` and `elif` conditions are false.

**Syntax:**
```bash
if [ condition1 ]; then
    # Statements to be executed if condition1 is true
elif [ condition2 ]; then
    # Statements to be executed if condition2 is true
else
    # Statements to be executed if all conditions are false
fi
```

**Example:**
```bash
#!/bin/bash

# if-elif-else statement
number=7

if [ $number -eq 10 ]; then
    echo "The number is 10."
elif [ $number -eq 5 ]; then
    echo "The number is 5."
else
    echo "The number is neither 10 nor 5."
fi
```

### 4. **`case` Statement:**
- The `case` statement is used for more complex conditional checks, especially when you want to compare a variable against multiple values.

**Syntax:**
```bash
case variable in
    pattern1)
        # Statements to be executed if variable matches pattern1
        ;;
    pattern2)
        # Statements to be executed if variable matches pattern2
        ;;
    *)
        # Statements to be executed if variable does not match any pattern
        ;;
esac
```

**Example:**
```bash
#!/bin/bash

# Case statement
fruit="apple"

case $fruit in
    "apple")
        echo "It's an apple."
        ;;
    "banana")
        echo "It's a banana."
        ;;
    *)
        echo "It's neither an apple nor a banana."
        ;;
esac
```

### 5. **Conclusion:**
- Conditional statements (`if`, `else`, `elif`, and `case`) allow you to control the flow of your script based on certain conditions.
- They are essential for making decisions in your scripts based on variable values or other conditions.

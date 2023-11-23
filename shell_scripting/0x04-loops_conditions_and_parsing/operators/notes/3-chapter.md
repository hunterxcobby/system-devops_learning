The `expr` command in shell scripting is used for evaluating expressions. It can perform various operations, including arithmetic calculations and string comparisons. Here's a brief overview:

1. **Arithmetic Operations:**
   - `expr` can perform basic arithmetic operations such as addition, subtraction, multiplication, division, and modulo.
   - Example:
     ```bash
     result=$(expr 5 + 3)
     echo $result  # Outputs 8
     ```

2. **String Comparison:**
   - It can be used for comparing strings, especially in the context of conditional statements.
   - Example:
     ```bash
     if [ $(expr "$string1" : "$string2") -ne 0 ]; then
       echo "Strings are not equal"
     fi
     ```

3. **Pattern Matching:**
   - `expr` supports pattern matching with regular expressions.
   - Example:
     ```bash
     match=$(expr "$string" : '.*pattern.*')
     ```

4. **Substrings:**
   - It can extract substrings from strings.
   - Example:
     ```bash
     substring=$(expr substr "$string" $start $length)
     ```

5. **Length of a String:**
   - `expr` can be used to find the length of a string.
   - Example:
     ```bash
     length=$(expr length "$string")
     ```

**Note:**
- The use of `expr` has declined in modern shell scripting in favor of more advanced constructs like `$(( ))` for arithmetic operations and `[[ ]]` for string comparisons. These alternatives are more portable and efficient.

While `expr` provides flexibility, its usage is somewhat dated, and you may find more concise and readable alternatives in modern shell scripting practices.
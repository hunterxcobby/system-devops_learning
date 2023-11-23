

**Logical Operators:**

1. **`!` (NOT):**
   - Purpose: Negates the condition. Returns true if the condition is false and vice versa.
   - Example:
     ```bash
     if [ ! -f $FILENAME ]; then
       # Executes if $FILENAME does not exist
     fi
     ```

2. **`&&` (AND):**
   - Purpose: Returns true if both conditions on either side of `&&` are true.
   - Example:
     ```bash
     if [ $condition1 ] && [ $condition2 ]; then
       # Executes if both condition1 and condition2 are true
     fi
     ```

3. **`||` (OR):**
   - Purpose: Returns true if at least one of the conditions on either side of `||` is true.
   - Example:
     ```bash
     if [ $condition1 ] || [ $condition2 ]; then
       # Executes if either condition1 or condition2 is true
     fi
     ```

**Script (Example 8-3):**

1. **Script Purpose:**
   - Demonstrates compound condition tests using `&&` and `||`.

2. **Tests in the Script:**
   - **Test #1:** Checks if both `$a` is 24 and `$b` is 47.
   - **Test #2:** Checks if either `$a` is 98 or `$b` is 47.
   - **Test #3:** Uses alternative `-a` option to test both conditions.
   - **Test #4:** Uses alternative `-o` option to test either condition.
   - **Test #5:** Compares strings, checking if `$a` is "rhino" and `$b` is "crocodile."

3. **Note on `&&` and `||`:**
   - Bash tests the exit status of each statement linked with a logical operator.

4. **Arithmetic Context:**
   - The `&&` and `||` operators also find use in an arithmetic context.

**Examples in Arithmetic Context:**
   ```bash
   echo $(( 1 && 2 ))   # Returns 1 (true && true)
   echo $((3 && 0))     # Returns 0 (true && false)
   echo $((4 || 0))     # Returns 1 (true || false)
   echo $((0 || 0))     # Returns 0 (false || false)
   ```

These logical operators provide powerful tools for creating conditions and controlling the flow of a script based on these conditions.


**Script: Greatest Common Divisor (gcd.sh)**

1. **Purpose:**
   - Finds the greatest common divisor (GCD) of two integers using Euclid's algorithm.

2. **Algorithm Overview:**
   - Euclid's algorithm uses successive division:
     - In each pass, `dividend` becomes `divisor`, and `divisor` becomes `remainder`.
     - This continues until `remainder` becomes 0. The GCD is then the final value of `dividend`.

3. **Argument Check:**
   - Ensures that the script is called with two command-line arguments.

4. **`gcd` Function:**
   - Parameters: Takes two integers, `$1` and `$2`.
   - Variables:
     - `dividend`: Initially set to the larger of the two numbers.
     - `divisor`: Initially set to the smaller of the two numbers.
     - `remainder`: Used to store the remainder of the division.
   - Loop: Continues until `remainder` becomes 0, applying Euclid's algorithm.
   - Result: Prints the GCD of the two input numbers.

5. **Exercises:**
   - Checks for integer command-line arguments and exits with an error message if not.
   - Suggests rewriting the `gcd` function to use local variables.

**Arithmetic Operators:**

1. **`+=`, `-=`, `*=`, `/=`, `%=`:**
   - Purpose: These are compound assignment operators.
   - Examples:
     ```bash
     let "var += 5"   # Increment variable by 5
     let "var *= 4"   # Multiply variable by 4
     ```

2. **Explanation:**
   - `+=`: Increment the variable by a constant.
   - `-=`: Decrement the variable by a constant.
   - `*=`: Multiply the variable by a constant.
   - `/=`: Divide the variable by a constant.
   - `%=`: Calculate the remainder of dividing the variable by a constant.

These compound assignment operators are shortcuts for performing arithmetic operations on variables in a concise manner.


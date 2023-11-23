**Test Operator:**

1. **`= Test Operator:**
   - Purpose: Used in conditional statements to check if two strings are equal.
   - Example:
     ```bash
     if [ "$string1" = "$string2" ]; then
       command
     fi
     ```
   - Safer usage includes prepending "X" to variables to prevent errors if variables are empty.
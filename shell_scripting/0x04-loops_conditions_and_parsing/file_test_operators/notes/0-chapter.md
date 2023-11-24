**File Test Operators:**

1. **`-e`:**
   - Purpose: Returns true if the file exists.
   - Example:
     ```bash
     if [ -e "$filename" ]; then
       # Executes if the file exists
     fi
     ```

2. **`-a`:**
   - Purpose: Identical in effect to `-e`. However, it has been deprecated, and its use is discouraged. It's better to use `-e` for clarity.
   - Example:
     ```bash
     if [ -a "$filename" ]; then
       # Executes if the file exists
     fi
     ```

3. **`-f`:**
   - Purpose: Returns true if the file is a regular file (not a directory or device file).
   - Example:
     ```bash
     if [ -f "$filename" ]; then
       # Executes if the file is a regular file
     fi
     ```

4. **`-s`:**
   - Purpose: Returns true if the file is not zero size (i.e., it has some content).
   - Example:
     ```bash
     if [ -s "$filename" ]; then
       # Executes if the file is not empty
     fi
     ```

5. **`-d`:**
   - Purpose: Returns true if the file is a directory.
   - Example:
     ```bash
     if [ -d "$dirname" ]; then
       # Executes if the file is a directory
     fi
     ```

6. **`-b`:**
   - Purpose: Returns true if the file is a block device.
   - Example:
     ```bash
     if [ -b "$filename" ]; then
       # Executes if the file is a block device
     fi
     ```

These file test operators provide a convenient way to check various attributes of files, allowing you to make decisions in your scripts based on the type or properties of a file. 
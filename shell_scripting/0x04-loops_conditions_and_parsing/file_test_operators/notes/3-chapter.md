
**Ownership and Modification Time File Test Operators:**

1. **`-O`:**
   - **Purpose:** Returns true if you are the owner of the file.
   - **Example:**
     ```bash
     file="/path/to/file"
     if [ -O "$file" ]; then
       echo "You are the owner of $file."
     fi
     ```
     - Checks if you are the owner of the specified file.

2. **`-G`:**
   - **Purpose:** Returns true if the group ID of the file is the same as yours.
   - **Example:**
     ```bash
     file="/path/to/file"
     if [ -G "$file" ]; then
       echo "The group ID of $file is the same as yours."
     fi
     ```
     - Checks if the group ID of the specified file is the same as yours.

3. **`-N`:**
   - **Purpose:** Returns true if the file has been modified since it was last read.
   - **Example:**
     ```bash
     file="/path/to/file"
     if [ -N "$file" ]; then
       echo "$file has been modified since it was last read."
     fi
     ```
     - Checks if the specified file has been modified.

4. **`f1 -nt f2` (Newer Than):**
   - **Purpose:** Returns true if file `f1` is newer than file `f2`.
   - **Example:**
     ```bash
     file1="/path/to/file1"
     file2="/path/to/file2"
     if [ "$file1" -nt "$file2" ]; then
       echo "$file1 is newer than $file2."
     fi
     ```
     - Checks if `file1` is newer than `file2`.

5. **`f1 -ot f2` (Older Than):**
   - **Purpose:** Returns true if file `f1` is older than file `f2`.
   - **Example:**
     ```bash
     file1="/path/to/file1"
     file2="/path/to/file2"
     if [ "$file1" -ot "$file2" ]; then
       echo "$file1 is older than $file2."
     fi
     ```
     - Checks if `file1` is older than `file2`.

6. **`f1 -ef f2` (Same File):**
   - **Purpose:** Returns true if files `f1` and `f2` are hard links to the same file.
   - **Example:**
     ```bash
     file1="/path/to/file1"
     file2="/path/to/file2"
     if [ "$file1" -ef "$file2" ]; then
       echo "$file1 and $file2 are hard links to the same file."
     fi
     ```
     - Checks if `file1` and `file2` are hard links to the same file.

7. **`!`:**
   - **Purpose:** Reverses the sense of the tests above. Returns true if the condition is absent.
   - **Example:**
     ```bash
     file="/path/to/file"
     if [ ! -O "$file" ]; then
       echo "You are not the owner of $file."
     fi
     ```
     - Checks if you are not the owner of the specified file.

These file test operators allow you to check ownership, modification time, and relationships between files.
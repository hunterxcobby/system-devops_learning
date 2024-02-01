In Fabric, the `local` function is used to run commands on the local machine. Here are some examples of how you can use `local`:

1. **Creating a source distribution tar archive for a Python application:**
   ```python
   local("python setup.py sdist --formats=gztar", capture=False)
   ```

2. **Extracting the contents of a tar archive:**
   ```python
   local("tar xzvf /tmp/trunk/app.tar.gz")
   ```

3. **Removing a file:**
   ```python
   local("rm /tmp/trunk/app.tar.gz")
   ```

With `local`, you can execute commands on the local machine, which is useful for tasks like managing local files, running local scripts, or performing other actions on the local system.
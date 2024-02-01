### 1. `local`:
- **Purpose**: Executes a command on the local machine.
- **Usage Example**:
  ```python
  from fabric.api import local
  
  local("ls -l")
  ```

### 2. `run`:
- **Purpose**: Executes a command on remote host(s) using the current user's permissions.
- **Usage Example**:
  ```python
  from fabric.api import run, env
  
  env.hosts = ['user@host1', 'user@host2']  # Define remote hosts
  run("ls -l")
  ```

### 3. `sudo`:
- **Purpose**: Executes a command on remote host(s) using sudo.
- **Usage Example**:
  ```python
  from fabric.api import sudo
  
  sudo("apt-get update")
  ```

### 4. `put`:
- **Purpose**: Uploads a file from the local machine to a remote destination.
- **Usage Example**:
  ```python
  from fabric.api import put
  
  put("local_file.txt", "/remote/path/")
  ```

### 5. `get`:
- **Purpose**: Downloads a file from a remote host to the local machine.
- **Usage Example**:
  ```python
  from fabric.api import get
  
  get("/remote/path/remote_file.txt", "local_file.txt")
  ```

### 6. `prompt`:
- **Purpose**: Prompts the user with text and returns the input (similar to `raw_input`).
- **Usage Example**:
  ```python
  from fabric.api import prompt
  
  user_input = prompt("Enter your name: ")
  ```

### 7. `reboot`:
- **Purpose**: Reboots the remote system and waits for a specified duration before disconnecting.
- **Usage Example**:
  ```python
  from fabric.api import reboot
  
  reboot(wait=30)  # Reboot after 30 seconds
  ```

These Fabric functions provide a powerful yet straightforward way to execute various tasks, whether locally or on remote hosts, making automation and deployment processes smoother and more efficient.
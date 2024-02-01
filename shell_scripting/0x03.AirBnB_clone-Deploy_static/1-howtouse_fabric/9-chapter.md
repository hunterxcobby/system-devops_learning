Roles in Fabric allow you to categorize servers into groups and execute specific actions on servers belonging to a particular role. Here's how you can define and use roles in Fabric:

1. **Define Role Sets:** Start by defining sets of servers as roles using `env.roledefs`. Each role consists of a list of servers.

2. **Set SSH User:** Set the SSH user to be used for connecting to the servers using `env.user`.

3. **Restrict Functions to Roles:** Use the `@roles` decorator to restrict specific functions to be executed only on servers belonging to certain roles.

Here's an example Fabfile demonstrating how to define roles and execute functions on servers based on their roles:

```python
from fabric.api import *

# Define sets of servers as roles
env.roledefs = {
    'webservers': ['www1', 'www2', 'www3', 'www4', 'www5'],
    'databases': ['db1', 'db2']
}

# Set the user to use for SSH
env.user = 'fabuser'

# Define function to get version (example task)
@roles('webservers')
def get_version():
    run('cat /etc/issue')

# Define function to get version on databases as well
@roles('webservers', 'databases')
def get_version():
    run('cat /etc/issue')
```

To execute the `get_version` function on servers belonging to the `webservers` role, you would run:

```bash
$ fab -R webservers get_version
```

To execute the `get_version` function on servers belonging to both the `webservers` and `databases` roles, you would run:

```bash
$ fab get_version
```

You can assign functions to multiple roles by using the `@roles` decorator with a comma-separated list of roles. Additionally, you can include a single server in multiple roles by listing it under different roles in `env.roledefs`.
Connecting to remote servers in Fabric involves setting up the `env` variables `user` and `hosts` to specify the username and list of hosts to connect to. Here's how you can connect to remote servers using Fabric:

1. **Import Fabric API:** Start by importing the Fabric API.

2. **Specify Hosts and User:** Set the `env.user` variable to specify the username used to log in remotely to the servers. Then, set the `env.hosts` variable to a list of hosts to connect to.

3. **Define Tasks:** Define tasks in the Fabfile, each representing a specific action to be executed on the remote servers.

4. **Run Fabric Commands:** Use the `fab` command followed by the task name to execute the defined tasks. Fabric will use the specified username and hosts to connect remotely and execute the commands.

Here's an example Fabfile demonstrating how to connect to a remote server and execute the `uptime` command:

```python
# Import Fabric API
from fabric.api import *

# Specify host(s) and username
env.user = 'username'
env.hosts = ['serverX']

# Define task to show uptime on remote host
def uptime():
    run("uptime")
```

To execute this task on the remote server, you would run:

```bash
$ fab uptime
```

If you have different usernames on different hosts, you can specify them in the `env.hosts` list:

```python
env.user = 'username'
env.hosts = ['userX@192.168.1.1', 'serverX']
```

With this setup, the `'username'` would be used for `'serverX'`, and `'userX'` username would be used for `'192.168.1.1'`.
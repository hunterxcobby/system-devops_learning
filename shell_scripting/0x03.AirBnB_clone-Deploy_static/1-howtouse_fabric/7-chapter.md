Creating a Fabfile involves writing Python functions that define tasks to be executed by Fabric. These tasks can include running shell commands on remote servers, uploading or downloading files, and performing various system administration tasks. Here's a step-by-step guide:

1. **Create a Fabfile:** Start by creating a blank file named `fabfile.py` in the directory where you want to use Fabric commands.

2. **Define Tasks:** Write Python functions in the `fabfile.py`, each representing a specific task. Inside these functions, you can use Fabric's API to execute shell commands on remote servers.

3. **Specify Target Servers:** Optionally, specify the target servers where the tasks will be executed. This can be done using the `-H` option when running Fabric commands.

4. **Execute Tasks:** Use the `fab` command followed by the task name to execute the defined tasks. You can also use `fab --list` to see a list of available commands.

5. **Run Fabric Commands:** When you run Fabric commands, Fabric logs into the specified servers and executes the shell commands defined in the Fabfile. You'll see the output of these commands in the terminal.

Here's an example of a simple Fabfile with a single task:

```python
# fabfile.py
from fabric.api import run

def host_type():
    run('uname -s')
```

To execute this task on one or more servers, you would run:

```bash
$ fab -H localhost,linuxbox host_type
```

This command would execute the `host_type` task on both `localhost` and `linuxbox`, displaying the output of the `uname -s` command for each server.

By following these steps and understanding how to define tasks in a Fabfile, you can effectively use Fabric to automate deployment and system administration tasks.
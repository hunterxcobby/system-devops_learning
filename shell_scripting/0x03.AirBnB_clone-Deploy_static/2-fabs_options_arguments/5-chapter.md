Understanding Roles and Hosts in Fabric:

**Overview**:
- Fabric allows you to specify hosts and roles at the task level using special keyword arguments: `host`, `hosts`, `role`, and `roles`.
- These arguments are used to set per-task host and/or role lists.
- The singular and plural forms of these arguments (`host` vs `hosts`, `role` vs `roles`) behave differently.

**Behavior**:
- These special kwargs are removed from the args/kwargs sent to the task function itself to prevent TypeErrors.
- If both the plural and singular forms are given, the plural form takes precedence.
- When using the plural form (`hosts`, `roles`), semicolons (;) are used to separate host lists to avoid conflicts with commas used to separate other arguments.
- Host lists should be quoted to prevent shell interpretation, especially if special characters like semicolons are involved.

**Example**:
```bash
$ fab new_user:myusername,hosts="host1;host2"
```
In this example, `new_user` function is invoked with the username `myusername`, and it will execute on a list of hosts `['host1', 'host2']`.

Understanding these concepts allows for effective management of hosts and roles when executing tasks in Fabric.
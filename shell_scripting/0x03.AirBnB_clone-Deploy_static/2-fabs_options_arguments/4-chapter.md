Understanding Per-task Arguments in `fab`:

**Overview**:
- Per-task arguments allow you to pass arguments to individual tasks at runtime.
- Syntax: `fab task_name:arg1,arg2,arg3...`

**Syntax Rules**:
- Use a colon (:) to separate the task name from its arguments.
- Use commas (,) to separate arguments from each other.
- Use equals signs (=) for keyword arguments, or omit them for positional arguments.
- Values are treated as strings.
- Backslash (\) is used to escape commas (,) and equals signs (=).

**Example Task**:
```python
def new_user(username, admin='no', comment="No comment provided"):
    print("New User (%s): %s" % (username, comment))
```

**Usage Examples**:
- Positional Arguments:
  - `$ fab new_user:myusername`
- Keyword Arguments:
  - `$ fab new_user:username=myusername`
- Positional and Keyword Arguments:
  - `$ fab new_user:myusername,yes`
  - `$ fab new_user:myusername,admin=yes`
- Escaping Special Characters:
  - `$ fab new_user:myusername,admin=no,comment='Gary\, new developer (starts Monday)'`

These arguments are translated into corresponding Python function calls, allowing flexibility in task execution and parameter passing.
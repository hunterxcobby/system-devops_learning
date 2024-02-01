Understanding Fabric Settings Files:

**Overview**:
- Fabric supports a user settings file, often referred to as `fabricrc`.
- This file contains key-value pairs, one per line, and is used to specify string settings.
- When `fab` runs, it loads this settings file (if found) prior to loading any fabfile, updating the `env` dictionary accordingly.

**Default Location**:
- By default, Fabric looks for `~/.fabricrc` as the user settings file.
- However, this location can be overridden by specifying the `-c` flag to `fab` and providing a custom file path.

**Example**:
Suppose your SSH login username differs from your workstation username. Instead of modifying `env.user` directly in a project's fabfile, you can use a `fabricrc` file. For example:
```plaintext
user = ssh_user_name
```
When running `fab`, your fabfile will load with `env.user` set to `'ssh_user_name'`, ensuring consistency across different users of the fabfile without modifying the fabfile itself.

Understanding and utilizing Fabric settings files allows for cleaner and more flexible configuration management in Fabric projects.
In Fabric, the `reboot` function is used to reboot the remote system. By default, it waits for two minutes (120 seconds) before initiating the reboot. You can also specify a custom wait time before rebooting.

Here are some usage examples:

1. **Reboot the remote system with the default wait time (120 seconds):**
   ```python
   reboot()
   ```

2. **Reboot the remote system after a specific wait time (e.g., 30 seconds):**
   ```python
   reboot(wait=30)
   ```

The `reboot` function simplifies the process of rebooting remote systems, providing a convenient way to perform this action as part of your Fabric scripts.
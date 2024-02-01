Starting, stopping, and reloading Nginx configuration involves using specific commands or signals to manage its processes. Here's a breakdown with examples:

1. **Starting Nginx**:
   - To start Nginx, run the executable file.
   - Example: `nginx`

2. **Controlling Nginx**:
   - Nginx can be controlled using the `-s` parameter followed by a signal.
   - Signals:
     - `stop`: Fast shutdown
     - `quit`: Graceful shutdown
     - `reload`: Reloading the configuration file
     - `reopen`: Reopening the log files
   - Example (graceful shutdown): `nginx -s quit`

3. **Reloading Configuration**:
   - Changes made in the configuration file require a reload to take effect.
   - Example (reload configuration): `nginx -s reload`

4. **Master Process Behavior**:
   - When the master process receives the reload signal:
     - It checks the syntax validity of the new configuration file.
     - Tries to apply the configuration.
     - Starts new worker processes and sends messages to old worker processes to shut down.
     - If successful, new worker processes handle requests while old ones are shut down.
     - If unsuccessful, it rolls back to the old configuration.

5. **Sending Signals with kill**:
   - Unix tools like `kill` can send signals directly to Nginx processes.
   - Example (graceful shutdown): `kill -s QUIT <nginx_master_process_id>`

6. **Listing Running Nginx Processes**:
   - Use the `ps` utility with `grep` to list all running Nginx processes.
   - Example: `ps -ax | grep nginx`

These commands and signals allow you to manage Nginx processes effectively, ensuring smooth operation and configuration updates.
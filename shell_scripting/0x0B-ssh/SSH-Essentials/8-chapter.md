### Navigating the Remote Wilderness - Command Emissary:

1. **Command Expedition - Swift & Direct:**
   - To dispatch a lone command to the remote realm:

     ```bash
     ssh username@remote_host command_to_run
     ```

   - Behold, as the command unfurls and retreats, leaving the remote realm untouched.

2. **Diverging Ports - Uncharted Territories Beckon:**
   - In the realm where port 22 isn't sovereign, chart a course using the -p option:

     ```bash
     ssh -p port_num username@remote_host
     ```

3. **Scribe Your Chronicles - A Local Configuration File:**
   - Inscribe your tales within the ~/.ssh directory. Create or edit the config file:

     ```bash
     nano ~/.ssh/config
     ```

   - Record the wisdom of port numbers, assigning them to hosts:

     ```bash
     Host remote_alias
         HostName remote_host
         Port port_num
     ```


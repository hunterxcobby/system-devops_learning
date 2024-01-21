### Restricting SSH Castle Access - A User-Approved Roster

**Introduction:**
- In our SSH castle, not everyone gets a key. Let's create a VIP roster for authorized users.

**Accessing the Castle Scrolls:**
- Open the sacred configuration scrolls of the SSH daemon: `sudo nano /etc/ssh/sshd_config`.

**Allowing Individual Knights:**
- Look for the `AllowUsers` directive. If absent, inscribe it. List the usernames allowed to enter:
  ```plaintext
  AllowUsers knight1 knight2
  ```
  Save and exit.

**Summoning the Knights:**
- Restart the daemon with the incantation:
  - Ubuntu/Debian: `sudo service ssh restart`
  - CentOS/Fedora: `sudo service sshd restart`

**Orchestrating Groups:**
- If you prefer groups, utilize the `AllowGroups` directive.
  ```plaintext
  AllowGroups sshknights
  ```
  Save and close.

**Creating the Noble Guild:**
- Form a guild with `sudo groupadd -r sshknights`.

**Knighting the Users:**
- Enlist users into the guild:
  ```bash
  sudo usermod -a -G sshknights knight1
  sudo usermod -a -G sshknights knight2
  ```

**Revelation of the Roster:**
- Restart the SSH daemon:
  - Ubuntu/Debian: `sudo service ssh restart`
  - CentOS/Fedora: `sudo service sshd restart`

**Acknowledgment:**
- Only the listed knights can access the SSH castle. Their presence is welcomed, others denied.

**Note:**
- Always ensure the safety of your castle scrolls. Unauthorized changes may lead to chaos.
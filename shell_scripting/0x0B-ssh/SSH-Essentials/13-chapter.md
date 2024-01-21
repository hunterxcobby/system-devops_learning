### Granting Root Access with Vigilance

**Introduction:**
- Bestow the sacred key upon the Root, allowing limited access for sacred rituals while maintaining the castle's security.

**Key Bestowal Ceremony:**
- Invoke the key transfer ritual: `ssh-copy-id root@remote_host`

**Entering the Forbidden Scrolls:**
- Open the forbidden scrolls (root's authorized_keys): `sudo nano /root/.ssh/authorized_keys`

**Crafting the Command Seal:**
- Prefix the key entry with a command seal specifying the ritual path:
  ```plaintext
  command="/path/to/command arg1 arg2" ssh-rsa ...
  ```
  Save and close.

**Fortress Decree Adjustment:**
- Open the fortress decree (sshd_config): `sudo nano /etc/ssh/sshd_config`
- Seek the `PermitRootLogin` directive and modify to allow forced commands only:
  ```plaintext
  PermitRootLogin forced-commands-only
  ```
  Save and close.

**Daemon Reinvigoration:**
- Renew the daemon's energy:
  - Ubuntu/Debian: `sudo service ssh restart`
  - CentOS/Fedora: `sudo service sshd restart`

**Root Access Proclamation:**
- Root access is granted only for specified commands. The castle's sanctity is preserved.

**Note:**
- Ensure command paths are accurate. Misconfiguration may lead to unintended consequences.
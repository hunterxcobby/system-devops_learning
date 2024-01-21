### Forbidding the Root Throne - Strengthening Castle Walls

**Introduction:**
- Guard the castle gates against unwarranted entry. Disabling root login enhances security.

**Entering the Fortress Scrolls:**
- Open the fortress scrolls, the SSH daemon configuration: `sudo nano /etc/ssh/sshd_config`.

**Root Banishment Ritual:**
- Seek the `PermitRootLogin` directive. Uncomment if concealed and set the value to "no":
  ```plaintext
  PermitRootLogin no
  ```
  Save and close.

**Reinforcing the Citadel:**
- Invoke the daemon renewal spell:
  - Ubuntu/Debian: `sudo service ssh restart`
  - CentOS/Fedora: `sudo service sshd restart`

**Acknowledgment:**
- Root entry is now forbidden. Only sworn guardians with designated keys may access the castle.

**Note:**
- Ensure the fortress scrolls are safeguarded. Unauthorized changes may weaken the castle defenses.
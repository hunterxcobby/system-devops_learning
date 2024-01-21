### Changing SSH Port - Unveiling a Secret Entrance

**Why Change the Port:**
- Imagine everyone knows where the secret entrance to a castle is.
- Changing the SSH port is like relocating that entrance, making it harder for intruders.

**Unlocking the Configuration Scroll:**
- To change the SSH port, we need to access the SSH daemon's secret configuration scroll.
- On the server, type `sudo nano /etc/ssh/sshd_config` to open the scroll.

**Discovering the Port Incantation:**
- Search for the line that says `Port 22`. This is where the current secret entrance is.
- Change `22` to a new number, like `4444`. Now, the secret entrance is at Port 4444.

**Saving the Scroll:**
- Save and close the scroll. In nano, it's `Ctrl + X`, then `Y` to confirm, and `Enter` to exit.

**Announcing the Change to the Daemon:**
- Tell the SSH daemon about the new entrance. Restart it with `sudo service ssh restart` (on Ubuntu/Debian) or `sudo service sshd restart` (on CentOS/Fedora).

**Entering the Castle:**
- When connecting, add `-p 4444` to your SSH command. For example, `ssh -p 4444 user@your_server_ip`.

**Congratulations:**
- Now, your server is more secure with a secret entrance known only to those who need to access it.
  
**Remember:**
- Keep track of the new entrance! You'll need to mention the port number every time you connect.

**Next Steps:**
- Explore more strategies to fortify your server's security castle.
### Explanation for Total Beginner:

In this step, we are making changes to the local computer's configuration to test the Nginx server block configurations. This is useful if you are using placeholder domain names and want to access your sites locally for testing. The modification is done by editing the hosts file, which allows you to map domain names to specific IP addresses.

Here's a breakdown:

1. **Editing Local Hosts File:**
   - For Mac or Linux, open the hosts file with `sudo nano /etc/hosts`.
   - For Windows, follow the provided link for instructions.

2. **Adding Entries to Hosts File:**
   - Add entries mapping your server's public IP address to the domain names you configured.
   - Example entries: `203.0.113.5 example.com www.example.com` and `203.0.113.5 test.com www.test.com`.

3. **Saving Changes:**
   - Save and close the hosts file after adding the entries.

### Walkthrough Guide:

1. **Open Hosts File:**
   - On Mac or Linux, run `sudo nano /etc/hosts` in the terminal.
   - On Windows, follow the provided instructions in the link.

2. **Add Entries:**
   - Add lines with your server's IP address and domain names. For example:
     ```
     127.0.0.1   localhost
     . . .
     203.0.113.5 example.com www.example.com
     203.0.113.5 test.com www.test.com
     ```
3. **Save and Close:**
   - Save changes by pressing `CTRL+O` (for nano) and exit with `CTRL+X`.

Now, your local computer will direct requests for the specified domains to your server's IP address, allowing you to test your Nginx configurations locally. Keep in mind that this only affects your local machine and won't impact external users.

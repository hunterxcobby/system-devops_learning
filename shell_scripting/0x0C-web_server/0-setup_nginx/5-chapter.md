### Explanation for Total Beginner:

In this step, we are enabling the server blocks we configured in the previous steps. We create symbolic links from the configuration files in the `sites-available` directory to the `sites-enabled` directory. This is where Nginx looks for active server block configurations during startup.

Here's a breakdown:

1. **Creating Symbolic Links:**
   - `sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/`: Creates a symbolic link for "example.com".
   - `sudo ln -s /etc/nginx/sites-available/test.com /etc/nginx/sites-enabled/`: Creates a symbolic link for "test.com".
   - These links enable Nginx to read the configurations from the `sites-enabled` directory.

2. **Adjusting Nginx Configuration:**
   - We modify the `server_names_hash_bucket_size` in the main Nginx configuration file (`/etc/nginx/nginx.conf`) to avoid potential memory issues.
   - Uncomment the line by removing the `#` symbol to activate this setting.

3. **Testing Nginx Configuration:**
   - `sudo nginx -t`: Tests the Nginx configuration for syntax errors.
   - If no errors are found, the configuration is valid.

4. **Restarting Nginx:**
   - `sudo systemctl restart nginx`: Restarts the Nginx service to apply the changes.
   - Nginx now reads the enabled server blocks and responds accordingly.

### Walkthrough Guide:

1. **Create Symbolic Links:**
   - Run `sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/` to link "example.com".
   - Run `sudo ln -s /etc/nginx/sites-available/test.com /etc/nginx/sites-enabled/` to link "test.com".

2. **Adjust Nginx Configuration:**
   - Open the Nginx configuration file with `sudo nano /etc/nginx/nginx.conf`.
   - Find `server_names_hash_bucket_size` and uncomment the line by removing the `#` symbol.
   - Save and exit the text editor.

3. **Test Nginx Configuration:**
   - Run `sudo nginx -t` to check for syntax errors.

4. **Restart Nginx:**
   - If no errors, restart Nginx with `sudo systemctl restart nginx`.

Now, Nginx is set up to serve both "example.com" and "test.com" based on the configurations you've provided.


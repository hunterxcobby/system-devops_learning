
In this step, we are creating server block configuration files for each of our domains in Nginx. Server blocks act as virtual hosts, defining how Nginx should handle requests for a specific domain.

Here's a breakdown:

1. **Creating Server Block File for "example.com":**
   - `sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/example.com`: This command copies the default Nginx server block configuration to a new file for "example.com".
   - `sudo nano /etc/nginx/sites-available/example.com`: Opens the new file in a text editor to modify its content.

2. **Server Block Configuration File for "example.com":**
   - The file initially looks like a basic server block configuration.
   - Adjustments are made to the `listen`, `root`, and `server_name` directives.
   - The `listen` directive specifies the port and IP to listen on.
   - The `root` directive points to the document root for "example.com".
   - The `server_name` directive defines the domain and any aliases.

3. **Creating Server Block File for "test.com":**
   - `sudo cp /etc/nginx/sites-available/example.com /etc/nginx/sites-available/test.com`: Copies the "example.com" server block configuration to a new file for "test.com".
   - `sudo nano /etc/nginx/sites-available/test.com`: Opens the new file for editing.

4. **Server Block Configuration File for "test.com":**
   - Similar adjustments are made to the `listen`, `root`, and `server_name` directives.
   - The `listen` directive specifies the port and IP to listen on.
   - The `root` directive points to the document root for "test.com".
   - The `server_name` directive defines the domain and any aliases.

### Walkthrough Guide:

1. **Create Server Block File for "example.com":**
   - Copy the default configuration with `sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/example.com`.
   - Open the new file for editing with `sudo nano /etc/nginx/sites-available/example.com`.

2. **Adjustments for "example.com":**
   - Modify the `listen`, `root`, and `server_name` directives to suit "example.com".
   - Save and exit the text editor.

3. **Create Server Block File for "test.com":**
   - Copy the configuration for "example.com" with `sudo cp /etc/nginx/sites-available/example.com /etc/nginx/sites-available/test.com`.
   - Open the new file for editing with `sudo nano /etc/nginx/sites-available/test.com`.

4. **Adjustments for "test.com":**
   - Modify the `listen`, `root`, and `server_name` directives to suit "test.com".
   - Save and exit the text editor.

Now, you have created server block configuration files for both "example.com" and "test.com". These files define how Nginx should handle requests for each domain.


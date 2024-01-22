In this step, we are setting up the directory structure for multiple websites on an Nginx server. By default, Nginx serves documents from the `/var/www/html` directory, but since we want to host multiple sites, we're creating separate directories for each site within the `/var/www` directory.

Here's what each part does:

1. **Creating Directories:**
   - `sudo mkdir -p /var/www/example.com/html`: This command creates a directory structure for a site named "example.com". The `-p` flag ensures that parent directories are created if they don't exist.
   - `sudo mkdir -p /var/www/test.com/html`: Similarly, this command creates a directory structure for a site named "test.com".

2. **Setting Ownership:**
   - `sudo chown -R $USER:$USER /var/www/example.com/html`: This command assigns ownership of the "example.com" directory to your user account. The `$USER` variable represents your current username.
   - `sudo chown -R $USER:$USER /var/www/test.com/html`: Similarly, this command assigns ownership of the "test.com" directory to your user account.

3. **Setting Permissions:**
   - `sudo chmod -R 755 /var/www`: This command sets the permissions for the `/var/www` directory and its subdirectories. It ensures that the owner has read, write, and execute permissions, while others have read and execute permissions.

### Walkthrough Guide:

1. **Creating Site Directories:**
   - Use `sudo mkdir -p /var/www/example.com/html` to create a directory structure for a site named "example.com".
   - Use `sudo mkdir -p /var/www/test.com/html` to create a directory structure for a site named "test.com".

2. **Setting Ownership:**
   - Run `sudo chown -R $USER:$USER /var/www/example.com/html` to give ownership of the "example.com" directory to your user.
   - Run `sudo chown -R $USER:$USER /var/www/test.com/html` to give ownership of the "test.com" directory to your user.

3. **Setting Permissions:**
   - Ensure correct permissions by running `sudo chmod -R 755 /var/www`.

Now, you've established the directory structure for your websites, making it easier to manage and organize content. This sets the foundation for hosting multiple sites on your Nginx server.
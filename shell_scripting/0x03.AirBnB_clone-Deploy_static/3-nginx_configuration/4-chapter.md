To serve static content using Nginx, follow these steps:

1. **Create Directories and Files**:
   - Create `/data/www` directory for HTML files and `/data/images` for images.
   - Place an `index.html` file in `/data/www` with your desired content.
   - Add some images to `/data/images`.

2. **Edit Configuration File**:
   - Open the Nginx configuration file. It's usually located at `/usr/local/nginx/conf/nginx.conf`, `/etc/nginx/nginx.conf`, or `/usr/local/etc/nginx/nginx.conf`.
   - Inside the `http` block, add a new `server` block:

     ```nginx
     http {
         server {
         }
     }
     ```

3. **Configure Server Block**:
   - Within the `server` block, add two `location` blocks to define how requests should be handled:

     ```nginx
     server {
         location / {
             root /data/www;
         }

         location /images/ {
             root /data;
         }
     }
     ```

4. **Explanation**:
   - The first `location` block handles requests without a specific path (`/`). It serves files from the `/data/www` directory.
   - The second `location` block handles requests starting with `/images/`. It serves files from the `/data/images` directory.
   - Nginx prioritizes `location` blocks with longer prefix matches, so requests starting with `/images/` will be handled by the second block.

5. **Reload Configuration**:
   - To apply the new configuration, reload Nginx by running:

     ```bash
     nginx -s reload
     ```

6. **Troubleshooting**:
   - If there are issues, check the `access.log` and `error.log` files in `/usr/local/nginx/logs` or `/var/log/nginx` for details.

With these steps, Nginx will serve static content from the specified directories based on the request paths.
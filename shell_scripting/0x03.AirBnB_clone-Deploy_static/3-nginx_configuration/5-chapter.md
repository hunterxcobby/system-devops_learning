To set up a basic proxy server using Nginx, follow these steps:

1. **Define Proxied Server**:
   - Add a new server block to Nginx's configuration file (`nginx.conf`). This block defines the server that will be proxied.
   
   ```nginx
   server {
       listen 8080;
       root /data/up1;

       location / {
       }
   }
   ```

   - This server listens on port 8080 and serves files from the `/data/up1` directory.

2. **Create Proxied Server Directory**:
   - Create the `/data/up1` directory and place an `index.html` file in it.

3. **Configure Proxy Server**:
   - Modify the existing server configuration to make it a proxy server. Update the first `location` block to include the `proxy_pass` directive with the URL of the proxied server.
   
   ```nginx
   server {
       location / {
           proxy_pass http://localhost:8080;
       }

       location /images/ {
           root /data;
       }
   }
   ```

   - Modify the second `location` block to match image requests with specific file extensions and serve them from the `/data/images` directory.
   
   ```nginx
   location ~ \.(gif|jpg|png)$ {
       root /data/images;
   }
   ```

4. **Regular Expression for Images**:
   - This `location` block uses a regular expression to match URIs ending with `.gif`, `.jpg`, or `.png`.

5. **Final Configuration**:
   - The resulting configuration routes image requests to `/data/images` and passes all other requests to the proxied server.

6. **Apply Configuration**:
   - Reload Nginx to apply the new configuration.

By following these steps, you'll have set up a basic proxy server with Nginx, routing requests to different destinations based on specific criteria.
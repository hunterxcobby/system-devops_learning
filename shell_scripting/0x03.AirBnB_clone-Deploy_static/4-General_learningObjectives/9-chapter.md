In an Nginx configuration, both the `root` and `alias` directives are used to specify the location of files on the server, but they serve different purposes:

1. **root Directive**:
   - The `root` directive sets the root directory for requests.
   - It appends the URI to the specified path to determine the file's location.
   - When a request is made, Nginx looks for files relative to the root directory.
   - It is typically used to serve static files like HTML, CSS, JavaScript, and images.
   - Example:
     ```
     server {
         root /var/www/html;
     }
     ```

2. **alias Directive**:
   - The `alias` directive sets an alternative location for requests.
   - It replaces part of the request URI with a specified directory.
   - It doesn't append the URI to the specified path; instead, it replaces the part of the URI that matches the location block with the specified directory.
   - It is useful for serving files from a different directory or hiding the actual file structure.
   - Example:
     ```
     server {
         location /images/ {
             alias /var/www/images/;
         }
     }
     ```

**Difference**:
- The key difference between `root` and `alias` is how they handle the URI when determining the file's location:
  - With `root`, the URI is appended to the root directory to determine the file's location.
  - With `alias`, the part of the URI that matches the location block is replaced with the specified directory to determine the file's location.

**Example**:
- Suppose there's a request for `/images/pic.jpg`:
  - With `root`, Nginx looks for the file at `/var/www/html/images/pic.jpg`.
  - With `alias`, Nginx looks for the file at `/var/www/images/pic.jpg`.

In summary, while both `root` and `alias` directives specify the location of files, they differ in how they handle the URI and determine the file's actual location on the server.
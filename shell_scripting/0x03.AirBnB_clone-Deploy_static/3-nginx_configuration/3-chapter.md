The configuration file of Nginx is structured around directives, which control its behavior. These directives can be categorized into two types: simple and block directives.

1. **Simple Directives**:
   - Format: `<directive_name> parameters;`
   - Example: `worker_processes 4;`
   - Explanation: Specifies the number of worker processes.

2. **Block Directives**:
   - Format: `<directive_name> { additional_instructions }`
   - Example: 
     ```
     server {
         listen 80;
         server_name example.com;
         location / {
             root /var/www/html;
         }
     }
     ```
   - Explanation: Defines a server block with instructions for handling requests.

Directives can be nested within each other to form contexts. Some common contexts include:
   - `events`
   - `http`
   - `server`
   - `location`

Directives placed outside of any contexts are considered to be in the main context. For example, `events` and `http` directives reside in the main context, `server` directives reside within `http`, and `location` directives reside within `server`.

Comments in the configuration file are denoted by the `#` sign, and anything after it on the same line is ignored by Nginx, making it useful for adding explanatory notes or annotations to the configuration.
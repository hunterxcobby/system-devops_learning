
In this step, we are creating simple web pages for each of our sites to have something to display when visitors access them. We'll create an "index.html" file for both "example.com" and "test.com".

Here's a breakdown:

1. **Creating Index Page for "example.com":**
   - `nano /var/www/example.com/html/index.html`: This command opens a text editor to create an "index.html" file for the "example.com" site.
   - Inside the file, we're adding basic HTML to indicate that the server block for "example.com" is working.

2. **Sample HTML for "example.com":**
   ```html
   <html>
       <head>
           <title>Welcome to Example.com!</title>
       </head>
       <body>
           <h1>Success! The example.com server block is working!</h1>
       </body>
   </html>
   ```
   - This HTML creates a simple page with a heading indicating success.

3. **Copying Index Page for "test.com":**
   - `cp /var/www/example.com/html/index.html /var/www/test.com/html/`: This copies the "index.html" file from "example.com" to "test.com".

4. **Editing Index Page for "test.com":**
   - `nano /var/www/test.com/html/index.html`: This opens the copied file for "test.com" in a text editor.
   - Modify the file to indicate that the server block for "test.com" is working.

5. **Sample HTML for "test.com":**
   ```html
   <html>
       <head>
           <title>Welcome to Test.com!</title>
       </head>
       <body>
           <h1>Success! The test.com server block is working!</h1>
       </body>
   </html>
   ```
   - Similar to "example.com", this HTML indicates success for the "test.com" server block.

### Walkthrough Guide:

1. **Create Index Page for "example.com":**
   - Use `nano /var/www/example.com/html/index.html` to open a text editor.
   - Inside, create the HTML content for the "example.com" page. Save and exit.

2. **Copy Index Page for "test.com":**
   - Copy the "index.html" from "example.com" to "test.com" with `cp /var/www/example.com/html/index.html /var/www/test.com/html/`.

3. **Edit Index Page for "test.com":**
   - Open the copied file for "test.com" with `nano /var/www/test.com/html/index.html`.
   - Modify the HTML content to indicate success for "test.com". Save and exit.

Now, you have created basic web pages for both sites. Visitors to "example.com" will see a message indicating success for that site, and the same for "test.com".
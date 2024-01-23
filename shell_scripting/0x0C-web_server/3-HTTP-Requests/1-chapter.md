## REDIRECTIONS

#### 1. **301 Redirect ("Moved Permanently") - Recommended for SEO:**
   - **Purpose:** Indicates that the requested resource has been permanently moved to a new location.
   - **Use Case:** Ideal for situations where a webpage's URL has changed permanently.
   - **SEO Impact:** Transfers the original page's SEO ranking to the new URL, as search engines update their indexes.

#### 2. **302 Redirect ("Found" or "Moved Temporarily"):**
   - **Purpose:** Signifies that the requested resource has been temporarily moved to another location.
   - **Use Case:** Suitable for temporary changes; the original URL is expected to be used again in the future.
   - **SEO Impact:** Search engines may not transfer the original page's ranking to the new URL.

#### 3. **Meta Refresh Redirect:**
   - **Purpose:** Uses an HTML meta tag to instruct the browser to automatically refresh to a different URL after a specified time.
   - **Use Case:** Often used for automatic page redirection or when JavaScript or server-side redirects are not available.
   - **SEO Impact:** Can be less SEO-friendly compared to server-side redirects, as search engines may interpret it differently.

### Implementation:

#### Server-Side Redirects:
   - **Nginx Example (301 Redirect):**
     ```nginx
     server {
         listen 80;
         server_name olddomain.com;
         return 301 http://newdomain.com$request_uri;
     }
     ```
   - **Nginx Example (302 Redirect):**
     ```nginx
     server {
         listen 80;
         server_name olddomain.com;
         return 302 http://temporarydomain.com$request_uri;
     }
     ```

#### Meta Refresh Redirect:
   - **HTML Example (Meta Refresh):**
     ```html
     <meta http-equiv="refresh" content="0;url=http://example.com">
     ```

Understanding and correctly implementing redirects is crucial for maintaining website integrity during URL changes or updates. If you have specific questions or scenarios, feel free to ask for further clarification!
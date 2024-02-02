In this example of Round Robin DNS, let's break down how requests to google.com are distributed among multiple servers:

1. **Initial DNS Query**:
   - When you initially type `http://google.com/` in your browser, a DNS query is made to resolve the domain name `google.com` to its corresponding IP address(es).

2. **DNS Response**:
   - The DNS server returns multiple IP addresses associated with `google.com`. For example:
     ```
     google.com has address 74.125.53.100
     google.com has address 74.125.45.100
     google.com has address 74.125.67.100
     ```
     This means there are three IP addresses associated with `google.com`.

3. **Request Distribution**:
   - Each time a user makes a request to `google.com`, the DNS resolver alternates between the available IP addresses. For instance:
     - First request: Sent to `74.125.53.100`, which displays the Google search homepage.
     - Subsequent requests: The DNS resolver rotates the order of IP addresses, so the next request might go to `74.125.67.100`, and then `74.125.45.100`, and so on.

4. **Load Balancing**:
   - By distributing requests among multiple servers (`74.125.53.100`, `74.125.45.100`, `74.125.67.100`), Google effectively spreads the load across its server infrastructure. This prevents any single server from being overloaded with traffic and helps maintain performance and availability.

5. **Common Usage**:
   - Large websites like Google, Amazon, and Yahoo utilize Round Robin DNS to manage the high volume of incoming requests efficiently. This technique is particularly beneficial for websites with millions of unique hits per day.

In essence, Round Robin DNS allows large websites to optimize their server resources, distribute incoming traffic evenly, and ensure a smoother user experience by rotating requests among multiple servers.
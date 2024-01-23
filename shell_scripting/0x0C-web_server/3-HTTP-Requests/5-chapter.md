### **Meta Refresh: Overview**

#### **Definition:**
- **Type:** Page-Level Redirect
- **Execution:** Executed at the Page Level using HTML `<meta>` tag.

#### **Key Characteristics:**
1. **Page-Level Redirect:**
   - Meta refresh operates at the page level rather than the server level, using the `<meta>` tag in HTML.

2. **Delay Mechanism:**
   - Often involves a delay mechanism, commonly seen as a countdown (e.g., "If you are not redirected in five seconds, click here").

3. **Link Equity Pass:**
   - Does pass some link equity to the redirected page.

4. **SEO Implications:**
   - Not a recommended SEO technique due to poor usability and potential loss of link equity.

#### **Example Implementation:**
```html
<meta http-equiv="refresh" content="5;url=https://example.com">
```
   - The above example redirects the page to "https://example.com" after a 5-second delay.

#### **Considerations:**
1. **Usability Concerns:**
   - Meta refreshes with countdowns can lead to a suboptimal user experience.

2. **SEO Best Practices:**
   - Generally not recommended for SEO due to potential loss of link equity and usability issues.

### **Conclusion:**
Meta refresh is a page-level redirect method achieved through the HTML `<meta>` tag. While it does pass some link equity, it is often discouraged for SEO purposes because of usability concerns and the availability of more SEO-friendly redirection methods, such as 301 or 302 redirects.
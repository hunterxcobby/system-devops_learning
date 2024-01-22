Before setting up Nginx, it needs to be installed on your server. Installing Nginx involves using package management tools to download and install the necessary files. Below are the steps:

1. **Update Package List:**
   - `sudo apt update`: This command updates the list of available packages on your Ubuntu system.

2. **Install Nginx:**
   - `sudo apt install nginx`: This command installs Nginx on your server. You may be prompted to confirm the installation by typing 'Y' and then pressing 'Enter'.

3. **Start Nginx:**
   - `sudo service nginx start`: This command starts the Nginx service. After this step, Nginx will be up and running on your server.

4. **Enable Nginx at Boot:**
   - `sudo systemctl enable nginx`: This ensures that Nginx starts automatically when your server reboots.

### Walkthrough Guide:

1. **Update Package List:**
   - Run `sudo apt update` to make sure your package list is up-to-date.

2. **Install Nginx:**
   - Run `sudo apt install nginx` to download and install Nginx on your server. Confirm the installation if prompted.

3. **Start Nginx:**
   - After installation, start Nginx by running `sudo service nginx start`. This launches the Nginx service.

4. **Enable Nginx at Boot:**
   - Ensure Nginx starts automatically on boot by running `sudo systemctl enable nginx`.
6

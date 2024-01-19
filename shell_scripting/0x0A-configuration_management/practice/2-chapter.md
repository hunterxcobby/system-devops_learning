Let's enhance your Puppet skills further. In this step, we'll explore how to parameterize your Puppet manifest to make it more flexible.

### Project: Parameterize Web Server Configuration

**Step 1: Update Puppet Manifest**
- Modify `site.pp` to accept parameters for the web page content and the web server port:

  ```puppet
# Define parameters
$web_content = 'Hello, Puppet Web Server!'
$web_port    = 8080  # Change to your desired port, e.g., 8080

# Install Apache
package { 'apache2':
  ensure => installed,
}

# Configure Apache service
service { 'apache2':
  ensure  => running,
  enable  => true,
}

# Create web page
file { '/var/www/html/index.html':
  ensure  => file,
  content => $web_content,
}

# Update default Apache port and bind to localhost
file { '/etc/apache2/ports.conf':
  ensure  => present,
  content => "Listen $web_port\n",
  notify  => Service['apache2'],
}

# Configure VirtualHost for localhost
file { '/etc/apache2/sites-available/localhost.conf':
  ensure  => present,
  content => "
    <VirtualHost *:$web_port>
        DocumentRoot /var/www/html
        ServerName localhost
        ServerAlias 127.0.0.1
    </VirtualHost>
  ",
  notify  => Service['apache2'],
  require => File['/etc/apache2/ports.conf'],
}

# Enable the VirtualHost
file { '/etc/apache2/sites-enabled/localhost.conf':
  ensure  => link,
  target  => '/etc/apache2/sites-available/localhost.conf',
  require => File['/etc/apache2/sites-available/localhost.conf'],
}
  ```

**Step 2: Apply Puppet Manifest with Parameters**
- Apply the updated manifest, providing values for the parameters:
  ```bash
  sudo puppet apply --var 'web_content="Welcome to My Puppet Web Server!"' --var 'web_port=8080' ~/site.pp
  ```

**Step 3: Verify Configuration**
- Access the web server at `http://your_server_ip:8080`. Confirm that the new content is displayed.

**Explanation:**
- We added two parameters (`$web_content` and `$web_port`) at the beginning of the manifest.
- The parameters are then used throughout the manifest, allowing for easy customization.
- When applying the manifest, we provided values for the parameters using the `--var` option.


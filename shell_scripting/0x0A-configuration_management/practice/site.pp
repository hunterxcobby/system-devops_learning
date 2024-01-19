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

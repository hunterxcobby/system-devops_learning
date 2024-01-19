
package { 'apache2':
    ensure => installed,
}

service { 'apache2':
  ensure  => running,
  enable  => true,
}

file { '/var/www/html/':
  ensure => directory,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello, Puppet Web Server!',
}
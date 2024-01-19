### Chapter 5: Puppet Variables and Facts

**Understanding Puppet Variables:**
Variables in Puppet allow you to parameterize your manifests, making them more flexible and reusable.

**Declaring Variables:**
In Puppet, you declare variables using the `$` symbol. For example:

```puppet
$web_server_port = 80

class mymodule {
  file { '/etc/nginx/nginx.conf':
    content => "listen ${web_server_port};",
  }
}
```

Here, `$web_server_port` is a variable holding the web server port.

**Using Variables:**
You can use variables in resource declarations, templates, and other parts of your Puppet code.

```puppet
file { '/etc/nginx/nginx.conf':
  content => "listen ${web_server_port};",
}
```

**Puppet Facts:**
Facts are pieces of information about the system Puppet is managing. Puppet automatically collects facts, and you can use them in your manifests.

**Accessing Facts:**
To access a fact, use the `$facts` variable:

```puppet
$os_family = $facts['os']['family']
```

Here, `$os_family` stores the operating system family.

**Common Facts:**
- `$facts['os']['family']`: Operating system family (e.g., Debian, RedHat).
- `$facts['fqdn']`: Fully Qualified Domain Name.
- `$facts['ipaddress']`: Primary IP address.

**Using Facts in Conditionals:**
```puppet
if $facts['os']['family'] == 'Debian' {
  package { 'nginx':
    ensure => 'present',
  }
} elsif $facts['os']['family'] == 'RedHat' {
  package { 'httpd':
    ensure => 'present',
  }
}
```

This installs Nginx on Debian-based systems and Apache HTTP Server on RedHat-based systems.


### Chapter 3: Puppet Manifests and Classes

**Understanding Puppet Manifests:**
In Puppet, a manifest is a file containing Puppet code that describes the desired system configuration. Manifests typically have a `.pp` extension. Here's a simple example:

```puppet
# This is a basic Puppet manifest
file { '/tmp/example.txt':
  content => 'Hello, Puppet!',
}
```

This manifest uses a `file` resource to ensure a file exists at `/tmp/example.txt` with the specified content.

**Organizing Manifests:**
As your infrastructure grows, organizing manifests becomes crucial. You can split your code into multiple files and directories. For instance, you might have a manifest for the web server, another for the database, and so on.

**Example Directory Structure:**
```
manifests/
|-- webserver.pp
|-- database.pp
|-- init.pp
```

The `init.pp` file is a special entry point for Puppet in each directory.

**Using Classes:**
Classes are a way to group related resources together. For example, you might have a `webserver` class that includes all resources related to your web server.

**Example Class in `webserver.pp`:**
```puppet
class webserver {
  file { '/var/www/html/index.html':
    content => 'Hello, Puppet Webserver!',
  }

  package { 'apache2':
    ensure => installed,
  }

  service { 'apache2':
    ensure => running,
    enable => true,
  }
}
```

**Including Classes:**
You include a class in your main manifest or another class like this:

```puppet
include webserver
```

This ensures all resources defined in the `webserver` class are applied.

**Next:** Now that you have a grasp of Puppet manifests and organizing your configuration
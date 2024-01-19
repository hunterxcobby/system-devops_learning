### Chapter 6: Puppet Modules

**Understanding Puppet Modules:**
Modules in Puppet help organize and structure your code. They contain manifests, files, templates, and other necessary components.

**Creating a Module:**
1. Create a directory for your module in the Puppet modules directory (e.g., `/etc/puppetlabs/code/environments/production/modules`).

2. Inside the module directory, create a `manifests` subdirectory. Create a manifest file (e.g., `init.pp`) inside it.

3. Define your module in the manifest file:

```puppet
# /etc/puppetlabs/code/environments/production/modules/mymodule/manifests/init.pp
class mymodule {
  # Your module code here
}
```

**Using a Module:**
Include a module in your main manifest (e.g., `site.pp`) using the `include` keyword:

```puppet
# /etc/puppetlabs/code/environments/production/manifests/site.pp
include mymodule
```

**Module Structure:**
A standard module structure includes the `manifests` directory for Puppet code, and optionally:
- `files`: Static files needed by your module.
- `templates`: Template files.
- `lib`: Custom Ruby code.
- `facts.d`: External facts.

**Module Best Practices:**
- Keep modules small and focused on specific tasks.
- Use parameters to make modules more flexible.
- Follow a naming convention for consistency.

**Module Parameters:**
Parameters allow customization of module behavior. Define parameters in your module:

```puppet
class mymodule (
  $web_server_port = 80,
) {
  file { '/etc/nginx/nginx.conf':
    content => "listen ${web_server_port};",
  }
}
```

**Using a Parameterized Module:**
Include the module with parameters:

```puppet
class { 'mymodule':
  web_server_port => 8080,
}
```

This overrides the default port.


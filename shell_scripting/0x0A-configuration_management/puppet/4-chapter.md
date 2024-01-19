### Chapter 4: Puppet Modules and Code Reusability

**Understanding Puppet Modules:**
Puppet modules are a way to organize and share Puppet code. A module typically includes manifests, templates, files, and other necessary components. Modules enhance code reusability and maintainability.

**Creating a Simple Module:**
1. Create a directory structure for your module:

   ```
   mymodule/
   |-- manifests/
   |   |-- init.pp
   |-- files/
   |   |-- myfile.txt
   ```

2. Define a simple manifest in `init.pp`:

   ```puppet
   # mymodule/manifests/init.pp
   class mymodule {
     file { '/tmp/myfile.txt':
       source => 'puppet:///modules/mymodule/myfile.txt',
     }
   }
   ```

3. Place the file you want to distribute in the `files` directory.

**Using Modules:**
To use a module in your main manifest, simply include it:

```puppet
include mymodule
```

This fetches the `mymodule` class and applies its resources.

**Puppet Forge:**
Puppet Forge is a repository for Puppet modules. You can find and share modules with the community. Install modules using the `puppet module install` command.

**Example Module Install:**
```bash
puppet module install puppetlabs-apache
```

This installs the Apache module from Puppet Forge.

**Code Reusability with Modules:**
Modules promote code reusability. For example, if you have a common set of configurations for a web server, you can create a module for it. This module can be reused across different nodes.

**Next:** Now that you understand the basics of Puppet modules,
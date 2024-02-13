Step 2 — Configuring the Source Database
In order for your source MySQL database to begin replicating data, you need to make a few changes to its configuration.

On Ubuntu 20.04, the default MySQL server configuration file is named mysqld.cnf and can be found in the /etc/mysql/mysql.conf.d/ directory. Open this file on the source server with your preferred text editor. Here, we’ll use nano:

sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
Within the file, find the bind-address directive. It will look like this by default:

/etc/mysql/mysql.conf.d/mysqld.cnf
. . .
bind-address            = 127.0.0.1
. . .
127.0.0.1 is an IPv4 loopback address that represents localhost, and setting this as the value for the bind-address directive instructs MySQL to only listen for connections on the localhost address. In other words, this MySQL instance will only be able to accept connections that originate from the server where it’s installed.

Remember that you’re turning your other MySQL instance into a replica of this one, so the replica must be able to read whatever new data gets written to the source installation. To allow this, you must configure your source MySQL instance to listen for connections on an IP address which the replica will be able to reach, such as the source server’s public IP address.

Replace 127.0.0.1 with the source server’s IP address. After doing so, the bind-address directive will look like this, with your own server’s IP address in place of source_server_ip:

/etc/mysql/mysql.conf.d/mysqld.cnf
. . .
bind-address            = source_server_ip
. . .
Next, find the server-id directive, which defines an identifier that MySQL uses internally to distinguish servers in a replication setup. Every server in a replication environment, including the source and all its replicas, must have their own unique server-id value. This directive will be commented out by default and will look like this:

/etc/mysql/mysql.conf.d/mysqld.cnf
. . .
# server-id             = 1
. . .
Uncomment this line by removing the pound sign (#). You can choose any number as this directive’s value, but remember that the number must be unique and cannot match any other server-id in your replication group. To keep things simple the following example leaves this value as the default, 1:

/etc/mysql/mysql.conf.d/mysqld.cnf
. . .
server-id               = 1
. . .
Below the server-id line, find the log_bin directive. This defines the base name and location of MySQL’s binary log file.

When commented out, as this directive is by default, binary logging is disabled. Your replica server must read the source’s binary log file so it knows when and how to replicate the source’s data, so uncomment this line to enable binary logging on the source. After doing so, it will look like this:

/etc/mysql/mysql.conf.d/mysqld.cnf
. . .
log_bin                       = /var/log/mysql/mysql-bin.log
. . .
Lastly, scroll down to the bottom of the file to find the commented-out binlog_do_db directive:

/etc/mysql/mysql.conf.d/mysqld.cnf
. . .
# binlog_do_db          = include_database_name
Remove the pound sign to uncomment this line and replace include_database_name with the name of the database you want to replicate. This example shows the binlog_do_db directive pointing to a database named db, but if you have an existing database on your source that you want to replicate, use its name in place of db:

/etc/mysql/mysql.conf.d/mysqld.cnf
. . .
binlog_do_db          = db
Note: If you want to replicate more than one database, you can add another binlog_do_db directive for every database you want to add. This tutorial will continue on with replicating only a single database, but if you wanted to replicate more it might look like this:

/etc/mysql/mysql.conf.d/mysqld.cnf
. . .
binlog_do_db          = db
binlog_do_db          = db_1
binlog_do_db          = db_2
Alternatively, you can specify which databases MySQL should not replicate by adding a binlog_ignore_db directive for each one:

/etc/mysql/mysql.conf.d/mysqld.cnf
. . .
binlog_ignore_db          = db_to_ignore
After making these changes, save and close the file. If you used nano to edit the file, do so by pressing CTRL + X, Y, and then ENTER.

Then restart the MySQL service by running the following command:

sudo systemctl restart mysql
With that, this MySQL instance is ready to function as the source database which your other MySQL server will replicate. Before you can configure your replica, though, there are still a few more steps you need to perform on the source to ensure that your replication topology will function correctly. The first of these is to create a dedicated MySQL user which will perform any actions related to the replication process.
**Step 5: Configuring the Replica Database**

**Overview:**
- Configuring the replica database involves adjusting its MySQL configuration file to match the source's settings and restarting the MySQL service to apply the changes.
- Key adjustments include setting a unique server-id, aligning log_bin and binlog_do_db values, and adding a relay-log directive.

**Analogies:**
- Configuring the replica database is like setting up a mirror in a room to reflect exactly what's happening in another room, ensuring both rooms have identical setups and reflect the same actions.

**Procedure:**
1. **Open MySQL Configuration File:**
   - Access the replica server's MySQL configuration file:
     ```
     sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
     ```

2. **Adjust Server-id:**
   - Find the server-id directive, uncomment it, and assign a unique positive integer value (e.g., 2):
     ```
     server-id = 2
     ```

3. **Update log_bin and binlog_do_db:**
   - Ensure log_bin and binlog_do_db values match the source's configuration:
     ```
     log_bin = /var/log/mysql/mysql-bin.log
     binlog_do_db = db
     ```

4. **Add relay-log Directive:**
   - Include a relay-log directive at the end of the file to define the location of the replica's relay log file:
     ```
     relay-log = /var/log/mysql/mysql-relay-bin.log
     ```

5. **Save and Restart MySQL:**
   - Save the changes and exit the text editor.
   - Restart the MySQL service to apply the new configuration:
     ```
     sudo systemctl restart mysql
     ```

**Conclusion:**
- The replica database is now configured to replicate data from the source database, ensuring synchronization between the two instances.

**Next Steps:**
- Verify replication status and monitor for any issues.
- Test data replication by making changes on the source and ensuring they reflect on the replica.

You're now ready to start replicating data from your source database. Let me know if you need further assistance!
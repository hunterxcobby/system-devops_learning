Understanding Fabric Exit Status:

**Success Condition**:
- When `fab` successfully executes all commands on all hosts, it returns a success exit status of 0.

**Failure Conditions**:
1. **Invalid Command or Option**:
   - If an invalid command or option is specified, `fab` aborts with an exit status of 1.

2. **Connection Failure**:
   - If a connection to a host fails, `fab` aborts with an exit status of 1. It does not attempt to connect to the next host.

3. **Command Execution Failure**:
   - If a local or remote command fails and returns a non-zero status, `fab` aborts with an exit status of 1. 
   - The exit status of the original command can be found in the log.

4. **Python Exception**:
   - If a Python exception is thrown during execution, `fab` aborts with an exit status of 1.

Understanding Fabric's exit status helps in determining the success or failure of the execution, allowing for effective error handling and troubleshooting.
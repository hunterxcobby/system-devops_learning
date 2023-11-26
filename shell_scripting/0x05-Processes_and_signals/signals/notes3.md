
### Maskable Signals:

1. **SIGINT (Ctrl+C):**
   - **Scenario:** When a user wants to interrupt a running process in the terminal.
   - **Use Case:** Typically used to gracefully terminate a process or allow it to perform cleanup operations before exiting.

2. **SIGTERM:**
   - **Scenario:** Software shutdown or termination initiated by a user or a script.
   - **Use Case:** Allows a process to catch the signal and perform any necessary cleanup before exiting. It gives the process a chance to terminate gracefully.

3. **SIGHUP:**
   - **Scenario:** Restarting a daemon or background process after configuration changes.
   - **Use Case:** The process can catch SIGHUP to reload its configuration or restart itself without a complete shutdown.

### Non-Maskable Signals:

1. **SIGKILL:**
   - **Scenario:** Forcefully terminating a misbehaving process.
   - **Use Case:** Used when immediate termination is necessary, and the process cannot be allowed to perform any cleanup or ignore the signal.

2. **SIGSEGV (Segmentation Fault):**
   - **Scenario:** Accessing invalid memory addresses, leading to memory corruption.
   - **Use Case:** Indicates a critical error in the program's memory management. Handling this signal is not possible; it usually results in a program crash.

3. **SIGILL (Illegal Instruction):**
   - **Scenario:** Attempting to execute an illegal or undefined CPU instruction.
   - **Use Case:** Indicates a severe issue in the program's code. Handling this signal is not practical; it typically results in immediate termination.

Understanding the nature of each signal helps determine the appropriate response in different situations. Maskable signals provide flexibility for graceful termination, while non-maskable signals are reserved for situations requiring immediate and forceful actions due to critical errors.
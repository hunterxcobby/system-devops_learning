
1. **Maskable Signals:**
   - **Definition:** Maskable signals are signals that the user or the running process can choose to handle, ignore, or modify.
   - **Example:** When you press Ctrl+C in the terminal to interrupt a running process, you're sending a maskable signal (SIGINT) that can be caught and handled by the process. The process can decide how to respond to this signal, whether to gracefully terminate or ignore it.
   - **Purpose:** These signals are designed to allow flexibility for the user or the program to control the behavior of processes in response to certain events.

2. **Non-Maskable Signals:**
   - **Definition:** Non-maskable signals are signals that cannot be ignored or modified by the user or the running process. They usually indicate critical and non-recoverable issues, often related to hardware errors.
   - **Example:** Non-maskable signals (e.g., SIGKILL) are sent in situations where immediate termination is necessary, and the process has no chance to intercept or handle the signal. These signals are reserved for extreme conditions.
   - **Purpose:** Non-maskable signals are essential for handling severe situations where a process needs to be forcefully terminated, and any attempt to modify or ignore the signal would be futile.

Understanding the distinction between maskable and non-maskable signals is crucial for effectively managing processes and ensuring appropriate responses to different types of events in a Linux environment.
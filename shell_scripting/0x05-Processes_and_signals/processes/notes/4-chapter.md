### Understanding Process Environment in C Programming

#### Environment List and Accessing Process Environment:

- The Linux command `env` displays a list of name=value pairs, representing the shell environment.

- Similarly, a process has its environment, and we can access it through two methods:
  1. Using the global variable `extern char **environ`
  2. Through the third argument to the `main()` function `char *envp[]`

- The historical third argument to `main()` (`envp[]`) allowed direct access to the process environment, although modern ISO C specifies `main()` with only two arguments.

#### Code Snippet Explanation:

- The following C code snippet demonstrates how to access the environment from within a process:

```c
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

extern char **environ;

int main(int argc, char *argv[])
{
  int count = 0;

  printf("\n");
  while(environ[count] != NULL)
  {
    printf("[%s] :: ", environ[count]);
    count++;
  }

  char *val = getenv("USER");
  printf("\n\nCurrent value of environment variable USER is [%s]\n",val);

  if(setenv("USER","Arora",1))
  {
    printf("\n setenv() failed\n");
    return 1;
  }

  printf("\n Successfully Added a new value to existing environment variable USER\n");

  val = getenv("USER");
  printf("\nNew value of environment variable USER is [%s]\n",val);

  while(1)
  {
    sleep(2);
  }
  return 0;
}
```

#### Code Output Explanation:

- The program prints the entire environment list to stdout.

- It uses `getenv` to get the value of the `USER` environment variable and `setenv` to change its value.

- The output shows the original and modified values of the `USER` environment variable.

#### Example Output:

```bash
$ ./environ

[ORBIT_SOCKETDIR=/tmp/orbit-himanshu] :: [SSH_AGENT_PID=1627] :: [TERM=xterm] ::
[SHELL=/bin/bash] :: [WINDOWID=39846040] :: [GTK_MODULES=canberra-gtk-module] ::
[USER=himanshu] :: [SSH_AUTH_SOCK=/tmp/keyring-6kpqGc/ssh] ::
..
..

Current value of environment variable USER is [himanshu]

Successfully Added a new value to existing environment variable USER

New value of environment variable USER is [Arora]
```

#### Conclusion:

- Understanding how to access and manipulate the process environment in a C program provides flexibility in handling environment variables during program execution.
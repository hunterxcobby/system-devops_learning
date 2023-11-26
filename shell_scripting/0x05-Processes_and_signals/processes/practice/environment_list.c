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
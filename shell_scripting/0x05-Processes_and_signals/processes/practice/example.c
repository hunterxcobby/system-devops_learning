#include<stdio.h>

int main(int argc, char *argv[])
{
  int count = argc;
  printf("\n The number of arguments passed is [%d] \n", count);

  int c = 0;
  while(c < count)
  {
    printf("\n The argument [%d] is : [%s]\n", c+1, argv[c]);
    c++;
  }
  return 0;
}
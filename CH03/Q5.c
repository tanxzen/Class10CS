/*

Q5. Write a C program to find the ASCII character of a given integer.

*/

#include <conio.h> //remove if not using turboc++
#include <stdio.h>

int main() {

  int n;

  clrscr(); // remove if not using turboc++;

  printf("Enter number : ");
  scanf("%d", &n);

  printf("Character : %c\n",n);
             // we are converting the interger to charcter with the format
             // specifier %c which represent character ;
 
  getch();   // remove if not using turboc++;
  return 0;
}

/*

Q4. Write a C program to find the value of y using the relation y = x^2 + 2x
- 1.

*/

#include <conio.h> //remove if not using turboc++;
#include <stdio.h>

int main() {

  float x, y;

  clrscr(); // remove if not using tubroc++;

  printf("Enter the value of x : ");
  scanf("%f", &x);

  y = x * x + 2 * x - 1;

  printf("The value of y : %6.2f\n", y);
  getch(); // remove if not using turboc++;
  return 0;
}

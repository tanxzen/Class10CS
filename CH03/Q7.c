/*

Q7. Write a C program to swap (exchange) the values of a variables A and B
without using temporary variable. [Hint : A = A + B ; B = A - B ; A = A - B]

*/

#include <conio.h> // remove if not using turboc++
#include <stdio.h>

int main() {

  int A, B;

  clrscr(); // remove if not using turboc++

  printf("Enter Value of A : ");
  scanf("%d", &A);

  printf("Enter Value of B : ");
  scanf("%d", &B);

  A = A + B;
  B = A - B;
  A = A - B;

  printf("Value of A : %d\n", A);
  printf("Value of B : %d\n", B);

  getch(); // remove if not using turboc++
  return 0;
}

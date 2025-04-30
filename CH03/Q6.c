/*

Q6. Write a C program to calculate simple interest using formula I = PNR/100.

*/

#include <conio.h> // remove if not using turboc++
#include <stdio.h>

int main() {

  float P, N, R, I;

  clrscr(); // remove if not using turboc++

  printf("Enter Pricipal : $ ");
  scanf("%f", &P);

  printf("Enter Time : ");
  scanf("%f", &N);

  printf("Enter Rate : ");
  scanf("%f", &R);

  I = (P * N * R) / 100.0;

  printf("Interest : $ %6.2f\n", I);
  getch(); // remove if not using turboc++
  return 0;
}

/*

Q9. Write a C program to calculate the cut-off mark of a student using the
formula CM = M/2 + P/2 - C/2 + E where CM = Cut-off Mark , M = Marks in
mathematics out of 200 , P = Mark in Physics out of 200 , C = Marks in Chemestry
out of 200 , E = Marks in entrance examination out of 100.

*/

#include <conio.h> //remove if not using turboc++
#include <stdio.h>

int main() {

  float M, P, C, E, CM;

  clrscr(); // remove if not using turboc++

  printf("Enter mark in mathematics (out of 200): ");
  scanf("%f", &M);

  printf("Enter mark in Physics (out of 200) : ");
  scanf("%f", &P);

  printf("Enter mark in Chemestry (out of 200) : ");
  scanf("%f", &C);

  printf("Enter mark in Entrance Exam (out of 100) : ");
  scanf("%f", &E);

  CM = (M / 2.0) + (P / 2.0) - (C / 2.0) + E;

  printf("Cut-Off Mark : %.2f\n", CM);

  getch(); // remove if not using turboc++
  return 0;
}

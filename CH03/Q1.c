/*

Q1. Write a C program to find the sum and average of given three numbers .

*/

#include <conio.h> // for turboc++ compilers , remove if you are not using turboc++
#include <stdio.h>


int main() {

  int num1, num2, num3, sum = 0;
  float average = 0;

  clrscr(); // remove if you are not using turboc++

  printf("Enter 3 numbers : ");
  scanf("%d %d %d", &num1, &num2, &num3);

  sum = num1 + num2 + num3;
  average = (num1 + num2 + num3) / 3.0;

  printf("Sum : %d \nAverage : %6.2f\n", sum, average);
  getch() // remove if you are not using turboc++

      return 0;
}

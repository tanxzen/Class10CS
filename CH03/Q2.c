/*

Q. Write a C program to convert temperature in °C to °F using the relation °F
= 1.8°C + 32 .

*/

#include <stdio.h>
// #include <conio.h>

int main() {
  float cel, far;

  clrscr(); // remove if not using turboc++

  printf("Enter Celsius : ");
  scanf("%f", &cel);

  far = 1.8 * cel + 32;

  printf("Farenheit : %6.2f°F\n", far);
  getch(); // remove if not using turboc++

  return 0;
}

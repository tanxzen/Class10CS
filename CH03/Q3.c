/*

Q3. Write a C program to find the area and circumference of a circle of radius
r.

*/

#include <conio.h> // for turboc++ , if not using remove ;
#include <stdio.h>

int main() {

  float r, area, circumference;

  clrscr() // remove if not using turboc++ compiler;

      printf("Enter radius of circle : ");
  scanf("%f", &r);

  area = 22.0 / 7.0 * r * r;
  circumference = 2 * 22.0 / 7.0 * r;

  printf("Area : %6.2f\n", area);
  printf("circumference : %6.2f\n", circumference);

  getch() // remove if not using turboc++ compiler ;
      return 0;
}

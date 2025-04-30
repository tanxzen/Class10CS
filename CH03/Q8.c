/*

Q8. Earth takes a period of revolution of 31558150 seconds. Write a C program
    to convert this into number of days, hours and minutes.

*/

#include <conio.h> //remove if not using turboc++
#include <stdio.h>

int main() {

  int sec = 31558150;
  float days, hours, minutes;

  clrscr(); // remove if not using turboc++

  days = sec / 86400.0; // 1 day = 86400 seconds
  hours = sec / 3600.0; // 1 hour = 3600 seconds
  minutes = sec / 60.0; // 1 minutes = 60 seconds

  printf("Numbers of days = %.2f days\n", days);
  printf("Hours : %.2f hours\n", hours);
  printf("Minutes : %.2f minutes\n", minutes);

  getch(); // remove if not using turboc++
  return 0;
}

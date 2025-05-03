## Textual Question 

  ---

   `Q1. Write a C program to find the sum and average of three given numbers .` <br>
   Ans :
   ```c
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
   ```
   
  `Q2. Write a C program to convert temperature in °C to °F using the relation °F = 1.8°C + 32.`<br>
  Ans : 
```c
#include <conio.h>

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
```
  
   `Q3. Write a C program to find the area and circumference of a circle of radius r.`<br>
   Ans : 
   ```c
#include <conio.h>

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
   ```
   `Q4. Write a C program to find the value of y using the relation y = x^2 + 2x - 1.` <br>
 Ans :
   ```c

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
   ```
   `Q5. Write a C program to find the ASCII character of a given integer.`<br>
 Ans : 
 ```c
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

```
   `Q6. Write a C program to calculate simple interest using formula I = PNR/100.`<br>
 Ans : 
```c

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
```
 
   `Q7. Write a C program to swap (exchange) the values of a variables A and B without using temporary variable. [Hint : A = A + B ; B = A - B ; A = A - B]`<br>
Ans : 
```c
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
```

   `Q8. Earth takes a period of revolution of 31558150 seconds. Write a C program to convert this into number of days, hours and minutes.`<br>
 Ans :
```c

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
```
 
   `Q9. Write a C program to calculate the cut-off mark of a student using the formula CM = M/2 + P/2 - C/2 + E where CM = Cut-off Mark , M = Marks in mathematics out of 200 , P = Mark in Physics out of 200 ,C = Marks in Chemestry out of 200 , E = Marks in entrance examination out of 100.`<br>

   Ans : 
```c

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
```

   ---
  

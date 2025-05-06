# SECTION A: REVIEW QUESTIONS AND EXERCISES

  ---

Q1. Write a C program to find the sum and average of three given numbers . <br>
Ans:
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
   
Q2. Write a C program to convert temperature in °C to °F using the relation °F = 1.8°C + 32.<br>
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
  
Q3. Write a C program to find the area and circumference of a circle of radius r.<br>
Ans : 
```c
#include <conio.h> //remove if not using turboc++
#include <stdio.h>
int main(){
    
    float r, area, circumference;
    
    clrscr(); //remove if not using turboc++
    
    printf("Enter Radius of the Circle : ");
    scanf("%f",&r);
    
    area = 22.0/7.0 * r * r; 
    circumference = 2 * 22.0/7.0 * r;
    
    printf("Area of circle : %.2f\n",area);
    printf("Circumference of Circle : %.2f\n",circumference);
    getch(); //remove if not using turboc++
    return 0;
}
```
Q4. Write a C program to find the value of y using the relation $y = x^2 + 2x - 1$. <br>
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
Q5. Write a C program to find the ASCII character of a given integer.<br>
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
Q6. Explain `scanf()` and `printf()` functions in C. <br>

Ans : Printf function is used to print/display values of variables using the standard output device(monitor).It can also be use to print any character of our choice in the monitor. Whereas, 
Scanf function is used to read/input values of variables using the standard input device (keyboard).It is used in a program to take input from the user or where there is necessary for user interaction. 

Q7. Explain the various character input/output functions in C. <br>

Ans : 
```
      getchat() function : It is used to read one character at a time from the standard input device(keyboard).<br>
      putchar() function : It is ued to display one character at a time on the monitor screen.
      getch() function : It is used to read a character from the keyboard and it does not expect the enter key press.
      putch() function : It is used to display a character on the monitor.
      gets() function : It is used to read a string of characters including white space.
```      

Q8. Mention the various conversion specifications for data I/O in C. <br>

Ans :
```
int :     : %d : represents a decimal integer value <br>
          : %u : represents an unsigned integer value.
          : %o : represents an unsigned octal value.
          : %x : represents an unsigned hexadecimal value.

float/double :
          : %f : represents a floating point value.
          : %e : represents a floating point value in a decimal or exponential form.

char :    : %c : represents a single character value.
          : %s : represents a string of value of characters.    
```
Q9. Write a C program to calculate simple interest using formula $I = \frac{PNR}{100}$.<br>
where P - Principal amount, N - Number of years, R - Rate of interest <br>
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
 
Q10. Write a C program to swap (exchange) the values of a variables A and B without using a temporary variable. <br>
[**Hint**: The following assignments are used to swap the values: <br>
A = A + B <br>
B = A - B <br>
A = A - B]<br>
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

Q11. Earth takes a period of revolution of 31558150 seconds. Write a C program to convert this into number of days, hours and minutes.<br>
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
 
Q12. Write a C program to calculate the cut-off mark of a student using the formula $CM = \frac{M}{2} + \frac{P}{2} = \frac{C}{2} + E$ <br>
where CM = Cut-off mark <br>
      M = Marks in mathematics out of 200 <br>
      P = Mark in Physics out of 200 <br>
      C = Marks in Chemistry out of 200 <br>
      E = Marks in entrance examination out of 100.<br>
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

# SECTION B: SHORT QUESTIONS

---

1. What is the purpose of `scanf()` function? How it is used within a C program?<br>

Ans : `scanf()` function is used to take user input in a program. It can be used along with the format specifier and address of the variable.

2. What is the use of "`\n`"?<br>

Ans : `\n` is used to move to new line in the program.

3. Assuming i=3, give the output for <br>
`printf("\n %d %d %d\n", i, ++i, i++);`<br>

Ans : 3 4 4

4. Explain the significance of the following control specifiers:

(a) **%c**
(b) **%0**
(c) **%x**
(d) **%d**

5. What is a header file in C? List any two header files.

6. The line from which a program execution begins is________.

7. The sign `#` of the compiler directive must appear at the __________ of a line.

8. Write four different C statements each adding 1 to integer variable x.

9. How do you generate an alarm/beep using `printf`?

10. What is the difference between `getchar()` and `getche()`?

11. What is an escape sequence? What is its purpose?

12. Explain the need for the following: <br>
`#include <stdio.h>` <br>
`#include <math.h>` <br>

13. Explain with examples the syntax of `scanf()` and `printf()` functions.

14. What is the difference between C character and C string?

15. Name any four functions available in `stdio.h`.

16. The file name `stdio.h` is an abbreviation for ________ file.

17. What is the difference between `'a'` and `"a"` in C?

18. How can the minimum field width for a data item be specified using the `printf()` function?

19. What are the advantages of `getche()` over `scanf()`?

20. Obtain the output of the following statements in C. The variables `count`, `amt` and `city` have the following values.<br>
```
int count =1275; 
float amt =-235.74;
char city [10] = "Chennai";
```
`(a) printf("%d\f", count, amt);`<br>
`(b) printf("%-10d%-15s", count, city);`<br>

Ans : 

21. How can precision be specified in `printf` function?

22. A C program contains the following variable declaration:
`int i = 12345, j = 0xbcd9, k077777;`
What will be the output of the `printf()` function?

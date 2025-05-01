# SECTION A: REVIEW QUESTIONS AND EXERCISES
1. Explain the various **if** structures available in C.

Ans : 
```
The various if structures are :
i. Simple if statement  : the if statement is used for the selection of one statement based on condition.
   The if statement will start with the evaluation of the given expression.
   The syntax of if statement is :
        if (condition)
          {
            Statement
          }

ii. If-else statement : if-else statement is used if the condition is true, the statement associated with the if part will be executed. If the condtion
    is false, the statement associated with the else part will be executed.
    The syntax of if-else is :
    if (condition)
    {
        True block
    }
    else 
    {
        False Block
    }

iii. Nested if-else statement : An if statement may have another if statement in a true block and false block. These compound statement are called nested if statement.
     The syntax of nested if-else statemnt is :
      if (condition 1)
{
  if (condition 2)
    {
        --------------
        <true block 1>
        --------------
    }
   else
    {
        -------------
        <false block 1>
        -------------
    }
}
else
{
  if (condition 3)
    {
      --------------
      <true block 2>
      --------------
    }
  else
    {
      ---------------
      <false block 2>
      ---------------
    }
}
  
```


2. Write notes on (i) conditional statement (ii) **switch** statement

Ans : 
```
i. Conditional Statement : Conditional Statement are used to execute/transfer the control from one part of the program to another depending on a condition.
   There are two types of conditional statement used in C language : 
      a. if-else statement. 
      b. switch statement.
ii. Switch Statement : The switch statement are substitude for a long if-else statement. Switch statment is used to
    execute a block of statement depending on the value of a variable or expression.
```

3. Discuss the difference between **if...else** and **switch** structures.<br>

Ans : 
| If-else | Switch |
| ------- | ------ |
| i. if else statement uses condition to execute a block of statement. | i. Switch statement uses a single expression or value of a variable to execute a block of statement | 
| ii. It's keywords are if, else and else if | ii. It's keywords are switch, case and default |
| iii. It can contain multiple condition using logical operators | Each case can contain only one value | 


4. Explain with example the if statement and nested if statement in C.<br>

Ans : 
```
i. If statement : if statement is used to execute a statement block or a single statement depending on the value of a condition
   Example :
         int mark = 50;
         if (mark < 40){
            printf("Failed\n");
         }
         else {
            printf("Passed")
         }
   In the following code the else part will be executed because mark is more than 40.

ii. Nested if-else statement : An if statement may have another if statement in the <true block> and <false block>.This compound statement is called nested if statement.
    Example :
      int mark = 95;
      if (mark > 40 ) {
         if (mark > 90)
               printf("Grade : A");
            else {
                  printf("Grade : B");
               }
      }
      else {
         printf("Grade : F");
      }
      In the following code the grade will be printed as A because the grade is greater than 40 and 90.
```

5. Write a C program to find the smallest of given two numbers.<br>

Ans :
```c
#include <conio.h> //remove if not using turboc++ compiler
#include <stdio.h>

int main(){
   int a, b, big;

   clrscr() //remove if not using turboc++

   printf("Enter two numbers : ");
   scanf("%d %d",&a,&b);

   if (a>b){
   big = a;
   }
   else {
   big = b;
   }
   printf("Biggest number : %d\n",big);
   getch() // remove if not using turboc++
   return 0;
}
```

7. Write a C program to find the smallest of given three numbers. <br>
Ans :
```c
#include <conio.h> //remove if not using turboc++
#include <stdio.h>

int main(){
  int a, b, c, big;

   clrscr() //remove if not using turboc++

   printf("Enter three numbers : ");
   scanf("%d %d %d",&a,&b,&c);

   if (a>b){
      if (a>c){
            big = a;
         }
      else{
         big = c;
         }
   }
   else {
      if (b>c){
            big = b;
            }
      else {
            big = c;
         }
   }
   printf("Biggest number : %d\n",big);
   getch() // remove if not using turboc++
   return 0;
}
```


9. Write a C program to find the average of best three marks from the given four test marks.

[Hint: Find the smallest of given four test marks. Subtract it from the sum of four test marks. You will now get the sum of best three marks. Take the average

i.e., average = $(T1 + T2 + T3 + T4 - smallest)/ 3$ <br>

Ans : 
```c
#include <conio.h> //remove if not using turboc++ compiler
#include <stdio.h>

int main(){

   int t1, t2, t3, t4, smallNum; 
   float avr;

   clrscr() ; //remove if not using turboc++

   printf("Enter the four marks : ");
   scanf("%d %d %d %d",&t1, &t2, &t3, &t4);

   smallNum = t1 ; // setting the small number is t1

   if (t2 < smallNum){
      smallNum = t2; // if t2 was less than smallNum then the value of smallNum is set to the value of t2
   }
   if (t3 < smallNum){
      smallNum = t3; // if t3 was less than smallNum then the value of smallNum is set to the value of t3
   }
   if (t4 < smallNum){
      smallNum = t4; // if t4 was less than smallNum then the value of smallNum is set to the value of t4
   }

   avr = (t1 + t2 + t3 + t4 - smallNum) / 3.0 ;

   printf("Average of best three marks : %.2f\n",avr);
   getch(); //remove if not using turboc++
   return 0;

}
```

8. Write a C program that will read the value of x and evaluate the function <br>
y(x) = x² + 2x - 10 if x < 10 <br>
= |x|               if x < 0
using a **if** statement.<br>

Ans : 
```c

#include <conio.h> //remove if not using turboc++
#include <stdio.h>
#include <math.h> // for absolute value of x or for fabs() func 

int main() {

   float x, y;

   clrscr() //remove if not using turboc++

   printf("Enter value of x : ");
   scanf("%f",&x);

   if (x>10){
      y = x*x + 2*x - 10; // set the value of y to the value of this expression if x is less than 10;  
   }
   if (x<0){
      y = fabs(x); // set the absolute value of x to y if x is less than 0 meaning negative numbers;
   }

   printf("Value of y : %.2f\n",y);
   getch(); //remove if not using turboc++
   return 0;
}

```





9. A company pays salary to an employee at the normal hourly rate, if the number of hours worked does not exceed 40. If the number of hours worked exceeds 40, the salary for the excess number of hours is calculated as 1.5 times the normal hourly rate. Write a C program to implement this to calculate the salary.

10. Write a C program to read the marks scored by a student in an examination and print the percentage of marks along with the grade obtained using the following conditions.

(1) percentage >=75 and percentage <=100, "DISTINCTION"

(ii) percentage >= 60 and percentage <75, "FIRST CLASS"

(iii) percentage >=50 and percentage <60, "SECOND CLASS"

(iv) If the marks obtained by the student in any subject is <50, "FAIL".<br>

Ans :
```c
#include <conio.h> //remove if not using turboc++
#include <stdio.h>

int main(){
   
   int mark ;
   float fullmark, per;

   clrscr(); //remove if not using turboc++
   
   printf("Enter mark : ");
   scanf("%d",&mark);

   printf("Enter full mark : ");
   scanf("%f",&fullmark);

   per = mark/fullmark * 100 ;

   if (per >= 50 ){ // if per is geater than 50 then the next if statements is executed
       if (per >= 60){ //if per is greater than 75 then the next if statement is executed
           if (per >= 75 && per <= 100){ //if per is greater than 75 and less than 100 it prints distinction
               printf("DISTINCTION\n");
           }
           else { 
               printf("FIRST CLASS\n"); // if per is less than 75 its prints first class
           }
       }
       else{ 
         printf("SECOND CLASS\n"); // if per is less then 60 prints second class
       }
   }
    else {
        printf("FAIL\n"); // if per is less than 50 it prints fail
    }

   getch(); //remove if not using turboc++
   return 0;
}
```

11. A company gives festival discount on purchase of their products in the following percentages:

(i) if purchase amount < 1000 then 5% discount

(ii) if purchase amount >= 1000 but <3000 then 10% discount

(ii) if purchase amount >= 3000 but <5000 then 12% discount

(iv) if purchase amount > 5000 then 15% discount.

Write a C program using nested if statement to compute the amount to be paid by the customer after discount.

12. Write a C program to calculate the commission of a salesman considering three regions X, Y and Z depending on the sales amount as follows.

(i) **For area code X**

|Sales amount | Commission |
|:------------|:-----------| 
|<1000        |10%         |
|<5000        |12%         |
|>=5000       |15%         |   

(ii) **For area code Y**

|<1500  | 10%|
|:------|:---|
|<7000  | 12%|
|>= 7000| 15%|

(iii) **For area code Z**

|<1200  | 10%|
|:------|:---|
|<6500  | 12%|
|>=6500 | 15%|

13. The commission on a salesman's total SALES is as follows:

SALES < Rs.100            -no commission
Rs.100 <= SALES < Rs.1000 -commission 10% of SALES.
SALES >= Rs.1,000         -commission Rs. 100+8% of SALES above Rs. 1000

Write a program that reads SALES and prints the salesman's commission.

# SECTION B: SHORT QUESTIONS

1. Give the general syntax of **if-else** statement in C.

2. Give the general syntax of **switch** statement in C.

3. A **break** statement is used to exit from a ___.

4. What is the purpose of a **switch** statement?

5. In what ways does a switch statement differ from an **if** statement?

6. Using what other statement can you avoid multiple nested **if** conditions?

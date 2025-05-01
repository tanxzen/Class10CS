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

3. Discuss the difference between **if...else** and **switch** structures.

4. Explain with example the if statement and nested if statement in C.

5. Write a C program to find the smallest of given two numbers.

6. Write a C program to find the smallest of given three numbers.

7. Write a C program to find the average of best three marks from the given four test marks.

[Hint: Find the smallest of given four test marks. Subtract it from the sum of four test marks. You will now get the sum of best three marks. Take the average

i.e., average = (T1 + T2 + T3 + T3 - smallest)/ 3

8. Write a C program that will read the value of x and evaluate the function
y(x) = x² + 2x - 10 if x < 10
= |x|               if x < 0
using a **if** statement.

9. A company pays salary to an employee at the normal hourly rate, if the number of hours worked does not exceed 40. If the number of hours worked exceeds 40, the salary for the excess number of hours is calculated as 1.5 times the normal hourly rate. Write a C program to implement this to calculate the salary.

10. Write a C program to read the marks scored by a student in an examination and print the percentage of marks along with the grade obtained using the following conditions.

(1) percentage >=75 and percentage <=100, "DISTINCTION"

(ii) percentage >= 60 and percentage <75, "FIRST CLASS"

(iii) percentage >=50 and percentage <60, "SECOND CLASS"

(iv) If the marks obtained by the student in any subject is <50, "FAIL".

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

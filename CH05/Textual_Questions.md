# SECTION A: REVIEW QUESTIONS AND EXERCISES 
1. Explain with an example a `for` loop used in C.
2. Write a C program to find the sum of natural numbers from 1 to `n`.<br>

Ans : 

```c
#include <conio.h> //remove if not using turboc++
#include <stdio.h>

int main(){
    int n, i, sum = 0;
  
    clrscr(); //remove if not using turboc++
     
    printf("Enter Number : ");
    scanf("%d",&n);
    
    for (i = 0;i<=n;i++){
        sum = sum + i;
    }
    printf("Sum of natural number upto %d : %d\n",n,sum);
    getch();
    return 0;
}
```

3. Write a C program to find the sum of all even integers between 2 and `n`.<br>

Ans : 
```c
#include <conio.h> //remove if not using turboc++
#include <stdio.h>

int main(){
    int n, i, sum=0;

    clrscr(); //remove if not using turboc++

    printf("Enter number : ");
    scanf("%d",&n);
    
    for (i = 3; i<=n; i++){
        if (i % 2 == 0){
            sum = sum + i;
        }
    }
    printf("The sum of all even integer between 2 and %d : %d\n",n,sum);
    getch(); //remove if not using turboc++
    return 0;
}
```

4. Write a C program to print integers from 1 to 50, five integers per line. Explain the working of the program.<br>

Ans : 
```c
#include <conio.h> //remove if not using turboc++
#include <stdio.h>

int main(){
    
    int i ;

    clrscr(); //remove if not using turboc++

    for(i = 1; i<=50;i++){
        printf("%d ",i);
        
        if (i % 5 == 0){
            printf("\n");
        }
    }
    getch(); //remove if not using turboc++
    return 0;
}
```

<p>
  
  In the following code, we first delcare `i = 1` setting the variable i as 1 then we apply `clrscr()` to clear any previous text from screen then we apply for loop with the condition `i<=50` , saying `i` is less than or equal to 50, which will run the loop for 50 times while running, inside the loop we print the value of `i` and we use a condition `i % 5 == 0` meaning if the value of i reach any number divisible by 5 then it should print new line, which solves the problem of displaying 5 values per line.   
</p>


5. The frequency `n` of a vibrating string which depends on length. 1, tension T. and linear density is given by <br>
$n = \frac{k}{l} \sqrt{\frac{T}{m}}$
where is a constant. Write a C program to find `n` when 1=50, 60, 70 and 80 cm. <br>

6. Write a C program to generate and print the numbers between 100 and 200 which are divisible by 3. but not divisible by 4.<br>

Ans : 
```c
#include <conio.h>
#include <stdio.h>

int main(){
    int i;

    clrscr(); //remove if not using turboc++

    printf("The number which are divisible by 3 but not by 4 between 100 and 200 are : \n");
    for (i = 100;i<=200;i++){
        if (i % 3 == 0 && i % 4 != 0){
            printf("%d\n",i);
        }
    }
    getch(); //remove if not using turboc++
    return 0;
}
```

7. Write a C program to print the individual digits of a 6-digit number. <br>

Ans:
```c
#include <conio.h> //remove if not using turboc++
#include <stdio.h>

int main(){
    int n, j;

    clrscr(); //remove if not using turboc++

    printf("Enter 6 digit number : ");
    scanf("%d",&n);
 
    printf("Individual Digits are : ");
   for (int i = 100000; i>0;i=i/10){
       j = n/i;
       n = n%i;
       printf("%d\n",j);
    }
    getch(); //remove if not using turboc++ 
    return 0;
}

```

8. Write a C program to find the sum of the individual digits of a N digit number and check whether it is odd or even. <br>

Ans : 
```c



```

9. Write a C program to print Armstrong numbers from 100 to 999.
10. Write a C program to test whether a given number is a palindrome nuniber. Explain the working of the program. 
(An integer is said to be a palindrome if it doesn must change when the order of digits in the integer is reversed. For example 321454123, 536635 are palindromes) 
11. Write a C program to accept an integer number between 1 and 9. Write the value of the mumber in words. 
12. Write a C program to print the prime numbers between 100 and 1000. 
13. Write a C program to check if the given number is a perfect number. 
(A number is said to be a perfect number if the sum of its factors is equal to the given number. For example, 6 is a perfect number (factors of 6 are 12 and 3: adding the factors we get 1+2+3=6). 
14. Write a C program which will print the factorial of all numbers from 1 to 15.
15. The numbers in the sequence 1 1 2 3 5 8 are called fibonacci numbers. Write a program in C using a `do-while` loop to calculate and print the first 50 Fibonacci numbers.
16. Write a C program to evaluate the series <br>
$1 + \frac{1}{3} + \frac{1}{5} + \ldots$
up to 15 terms.
17. Write a C program to generate and print the pyramid of numbers as follows. <br>
<pre>
                         1 
                     2       2                                                              
                 3       3       3                        
             4       4       4       4                                      
         5       5       5       5       5                    
</pre>
18. Write a C program to generate the following:
<pre>
        1 2 3 4 5 6 7
          1 2 3 4 5
            1 2 3
              1
</pre>
Explain the working of the program. <br>

19. Write a C program to print multiplication tables for 6 upto 20 numbers. 
20. Write a C program to convert an octal number into a decimal number. 
21. Write a C program to convert a decimal number into its equivalent octal number. 
22. Explain `for` loop and nested `for` loop with suitable examples.
23. Summarize the syntactic rules associated with the `for` statement in C language. Can any of the three expressions in the `for` statement be omitted? If so, what are the consequences of each omission. 
24. Explain the loop control structures used in C language.
25. Differentiate `while` loop and `do-while` loop.
# SECTION B: SHORT QUESTIONS 
1. Give differences between `while` and `do-while` statement.
2. Write a C program to find the sum of numbers between 1 and n.
3. Write a C program to find the square root of a given number. 
4. The loop in a `do-while` structure is executed ________ once. 
5. The _______ statement causes the loop to be terminated. 
6. The continue statement is used to transfer the control to the ______ of the loop.
7. Distinguish between the break and continue statements in C. 
8. What are the differences between break and exit() function.
9. What happens if the condition in a `while` loop is initially false? 
10. What is the use of break statement? 
11. What is the use of continue statement? 
12. exit(0) in a C program represents ________
13. List a few unconditional control statements in C.
14. Give an alternative for multiple if statements in C.
15. What is the output for the following program?

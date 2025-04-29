# CH03 : Input/Output Functions and statements

`stdio.h stands for standard input-output header , we will be learning to use the functions present in this header file.`

---

<details>
  <summary>
    Textual Question 
  </summary>

  ---

   `Q1. Write a C program to find the sum and average of three given numbers .` <br>
   
  `Q2. Write a C program to convert temperature in °C to °F using the relation °F = 1.8°C + 32.`<br>
  
   `Q3. Write a C program to find the area and circumference of a circle of radius r.`<br>
   
   `Q4. Write a C program to find the value of y using the relation y = x^2 + 2x - 1.` <br>
   
   `Q5. Write a C program to find the ASCII character of a given integer.`<br>
   
   `Q6. Write a C program to calculate simple interest using formula I = PNR/100.`<br>
   
   `Q7. Write a C program to swap (exchange) the values of a variables A and B without using temporary variable. [Hint : A = A + B ; B = A - B ; A = A - B]`<br>
   
   `Q8. Earth takes a period of revolution of 31558150 seconds. Write a C program to convert this into number of days, hours and minutes.`<br>
   
   `Q9. Write a C program to calculate the cut-off mark of a student using the formula CM = M/2 + P/2 +  // continue later


   ---

  
</details>


<details>

<summary>escape sequences</summary>

#

`Escape sequence are control characters used to move the cursor and print characters such as ?,",\ and so on.`

<br>

Some escape sequence are :

| Escape Sequence | Description                                                  | Function                                                    |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `\n`            | Newline (line feed)                                       | Moves the cursor to the beginning of the next line.         |
| `\t`            | Horizontal tab                                            | Moves the cursor to the next tab stop.                      |
| `\b`            | Backspace                                                 | Moves the cursor back one position.                         |
| `\r`            | Carriage return                                           | Moves the cursor to the beginning of the current line.      |
| `\f`            | Form feed (page break)                                    | Moves the cursor to the beginning of the next page.         |
| `\0`            | Null Character                                            | Represents the null character, which is the character with the ASCII value of 0. It is used to mark the end of a string and can be used for various other purposes, such as string manipulation and memory management.                                                        |
| `\v`            | Vertical tab                                              | Moves the cursor down to the next vertical tab stop.       |
| `\a`            | Alert (bell)                                              | Produces an audible alert (usually a beep).                |
| `\\`            | Backslash                                                 | Prints a backslash character.                               |
| `\?`            | Question mark                                             | Prints a question mark.                                     |
| `\'`            | Single quote                                              | Prints a single quote.                                      |
| `\"`            | Double quote                                              | Prints a double quote.                                      |
| `\ooo`          | Octal escape sequence (where `ooo` is an octal number)    | Prints the character represented by the octal number.      |
| `\xhh`          | Hexadecimal escape sequence (where `hh` is a hex number) | Prints the character represented by the hexadecimal number. |

  
</details>


<details>

<summary>
  format specifiers
</summary>

---

`Format specifier are used to specify the format of a variable or other while using input or output functions`
<br>

Some format specifier are :
<br>

| Format Specifier | Description                                                  | Function                                                    |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `%d` or `%i`     | Signed integer                                            | Prints or reads a signed integer value.                     |
| `%u`             | Unsigned integer                                          | Prints or reads an unsigned integer value.                  |
| `%f`             | Floating-point number                                     | Prints or reads a floating-point number.                    |
| `%e` or `%E`     | Floating-point number in scientific notation             | Prints or reads a floating-point number in scientific notation. |
| `%g` or `%G`     | Floating-point number in the more compact of `%f` or `%e` | Prints or reads a floating-point number in the more compact of `%f` or `%e`. |
| `%c`             | Single character                                          | Prints or reads a single character.                         |
| `%s`             | String                                                    | Prints or reads a string.                                   |
| `%p`             | Pointer                                                   | Prints the address of a pointer.                            |
| `%x` or `%X`     | Hexadecimal integer                                       | Prints or reads a hexadecimal integer value.               |
| `%o`             | Octal integer                                             | Prints or reads an octal integer value.                     |
| `%%`             | Literal percent sign                                      | Prints a literal percent sign. 

  
</details>

---

## printf() function

`printf() function is used to print/display values of variables using the standart input/output device(monitor).`
<br>


*syntax* : `printf("format string",V1,V2,Vn);`

where V1,V2 ... Vn are variables whose values are to be displayed in the monitor. "format string" is the control string which represents the format specification (refer to format specifiers).

### Example 
```c
printf(" %f ",s);
printf("\n sum = %6.2f ",s);
printf("\n %d factorial is %d",k,kfact);
```
When these functions are executed, the computer prints/display the values of the variables listed in printf().<br>
Consider value s = 2.8, k = 5 and kfact = 120.

```
2.800000
sum = 2.80
5 factorial is 120
```

---

## scanf() function

`scanf() function is used to read/input values of variables using the standard input device(keyboard).`
<br>

*syntax* : `scanf("format string",&V1,&V2 ... &Vn);`

Where V1, V2 ... Vn are variable whose values are to be read form the keyboard.<br>"format string" is the control string which represents the format specification (refer to format specifier ).<br>
The symbol `&`(ampersand) represents the memory address where the variable value is to be stored.


### Example
```c
scanf("%d %d", &a, &b); // to read value of int variables a and b.
scanf("%f %d", &x, &n); // to read float value of x and int value of n.
scanf("%c",&gender); // to read char value for the variable gender.
scanf("%s",sname); // to read a string of char variable sname.
```

When these functions are executed, the computer will wait for the values of the variable listed in scanf which are to be entered using keyboard.
<br>

```
12 13
4.03 10
m
tomba
```


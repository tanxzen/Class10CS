# CH03 : Input/Output Functions and statements

`stdio.h stands for standard input-output header , we will be learning to use the functions present in this header file.`

---

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

The `printf()` function is used in C programming to **print or display information on the screen** (monitor).

### What it Does:
It shows the values of variables or text messages on the screen.

### Syntax:

`printf("format string", variable1, variable2, ..., variableN);`

"format string": Tells the computer how to display the values (like %d for integer, %f for float, etc.).

variable1, variable2, etc.: These are the variables whose values you want to display.

Examples:
```c
float s = 2.8;
int k = 5, kfact = 120;

printf("%f", s);                          // Output: 2.800000
printf("\nsum = %6.2f", s);               // Output: sum =  2.80
printf("\n%d factorial is %d", k, kfact); // Output: 5 factorial is 120
```

## scanf() function

The `scanf()` function is used to **get input from the user through the keyboard**.

### What it Does:
It allows the user to **enter values**, which are stored into variables.

### Syntax:

`scanf("format string", &variable1, &variable2, ..., &variableN);`

"format string": Tells the computer what type of data to expect (%d for int, %f for float, etc.).

&variable: The & symbol means “address of” the variable. It tells the computer where to store the value entered by the user.

Examples:
```
int a, b;
float x;
char gender;
char sname[20];


scanf("%d %d", &a, &b);    // User enters two integers
scanf("%f", &x);           // User enters a float number
scanf("%c", &gender);      // User enters a character
scanf("%s", sname);        // User enters a string (one word)
```


## MORE FUNCTIONS : 

This guide covers common I/O functions in C from `stdio.h` and `conio.h`, with syntax and explanations.

---

### Standard I/O Functions (`<stdio.h>`)

| Function     | Syntax                    | Explanation |
|--------------|---------------------------|-------------|
| `getchar()`  | `char c = getchar();`     | Can take input of a character by reading **one character** from the keyboard when the user presses Enter. The character is stored in the variable (e.g., `c`). |
| `putchar()`  | `putchar(c);`             | Prints a **single character** to the screen. The character `c` must be provided. |
| `gets()`     | `gets(buffer);`           | Can take input of the user by reading a **whole line of text** (until Enter) from the keyboard and stores it in the variable `buffer`. |
| `puts()`     | `puts(string);`           | Prints the **string** to the screen and automatically moves the cursor to the next line. |

---

### Console I/O Functions (`<conio.h>` - Non-standard)

| Function     | Syntax                    | Explanation |
|--------------|---------------------------|-------------|
| `getch()`    | `char c = getch();`       | Reads a **single character** from the keyboard **without waiting for Enter**. The character is **not shown on the screen** as it's typed (useful for passwords). |
| `getche()`   | `char c = getche();`      | Same as `getch()`, **but echoes/print the character** on the screen as the user types it. |
| `putch()`    | `putch(c);`               | Prints a **single character** to the screen, just like `putchar()`, but it's from `<conio.h>`. |
| `clrscr()`   | `clrscr();`               | Clears the console screen. Only works in **old compilers** like Turbo C/C++, not supported in modern IDEs like Code::Blocks or GCC. |

---

### Summary Table

| Function   | What It Does                                     | Header File   |
|------------|--------------------------------------------------|---------------|
| `getchar()`| Reads one char from user                         | `stdio.h`     |
| `putchar()`| Outputs one char to screen                       | `stdio.h`     |
| `gets()`   | Reads a line of text                             | `stdio.h`     |
| `puts()`   | Prints a string with newline                     | `stdio.h`     |
| `getch()`  | Reads char instantly without showing it          | `conio.h`     |
| `getche()` | Reads char instantly and shows it on screen      | `conio.h`     |
| `putch()`  | Outputs one char (same as `putchar()`)           | `conio.h`     |
| `clrscr()` | Clears screen (console window)                   | `conio.h`     |


---










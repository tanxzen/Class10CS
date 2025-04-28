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


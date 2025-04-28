> [!IMPORTANT]
> All documentation will be on this readme no sperate files

# CH02 : Introduction to C language 

`C is a general-purpose programming language developed by Dennis Ritchie at Bell Labs in the early 1970s. Ritchie created C as a low-level language that could be used to write efficient and portable system software.`

##

<details>
  <summary>
    Variable  
  </summary>
  
- `A variable is an identifier or a name which is used to refer a value and this value varies or changes during the program execution.`<br>
*example* : *name = tomba , surname = laisharam, age=25*
- `How to declare a variable in C ?`
  - We use a data type specifier along with the variable
     - e.g : `int age ;` , *int is a data type for interger and age is the name of variable*
- `Two types of Variable` :
  - `Global Variable` : *Variable which are declared outside the main function block, and they can be used in the main program block and sub program block like functions.*
  - `Local Variable `: *Variable which are declared inside the main function block, and they are used only in the block in which they are declared. Sub programs or functions can also have local variable.*
- `Initialization and Assignment`

  - `Initialization`: *When we declare a variable and give it a value at the same time, it's called initialization.*
    - **Example**: 
      ```c
      int age = 32;
      ```
      We declare an integer variable named `age` and assign it the value 32 at the same time.

  - `Assignment`: *When we give a new value to an already declared variable, it's called assignment.*
    - **Example**: 
      ```c
      age = 25;
      ```
      The variable `age` was already initialized with the value 32, and now we are updating it to 25.

    - Assignment is not limited to changing values. If a variable was declared but not initialized, we can assign a value to it later.
      - **Example**:
        ```c
        int age;     // Declaration without initialization
        age = 30;    // Assignment after declaration
        ```
</details>

<details>
  <summary>
    Constants
  </summary>

- `Constant : Any unchanged value in a program during program execution is called a constant .`
  
- `Different Types of Constant `:
  
    - `Numeric Constants` :
      
        - 1.`Interger Constant `: *An interger constant is a signed or unsigned whole number.*
          - e.g `-24, 52, 102`
            
        - 2.`Real or Floating Point Constant` : *Any signed or unsigned number with fractional part is called real or floating point constant*
            - e.g `3.14, 0.234, 0.42e-32`
              
    - `String or Character constant` :
      
        - 1.`Single character string constant` : *Any letter or character enclosed in single apostrophe is called single character sting constant*
            - e.g `'h', 'a' , '+'`
              
        - 2.`String of characters constant` : *Any string of characters consisting of letters, digits, and symbols enclosed in double quotes is called string of characters constant*
            - e.g `"letters", "number02" , "person+name+$`
              
</details>

<details>

<summary>
  Library
</summary>

- `Library` :  *A library in C is a collection of pre-compiled functions and routines that can be used in programs to perform common tasks, such as input/output, string handling, or math operations.*

-  `Common Librarys`:

      - `stdio.h` : *provides function and others assets for input/output*

      - `conio.h` : *short for console input output , is a library used by some older compilers like TURBOC++ compiler, that provide functions like getch,clrscr,etc but it's a outdated library*
    
      - `math.h` : *provides mathematical funtions to perform mathematical calculations , funcitons include sqrt, pow,etc*
    
      - `string.h` : *provide funtions for manipilating strings in c , functions include strcpy,strcmp,strlen ,etc*

      - `stdlib.h` : *provides system related functions , like malloc,calloc,free for dynaminc memory allocation*
 
> Sometimes Programmers write their own librarys for their specific needs

</details>

<details>
<summary>Preprocessor Directives</summary>

- `Preprocessor directives in C are instructions that are processed by the C preprocessor before the actual compilation of the program begins. These directives begin with the symbol # and are used to include files, define constants or macros, and control the compilation process conditionally.`
  
- `Types of Preprocessor directives` :
  - 1. `File Inclusion` :  *Used to include contents of another file , `syntax : #include <file>`*

  - 2. `Macro Definition` : *Used to define symbolic constant or macro , `example : #define MONTH 30`*

  - [more are available here](https://www.geeksforgeeks.org/cc-preprocessors/) 
  
</details>

<details>
  <summary>
    C Keywords 
  </summary>

`There are 32 available Keywords in C (version C98/C90)`

```c
auto        break       case        char        const
continue    default     do          double      else
enum        extern      float       for         goto
if          int         long        register    return
short       signed      sizeof      static      struct
switch      typedef     union       unsigned    void
volatile    while
```

  
</details>


#


### Structure of C program :
```c
<Header files>

<Global declaration of variables>

main()
{

  <Local declaration of variables>

  --------------

  <Statements>

  --------------

}

<Sub programs - function blocks>
```

- *The header files tell compiler to include required files to run the program, define maros substitution etc.*
- *Global declaration of variable declares the variable outside the main block meaning the declared variable can be use by any function or also by the main function.*
- *Local declaration of variable means that the variable is declared inside the main block and cannot be used in other sub blocks.*
- *The statements which are written inside the main function will only execute other statements which are written outside the main block will not be executed*
- *functions are just like another main block which will not be executed but which can be call in the main block to do certain actions, work, etc.*

##

### Basic Data types :

- `int` : *refers to interger. It can hold a signed or unsigned whole number within specific range.*
  
- `char` : *refers to characte. It can hold one letter/symbol. In fact, char in C language is associated with integers refers to a letter/symbol as per ASCII which has assigned integer value for all letters/symbol used in programming.*
  
- `float` : refers to floating point or real number. It can hold a real numeber like 3.174813 or 4.53e6 with six decimal digits in decimal or exponential form.,

- `double` : also refers to floating or real number. It can hold a real number in double precision. A double precision number uses 12 decimal digit like 3.42134421232 or 4.2324452423e12.

- [more are available here](https://www.geeksforgeeks.org/data-types-in-c/)

## 

### Operators 

<details>
  <summary>
    Arithmethic Operators 
  </summary>
  
- `+ : addition` , *1 + 1 = 2* 
- `- : substraction`, *2 - 1 = 1*
- `* : multiplication`, *2 * 3 = 6*
- `/ : division`, *8 / 2 = 4*

</details>

<details>
  <summary>
    Relational Operator
  </summary>

- `< : less than` : *5 < 2 : FALSE*

- `> : greater than` : *5 > 2 : TRUE*

- `<= : less than or equal to` : *5 <= 2 : FALSE*

- `>= : greater than or equal to` : *5 >= 2 : TRUE*

- `== : equal to` : *5 == 2 : FALSE* or *5 == 5 : TRUE*

- `!= : not equal to` : *5 != 2 : TRUE*

</details>

<details>
  <summary>
    Logical operators
  </summary>


-`&& : AND` : Returns TRUE if all the given condition or statement are true , if any statement is false , it will always return FALSE <br> *e.g (5<2) && (5>2) : FALSE*

-`|| : OR` : Return TRUE if any of the given condition or statement are true, if none of the condition is TRUE , it will always return FALSE <br> *e.g (5<2) || (5>3) : TRUE*  

-`! : NOT` : Return TRUE if the condition is FALSE , if the condtion is TRUE , it will always return FALSE <br> *e.g !(5<2) : TRUE*


`TRUTH TABLE FOR AND(&&)`


| `OPERAND 1` | `OPERAND 2` | `RESULT` |
| -- | -- | -- |
| `true` | `true` | `true` |
| `true` | `false` | `false` | 
| `false` | `true` | `false` |
| `false` | `false` | `false` |


`TRUTH TABLE FOR OR(||)`


| `OPERAND 1` | `OPERAND 2` | `RESULT` |
| -- | -- | -- |
| `true` | `true` | `true` |
| `true` | `false` | `true` | 
| `false` | `true` | `true` |
| `false` | `false` | `false` |


`TRUTH TABLE FOR NOT(!)`

| `OPERAND` | `RESULT` |
| -- | -- |
| `true` |  `false` |
| `false` | `true` | 

</details>

<details>
  <summary>
    Increment and decrement 
  </summary>


### In the C programming language, increment and decrement are operators that are used to increase or decrease the value of a variable by 1, respectively.

## Increment

The increment operator in C is represented by the `++` symbol. It can be used in two ways:

1. **Pre-increment**: `++variable`
   - The value of the variable is incremented by 1 before it is used in the expression.
   - Example: `x = ++y;` (first increments `y` by 1, then assigns the new value of `y` to `x`)

2. **Post-increment**: `variable++`
   - The value of the variable is used in the expression first, and then it is incremented by 1.
   - Example: `x = y++;` (first assigns the current value of `y` to `x`, then increments `y` by 1)

## Decrement

The decrement operator in C is represented by the `--` symbol. It can also be used in two ways:

1. **Pre-decrement**: `--variable`
   - The value of the variable is decremented by 1 before it is used in the expression.
   - Example: `x = --y;` (first decrements `y` by 1, then assigns the new value of `y` to `x`)

2. **Post-decrement**: `variable--`
   - The value of the variable is used in the expression first, and then it is decremented by 1.
   - Example: `x = y--;` (first assigns the current value of `y` to `x`, then decrements `y` by 1)

Here's an example to illustrate the difference between pre-increment/decrement and post-increment/decrement:

```c
int x = 5;
int y = 10;

// Pre-increment
x = ++y; // x = 11, y = 11

// Post-increment
x = y++; // x = 11, y = 12

// Pre-decrement
x = --y; // x = 11, y = 11

// Post-decrement
x = y--; // x = 12, y = 11
```
  
</details>

<details>
  <summary>
    Assigment
  </summary>


In C programming, assignment operators are used to assign values to variables. The most common assignment operator is the equal sign (=), but there are several compound assignment operators that combine an arithmetic operation with assignment. Here's a brief explanation of some of these operators, along with examples in C code format.

Simple Assignment (=)
Assigns the value on the right to the variable on the left.

```c
int x = 10;  // x is now 10
```

Addition Assignment (+=)
Adds the right operand to the left operand and assigns the result to the left operand.

```c
int x = 10;
x += 5;  // x is now 15 (10 + 5)
```

Subtraction Assignment (-=)
Subtracts the right operand from the left operand and assigns the result to the left operand.

```c
int x = 10;
x -= 3;  // x is now 7 (10 - 3)
```

Multiplication Assignment (*=)
Multiplies the left operand by the right operand and assigns the result to the left operand.

```c
int x = 10;
x *= 2;  // x is now 20 (10 * 2)
```

Division Assignment (/=)
Divides the left operand by the right operand and assigns the result to the left operand.

```c
int x = 10;
x /= 2;  // x is now 5 (10 / 2)
```

Modulus Assignment (%=)
Takes the modulus using the left operand and the right operand and assigns the result to the left operand.

```c
int x = 10;
x %= 3;  // x is now 1 (10 % 3)
```

Bitwise AND Assignment (&=)
Performs a bitwise AND operation on the left operand and the right operand and assigns the result to the left operand.

```c

int x = 0b1010;
x &= 0b1100;  // x is now 0b1000 (0b1010 & 0b1100)
```

Bitwise OR Assignment (|=)
Performs a bitwise OR operation on the left operand and the right operand and assigns the result to the left operand.

```c

int x = 0b1010;
x |= 0b0011;  // x is now 0b1011 (0b1010 | 0b0011)
```

Bitwise XOR Assignment (^=)
Performs a bitwise XOR operation on the left operand and the right operand and assigns the result to the left operand.


```c

int x = 0b1010;
x ^= 0b0101;  // x is now 0b1111 (0b1010 ^ 0b0101)
```

These compound assignment operators provide a shorthand way to update the value of a variable based on its current value. They are widely used in C programming to make code more concise and readable.
  
</details>


<details>

<summary>
  Conditional Operators
</summary>
<br>

Conditional Operator or Ternary operator is used to check a condition and select a value of the condition depending on the value of the condition.
It's just a shorter version of if-else statement completed in one line. 

- `Ternary operator in c` : *syntax :* `(condition)? value 1 : value 2 ;`,
- If the condition is *TRUE* it will execute the `value 1` and if the condition is *FALSE* it will execute the `value 2`.

<br>

`Comparision Ternary and if-else operator :`

<br>

`Ternary`

```c
int a = 10 ;
int b = 15 ;
int big;

big = (a>b)? a : b ; 
```

<br>

`If-else`

```c
int a = 10;
int b = 15;
int big;

if (a>b){
big = a;
}
else {
big = b;
}
```

</details>


<details>
<summary>
  Bitwise Operator
</summary>

>Recommanded not to focus much on these as they are for advance programmers who manages data at bit level<br>
>Some Research on Binary numbers and Base 2 number system will help understand these better ! 

## 🔹 What Are Bitwise Operators?

Bitwise operators work on **individual bits** (0s and 1s) of integer values.  
They perform operations at the binary level.

---

## 🔹 Why Use Bitwise Operators?

They are useful for:
- Low-level hardware programming
- Efficient memory or flag manipulation
- Performance optimization

---

## 🔹 Bitwise Operators in C

| Operator | Name         | Description                                                |
|----------|--------------|------------------------------------------------------------|
| `&`      | AND          | 1 if **both bits** are 1                                   |
| `\|`      | OR           | 1 if **at least one** bit is 1                             |
| `^`      | XOR          | 1 if **only one** of the bits is 1                         |
| `~`      | NOT          | **Flips** all bits (0 becomes 1, and 1 becomes 0)          |
| `<<`     | Left Shift   | Shifts bits **left**, fills 0s on the right                |
| `>>`     | Right Shift  | Shifts bits **right**, removes bits from the end           |

---

## 🔹 Example in C

```c
#include <stdio.h>

int main() {
    int a = 5;   // Binary: 00000101
    int b = 3;   // Binary: 00000011

    printf("a & b = %d\n", a & b);  // 00000001 -> 1
    printf("a | b = %d\n", a | b);  // 00000111 -> 7
    printf("a ^ b = %d\n", a ^ b);  // 00000110 -> 6
    printf("~a = %d\n", ~a);        // In 8-bit: 11111010 -> -6 (2's complement)
    printf("a << 1 = %d\n", a << 1); // 00001010 -> 10
    printf("a >> 1 = %d\n", a >> 1); // 00000010 -> 2

    return 0;
}
```

---

## 🔹 Quick Bit Reference

```text
a = 5  = 00000101
b = 3  = 00000011

a & b  = 00000001 = 1
a | b  = 00000111 = 7
a ^ b  = 00000110 = 6
~a     = 11111010 = -6 (in 2's complement)
a << 1 = 00001010 = 10
a >> 1 = 00000010 = 2
```

---

</details>

---


# HOW TO WRITE A C PROGRAM | WRITING A C PROGRAM 

### To write a program , you need to understand the language properly i will try to make you understand some concepts and rule .

`These part is based on my current knowledge and experience , i too am a student of class 10 learning c , right now 2025 , so any questions and issues are requested to post on issue page, thanks`

<details>

<summary>
  Why do we need to include header files ? 
</summary>


### Why do we need to include header files ?

`We include header file because they contain pre-define functions , macros which will help us write a program without making complex functions .`

*We can also write a program without including a header file but we need to write our own functions like example we do not want to include the stdio.h header file but this header file give us the required functions for input/output like printf and scanf so if we do not include the stdio.h header file we need to make a custom funtion for printing and getting user input like printf and scanf by ourself*

### TL;DR

`We include header file to use pre-define functions , macros so if we do not include them we need to make the funtions ourself`


</details>

<details>

<summary>
  why int/void main() funtion ?
</summary>

### Why most of the time main() has int/void next to it like int/void main() ? 

> using void is also discourage for large projects

`Main function is the only function which is executed by the program. So a funtion need a type right ? so we are specifying the type of our main funtion int meaning it was a integer return type and void means no return type and the OS also checks for return type to determine what happen to the program running ?`

- *For every funtion there should be a type and the types can be our choice wheather int/void it totally depends on us*<br>
- *if we want to debug our code we specify the return type to `int`  to main because when the main program executes successfully it return 0 and when it had error it return 1*<br>
- *if we dont want to debug or bother with returns we specify `void` to main because when it executes it will not return anything*<br>
- *the OS or the system check the program running so it check via the return type if return was 1 it knows the program has ran into an error and will notify you*

### TL;DR

`We use int/void to main because main is also a funtion and every funtion needs its type to determine return type and we use int when we need to debug code because it returns 0 when it works and 1 when it gives error and we use void to specify no return type meaning nothing will return and bother and the os also check the program condition using return values`.

--- 

### 🙃 After this did i just sense another question XD ? if not 😳 i will try to list it 

### Q. Then why can't we use char main() or float main() ?

`We can use char or float type with main but it is highly discourage because the OS or the system checking the program condition via the return value
will not be able to understand char return and float return as said in the above that 0 and 1 are used for success and error and there are no know values for char and float return.`

### TL;DR 

`We can use char or float main but it is highly discourage as the OS will not know the return values because the OS does not have any idea what a char or float return means as it works on 0 and 1 for return`

</details>

```c

// Declaring a variable 
// we use a type specifier to declare a variable [ int , char , float , double] choose the required type

int age = 25 ; // int for age as it is interger ;

char name[20] = "tomba" ; // we are using array it's just a collection of many char

float pi = 3.14 ; // we are using float for decimal numbers 
```









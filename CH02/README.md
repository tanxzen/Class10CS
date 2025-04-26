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
- `Common Librarys`:
    - `stdio.h` : *provides function and others assets for input/output*
    - `conio.h` : *short for console input output , is a library used by some older compilers like TURBOC++ compiler, that provide functions like getch,clrscr,etc but it's a outdated library*
    - `math.h` : *provides mathematical funtions to perform mathematical calculations , funcitons include sqrt, pow,etc*
    - `string.h` : *provide funtions for manipilating strings in c , functions include strcpy,strcmp,strlen ,etc*
    - `stdlib.h` : *provides system related functions , like malloc,calloc,free for dynaminc memory allocation*
 
> Sometimes Programmers write their own librarys for their specific needs

</details>


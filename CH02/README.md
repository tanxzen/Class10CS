# CH02 : Introduction to C language 

`C is a general-purpose programming language developed by Dennis Ritchie at Bell Labs in the early 1970s. Ritchie created C as a low-level language that could be used to write efficient and portable system software.`

##

## Variable : 
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

## Constants 
- 


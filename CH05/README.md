

# CH05 : Loop Control Structures in C

<p>
  
  Loops control structures are used to execute and repeat a block of statements depending on the value of a condition.
</p>

### `Types of Loops` : 

  - `For Loop`
    
  -  `While Loop`

  -  `Do - While Loop`

---

<details>

<summary>For Loop</summary>

### For Loop 

<p>

  A `for` loop is used to execute and repeat a block of statements depending on a condition.
</p>

  **syntax** :
```c
for (<initial value>; (<condition>); <increment>)
{
  -----------------
  <statement block>
  -----------------
}
```
<p>

Where `initial value` is the assignment expression which initializes the value of a variable.
`condition` is a relational or logical expression which will have the value `true` or `false`.
`increment` is the increment value of the variable which will be added every time.
</p>


### Example : 
```c
int i;
for (i = 0; i<=5 ; i++){
  printf("This will execute 5 times ! \n");
}
```

- The statement inside the for loop will execute upto 5 times because the initialize value `i`, is set to `0` , so if `i < 5` then will run for 4 times but there is `=` sign making it `i<=5` meaning it will execute until `i` becomes `5`.

</details>


<details>

<summary>Nested For Loop</summary>

When a for loop is place inside another for loop it is called nested for loop.

**Example** : 
```c
for (int i = 0 ; i<10; i++){
    for(int j = 0 ; j<20 ; j++){
        printf("Nested For Loop\n");
    }
}
```
</details>

<details>


<summary>While Loop</summary>

<p>

  A while loop is used to execute and repeat a block of statements depending on a condtion.
</p>

**syntax**:
```c
while(<condition>)
{
  -----------------
  <statement block>
  -----------------
}
```
<p>

  Where `condition` is a relational or logical expression which will have the value `true` or `false`.
</p>

### Example :

```c
int i = 0;

while (i<=10){
  printf("%d\n",i);
  i++;
}
```
<p>

  In the following code the initial value of the i is 0 but when we use while statement the while condition will be true because the value of i, which is 0 is less than 10 so it will continue until the value of i reached 10 and giving the result of printing 0 to 10.
</p>
</details>



<details>


<summary>Do-While Loop</summary>

<p>

  A do-while statement is also used to execute and repeat a block of statements depending on a condition.
</p>

**syntax**: 
```c
do
{
  -----------------
  <statement block>
  ----------------
}
while (<condition>)
```
<p>

  Where `conditon` is a relational or logical expression which will have the value `true` and `false`.
</p>

When this statement is executed the computer will execute the statement block irrespective of the value of the condition. At the end of statement block, the condition is evaluated. If the value of the condition
is `true` the statement block is executed again and is repeated until the condition is `false`.

  
</details>

<details>

<summary>Goto Statement</summary>

<p>

  The `goto` statement is an unconditional transfer of control statement. It is used to transfer the control from one part to another.
</p>

**syntax**: 
```c
goto label ;
------------
------------
label:
------------
```
<p>

  Where `label` is the statement label which is available anywhere in the program . Its the identifier which is used to mark the beginning of the another part of the program which will be transfer by the `goto` statement.
</p>
  
</details>


<details>

<summary>Break statement</summary>

<p>

  The break statement is use to transfer the control to the end of a statement block in a loop. 
</p>

**syntax**:
```c
break;
```

<p>

  Break is frequently used in the `case` block of `switch` statement. 
</p>

### Example :
```c
char n = 'a';

switch(n){
  case 'a' : printf("a is for apple");
             break;
  case 'b' : printf("b is for ball");
             break;
  case 'c' : printf("c is for cat");
             break;
  case 'd' : printf("d is for dog");
             break;
  default : printf("Invalid input ! please enter a,b,c and d only.";
             break; 
}
```

<p>

  In the given example `break` statement is used after every end of the case because if break statement is not present , then if any of the condition is match it will execute all the case meaning it will activate all case and cause error in the program.
</p>

</details>














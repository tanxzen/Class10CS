

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

  In the following code the initial value of the i is 0 but when we use while statement the while condition will be true because the value of i, which is 0 is less than 10 so it will continue untill the value of i reached 10 and giving the result of printing 0 to 10.
</p>
</details>



  
</details>


# CH04 : Control Statement in C



### `Two types of Control Statement` : 
  - if-else statement
   - switch statement

<br>

### `If-else` : 

<p>
  If-else statement is used to execute a statement block or a single statement depending on the value of a condition. 
</p>

  **syntax** :
```c
if (condition)
{
  ------------
  <true block>
  ------------
}
else
{
  -------------
  <false block>
  -------------
}
```
Where `conditon` is a logical expression which will have the value of true or false.

### nested if-else statement 

<p>
  
  An if statement may have another if statement in the `true block` and `false block`.This compound statement is called nested if statement.

</p>

  **syntax** :
```c
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
```

### switch statement

<p>
  switch statement is used to create a block of statements depending on the value of a variable or an expression.
</p>

**syntax** :
```c
switch ( <expression>)
{
case <label 1>: {
                  -------------
                  <statement block 1>
                  -------------
                  break;
                }
case <label 2>: {
                  -------------
                  <statement block 1>
                  -------------
                  break;
                }
case <label n>: {
                  -------------
                  <statement block n>
                  -------------
                  break;
                }
default:        {
                  -------------
                  <default statement block>
                  -------------
                  break;
                }
}
```
where `<expression>` refers to any `int` or `char` expression or variable. <br>
      `<label 1>`, `<label 2>`...`<label n>` are values which will match with the value of the expression. <br>
      **break** is a statement which will transfer the control to the end of **switch** statement.

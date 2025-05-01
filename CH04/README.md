
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


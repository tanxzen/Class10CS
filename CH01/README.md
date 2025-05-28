# CH01 : Algorithm for Problem Solving 

### MORE ALGORITHM ARE COMING SOON ...

`RECOMMANDED TO READ THE Algorithm.txt AS IT HAS EXPLAINATION WITH SOME DETAILS`

## Overview 

- `Swapping two values` : *use another variable to store the value of a variable1 then replace the value of the variable 1
                        with value of variable 2 then replace the value of the variable 2 with value of variable 3.*
- `Biggest Number between 2 number` : *use another variable big , if value of variable1 > variable2 then big = variable1 else big = variable2*
- `Farenheit (°F) to Celsuis (°C)` : *use a variable ces = 5/9 (°F - 32) , where °F is the given farenheit ... <br>`Formula : 5/9 (°F - 32)`*
- `Sum of n natural number` : *use i=0, sum=0 and we will use while loop untill i is not equal to n and inside the loop we will add sum and i and i + 1* example :<br> *while i != n <br> sum = sum + i <br> i = i + 1*
- `FACTORIAL of n term OR Product of n natural number` : *use i=0, pro=1 and we will use while loop untill i is not equal to n and inside the loop we will multiply pro and i and i + 1* <br>example :<br> *while i != n <br> pro = pro * i <br> i = i + 1*
- `Reverse digit of a given number` : *use two variable lastdigit and reverse , let n = 123 now we assign lastdigit = n % 10 , % give remainder of a division now we will loop through a while loop , while n is greater than 0 we will assign reverse = reverse * 10 + lastdigit then we will again assign lastdigit = n % 10 and lastly we reduce n by dividing it by 10*<br> example :<br> *lastdigit=n%10<br>while n>0<br>reverse = reverse * 10 + lastdigit<br>n = n/10*

- `Swapping number without another variable`

   Let a and b be the two numbers then we will write an expression like <br>
   a = a+b <br>
   b = a-b <br>
   a = a-b<br>

   so lets assume the a=1, b=2 then we have a = 1+2 =3 <br>
   b = 3-2 =1<br>
   a = 3-1 =2<br>

### Advance Algorithm :

1. Finding element in an array :
 Take a array `arr[9] = {1,2,3,4,5,6,7,8,9,10}` which contains 10 elements (remember that array index start from 0) and we want to find an element lets say `6` then we will initialize a variable with the element we want say `searchElement = 6` and we loop through the array to check if the array at index `i`(we are using for loop like `for(int i=0;i<=9;i++)`)then in the block we check if arr[i] is matching to the
  `searchElement` if yes, we print the index of `i`.

Sample Code.
```c
int arr[9] = {1,2,3,4,5,6,7,8,9,10};
int searchElement = 6;

for(int i=0;i<=9;i++){
  if(arr[i] == searchElement){
    printf("Found %d at index %d\n",searchElement,i);
  }
}
```
Output :
```
Found 6 at index 5 
```
Note : the counting of index should start from 0.

    
2. Sorting array (Bubble sort Alogrithm)

>sizeof() operator is used to get the size of any datatype , variable .
>
>example : sizeof(int) >>output>> 4 
>
>Reseach more or a quick view on https://www.geeksforgeeks.org/sizeof-operator-c/
>

Sample code : 
```c
int arr[9] = {9,10,3,2,1,7,5,8,4,6};
int size = sizeof(arr)/sizeof(int);
int temp;

for(int i=0;i<size - 1;i++){
  for(int j=0;j<size - i - 1;j++){
    if(arr[j] > arr[j+1] ){
        temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
    }
  }
}

for{int k = 0;k<size;k++}{
  printf("%d ",arr[k]);
}
```
Output :
```c
1 2 3 4 5 6 7 8 9 10
```

Using the same array as used in the `point 1` with random numbers , 'arr[9] = {9,10,3,2,1,7,5,8,4,6}' and to sort we need to use nested loop and we will be using for loop and we need to get the size of array 
so we use the sizeof(arr return the sizeof array) then we divide the result of sizeof(arr) by sizeof(int)(the datatype of the array) this will return the sizeof the int meaning the total size of int array is divide by the size of 1 element present then this will return the number of element present inside the array then we store the value in a variable call `size`.Then we intialize a temporary variable say, `temp` and we loop the counter variable is `i` through the array with for loop unitl `size - 1` because the last value will already be the sorted(meaning it already done).Then we add a nested for loop with the loop counter as `j` to loop until `size - i - 1 (i is the first for loop counter variable)` we use this size - i - 1 because it skips the already sorted values. Then we add a condition `if (arr[j] > arr[j+1]) (we use the '>' greater than symbol to organise according to accending order you can also use the '<' less than symbol to sort decending value)` we are checking if the current index value is greater then the next index value , if yes we execute the statement to switch the we put the value of current arr to temp `temp = arr[j]`, then we change the value of current array to the next array value `arr[j] = arr[j+1]` and lastly we change the value of next array to the current array value `arr[j+1] = temp`.    


---

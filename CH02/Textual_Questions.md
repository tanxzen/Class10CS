# REVIEW QUESTIONS AND EXERCISES
1. What is a constant? Explain the constants in C. <br>
    Ans : Any unchanged value in a program during the program execution is called constant.<br>
     In C language, constant are divided into two types Numeric and String or character :<br> 
     1. Numeric Constant :<br>
            i.Integer constant : an integer constant is a signed or unsigned whole number.<br> 
                    eg. -23,12,+240.<br>
           ii.Real or Floating point constant : Any signed or unsigned number with fractional part is called real or floation point constant.<br>
                    eg. -23.41, +234.21,3.14<br>
        
    2.String or character constant : <br>
            i.Single character string constant : any letter or character enclosed in single apostrophe is called single character string constant.<br>
                    eg. 'a','$','+'.<br>
           ii.String og characters constant : any string of characters consisting of letters, digits and symbols enclosed in double quotes is called string of characters constant.<br>
                   eg. "Some Names", "India +91","$$Money".

2. What is a variable? How are the variables declared in C?<br>
Ans : A variable is an identifier or a name which is used to refer to a value and this value varies or changes during the program execution.Variabe used in a C program are declared with appropriate datatypes along with their name.


3. What is an expression? What are the operators in C? <br>

Ans : An expression consists of variable and constants seperated by operators.

4. What is a library function? Mention its use. <br>

Ans : Library functions are the build in program that are available with the compiler.It is used to perform standard mathematical operations. <br>
        eg. sqrt(),fabs(), log(),etc.

5. Convert the following mathematical expressions into C expressions. <br>
(i) $\frac{a+b}{c+d}$ <br>
(ii) $\frac{ab}{c^2+d}g$ <br>
(iii) $\sqrt{1+x}\frac{\log\ \cos2x\}{1+|y|}$ <br>
(iv) $z =e^x+ \log\ y+ pqr(s-t)$ <br>
(v) $T =\sin(a)\ cos(b) - |g-h|+\sqrt{ab}$ <br>
(vi) $z\frac{\alpha+\beta}{\sin\ x^o} + \frac{a^b+c^d}{a+b}$ <br>
(vii) $y = \sin\ \omega \pi\ \cos\frac{\omega\pi}{t}$ <br>

Ans : 
```
i. (a + b) / (c + d)
ii. (a * b) / (pow(c, 2) + d) * g
iii. sqrt(1 + x) * (log(cos(2 * x)) / (1 + fabs(y)))
iv. z = exp(x) + log(y) + p * q * r * (s - t);
v. T = sin(a) * cos(b) - fabs(g - h) + sqrt(a * b);
vi. z * (alpha + beta) / sin(x * M_PI / 180) + (pow(a, b) + pow(c, d)) / (a + b)
vii. y = sin(omega * M_PI) * cos((omega * M_PI) / t); 
```

6. Explain the program structure in C language.<br>

Ans : 
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
1.The header files or preprocessor directives gives instructions to the compiler to include compiler options(#include),macro substitution(#define) to substitude a constant for an identifier and conditional(#ifdef) directives.
2. The main statement block, function block and other blocks used in C program are enclosed in braces {}.
3. Variables declared outside main() are called global variables, and they can be used in the main program block and sub program block.
4. Variables declared inside main() are called local variables, and they are used only in the block in which they are declared.Sub programs/functions can also have local variables.
5. Any C program has coding in the form of letters and symbols.Normally documentation to the program is made by adding remarks or comment lines enclosed  in /* and */ whenever necessary.

7. Explain the different data types in C.
8. Discuss increment and decrement operators available on C and the rules associated with them.
9. Explain arithmetic and logical operators in C with suitable examples.
10. Explain bitwise logical operators available in C. Discuss the order of evaluation.
11. List the different types of operators in C. Discus the following with examples: (a) conditional operators (b) relational operators.
# SHORT QUESTIONS 
1. C language has been developed by _________.
2. Like decimal number system, octal and hexadecimal system can also be used in C language. (True/False) 
3. An octal mumber is preceded by ________ and a hexadecimal number in preceded by _________.
4. An identifier/variable can begin with `_`(underscore). (True/False) 
5. Mention the basic data types used in C language. 
6. A variable declared as `long int` occupies _________ bytes of memory.
7. If 'a' is an integer variable, then a=5/2 will return value __________.
8. Bitwise operators are for manipulation of ______________ in bit level.
9. Define nibble and byte. 
10. Explain terniary operator. 
11. What is the purpose of type declaration in C?
12. What are library functions? Mention any four library functions in C (functions available in math.h)?
13. What are the logical operators available in C? 
14. How does x++ differ from ++x? 
15. __________ is the operator which represents the bitwise OR operator. 
16. What is an identifier? 
17. A variable in C can be declared as float (real) if it is within the range _________ to ___________.
18. The relational operation that are commonly used in C are,__________,___________,_________,___________,___________,_________.
19. In C language a comment starts with the symbol _________ and ends with ___________.
20. Discuss the increment operator in C. 
21. Discuss the decrement operator in C.
22. What are the bit operators used in C.
23. Determine the value of the following logical expression for a=5, b=10, c=-6.
    (i) a == c ¦¦ b > a
    (ii) b > c && < 0 a > 0
24. Which of the following identifiers are invalid.
    (i) total
    (ii) average_value
    (iii) 6month
    (iv) cd 200
    (v) _sum
    (vi) rate$
25. For 9%4 the output is _________.
26. i += 1 can also be written as _____________.
27. __________ is the operator which represents bitwise exclusive OR.
28. How does the type `float` differ from `double` in C language? 
29. What is an operator? What is an operand? 
30. Explain with an example the usage of shorthand assignment operator. 
31. Mention the applications of C language. 
32. What do you mean by case-sensitive? Is C a case-sensitive language? 
33. ___________ data items are real data items that provide greater precision than is normally provided by the real data items.
34. Give the declaration for the string "COMPUTER" in C. 








 

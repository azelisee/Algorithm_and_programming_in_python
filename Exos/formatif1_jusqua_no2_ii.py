Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> (2+5)*9**0.5
21.0
>>> 2//3-27%5/4
-0.5
>>> "2"+"3"+"1+3"
'231+3'
>>> 
>>> 0b1100110011
819
>>> 0xaf6
2806
>>> bin(0xaf6)
'0b101011110110'
>>> int(0x5b)
91
>>> "111011".zfill(16)
'0000000000111011'
>>> x=3
>>> y=x+2
>>> (y-x)**2//5
0
>>> x=2
>>> x=x+3
>>> y,z=x+1,x-2
SyntaxError: multiple statements found while compiling a single statement
>>> x=3
>>> 
SyntaxError: multiple statements found while compiling a single statement
>>> x=2
>>> x=x+3
>>> y,z=x+1
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    y,z=x+1
TypeError: cannot unpack non-iterable int object
>>> x=2
>>> x=x+3
>>> y,z=x+1,x-2
>>> print("\n\tx=",x,"\ty=",y,"\tz=",z)

	x= 5 	y= 6 	z= 3
>>> n=int(input("Saisissez un entier:"))
Saisissez un entier:
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    n=int(input("Saisissez un entier:"))
ValueError: invalid literal for int() with base 10: ''
>>> n=int(input("Saisissez un entier:"))
Saisissez un entier:2
>>> if n<10:
	x=n**2-n//3
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> 

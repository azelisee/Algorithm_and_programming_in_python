Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[10, 100, 0, 1000 5, 5000, 1, 500, 50]
SyntaxError: invalid syntax
>>> x=[10, 100, 0, 1000, 5, 5000, 1, 500, 50]
>>> y=x
>>> y[2]=10000
>>> x
[10, 100, 10000, 1000, 5, 5000, 1, 500, 50]
>>> 
>>> 
>>> 
>>> z=x[:]
>>> z[2]=50000
>>> z
[10, 100, 50000, 1000, 5, 5000, 1, 500, 50]
>>> x
[10, 100, 10000, 1000, 5, 5000, 1, 500, 50]
>>> x[3]-z[4]
995
>>> x[3]%z[4]
0
>>> x[3]//z[4]
200
>>> x[2]**0.5
100.0
>>> max(z)
50000
>>> min(y)
1
>>> x.sort()
>>> x
[1, 5, 10, 50, 100, 500, 1000, 5000, 10000]
>>> w=sorted(z)
>>> w
[1, 5, 10, 50, 100, 500, 1000, 5000, 50000]
>>> range(10,20)
range(10, 20)
>>> list(range(10,20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(10,20,4))
[10, 14, 18]
>>> list(range(10,20,-4))
[]
>>> [0]*6
[0, 0, 0, 0, 0, 0]
>>> z=[0,1,2]
>>> z*4
[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
>>> t=[5,4,3]
>>> z+t
[0, 1, 2, 5, 4, 3]
>>> 

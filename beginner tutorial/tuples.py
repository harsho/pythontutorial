'''
Python knows number of compound data types, 
used to group together other values.
They are:
tuple 
dictionary
set 
list

Tuples are writeen as a list of comma-separated values
(items) between brakets.

Tuples re immutable - this means that items can not be changed. 
However, a tuple can contain mutable objects.

Tuple has 2 methods available.
count() returns the number of elements with the specified value
index() returns the index of the first element with the specified value
'''

#The basics - tuple packing
from re import X


t = 12345, 54321, 'hello!'
print(t[0])
print(t)

#Tuples may be nested
u= t, (1,2,3,4,5)
print(u)

#Tuples are immutable:
t[0] = 8888

#but they can contain mutable objects:
v = ([1,2,3], [3,2,1])
print(v)
print(v[0][1])
#Indexing
'''
+---+---+---+---+---+---+---+---+---+
| D | i | d | C | o | d | i | n | g |
+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   
-9 -8  -7  -6  -5  -4  -3  -2  -1
'''
t[0]
t[-1]

#trailing comma
empty = ()
singleton = 'hello', 'test'
print(len(empty))
print(len(singleton))
print(singleton)

#unpacking a tuple
x, y, z = t
print(x)
print(y)
print(z)
#t=[1,2,3]

#built-in function tuple()
x = tuple(['bobby', 'at', 'didcoding', 'dot', 'com']) #creates a tuple object
print(x)

#Tuple comprehension...Just use list comprehension with the tuple function 
tuple([x**2 for x in range(10)])
#make venv
    # python3 -m venv my_venv_
#activate venv
    #source /home/harshdev/Documents/my_venv_/bin/activate
#activate interpreter mode
 #python3 and Ctrl+z to quit
# python tutorial doc here
# #https://docs.python.org/3/tutorial/index.html



print('freecodecamp python tutorial for beginners')


# (0:19:30) Numbers
'''
+ - / * %
// floor division
exponents pow(3, 2) or x**y



Assignment Opperators:
= equals

int
float (2.5, 5.78894567)

built in Function:
round(n,d) rounds a number to a specified decimal

bigger ints can be written as 
1000000000 to 1_000_000_000 to improve legibility

 
'''
print('Numbers: simple operations')
print(2+2)
print(2-5)
print(5*10)

print('Numbers: division operations')
print(10/4)
print(10//4)
print(10%4)
print(divmod(10,4))


print('Numbers: Pemdas')
print(50-5*6)
print((50-5*6)/4)
print(5*3+2)

print('Numbers: Power of')
print(5**2)
print(2**7)
print(pow(2,7))

print('Numbers: variables')
width = 60
height = 3*7
print(width)
print(height)
print(width * height)

print('Numbers: In interactive mode, the last printed experssion is assigned to the variable _. ')
tax = 12.5/100
price = 100.50

print(tax)
print(price)
print(price*tax)

_ = (price*tax) #this would be the assignment in interactive mode
print(round(_,2))


# (0:29:46) Strings

'''
Python can be used to manipulate strings, which can be expressed in several ways. 

They can be enclosed in single or double quotes

'\' can be used to escape quotes

Python strings cannot be changed - they are ummutable. 

The built in function called len()
This Funtion returns the length of a string:

Strings have a bundh of methods available. 
capitalize() Converts the first characcter to upper case
casefold() Converts string into lower case
center() returns a centered string
count() returns the number of times a specified value occurs in a string
encode() returns an encoded version of the string 
endswith() returns true if the string ends with the specified value 
expandtabs() sets the tabsize of the string 
find() searches the string for a specified value and returns the position of where it was found
format() formats specified values in a string
format_map() formats specified values in a string
index() Searches the string for a specified value and returns the position of where it was found
isalnum() returns true if all charecters are alphanumeric
isalpha() returns true if all charecters are in the alphabet
isascii() returns true if all charecters in the string are ascii charecters
isdecimal() returns true if all charecters in the string are decimanls
isdigit() returns true if all charecters in the string are digits
isidentifier() returns true if the string is an indentifier
islower() returns true if all charecters in the string are lowercase
isnumeric() returns true if all charecters in the string are numeric
isupper() returns true if all characters in the string are upppercase
isprintable() returns true if all charecters in the string are printable
isspace() returns true if all charecters are whitespaces
istitle() returns true if string follows rule of a title
join() converts elements of an iterable into a string
ljust() converts left justified version of a string
lower() coverts string into lowercase
lstrip() returns a left trim version of the string
maketrans() returns a translation table to be used in translations
partion() returns a tuple where the string is parted into three parts
replace() returns a string where a specified value is replace with a specified value
rfind() searches the string for a specified value and returns the last position of where it was found
rindex() searches the string for a specified value and returns the last postion of where the index
rjust() returns a right justified version of the string
rpartition() returns a tuple where the string is parted into threee parts
rsplit() splits the string at the specified sparator, and returns a list
rstrip() returns a right trim version of the string 
split() splits the string at the specified separator and returns a list
splitlines() splits the string at line breasks and returns al list
startswith() returns true if the string starts with the specified value
strip() returns a trimmed version of the string 
swapcase() swaps cases, lower casse becomes upper case and vice vresa
title() converts the first character of word to uppercase
translate() returns a translated string
upper() converts a string into all uppercase
zfill() fills the string with a specified number of 0 values at the beginning

'''
print('Strings: the basics')
print('scrambled eggs')
print('doesn\'')
print("doesn't")
print("They said \"yes\".")
print('They said "yes".')


#new line
s = 'Firstline. \n Second line.'
s #without print s includes "\n" in output
print(s)

#raw string
print('C:\some\name') #here \n means newline
print(r'C:\some\name') #note the r before the quote

#string literals
print("""\
Usage: thingy [OPTIONS]
-h                  Display this usage message
-H hostname         Hostname to connect to 
""")

#concatenated
print(3*'un'+ 'ium')
'Did' 'Coding'
text = ('put several strings withing parentheses ' 'to have them joined together.')

print(text)

#this only works with 2 literals though,
#not with variables or expresions:
prefix = 'did'
#prefix 'coding' invalid
print(prefix+' coding')

#indexing
print('Strings: indexing')
'''
+---+---+---+---+---+---+---+---+---+
| D | i | d | c | o | d | i | n | g |
+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   
-9 -8  -7  -6  -5  -4  -3  -2  -1
'''
word = 'Didcoding'
print(word[0])
print(word[5])
print(word[0:2]) #0 include 2 exclude
print(word[2:5]) #2 include 5 exclude
print(word[:2]) #beginning to 2 exclude
print(word[4:]) #4 include to the end
print(word[-2:]) #second to last include to the end

print(word[:2]+word[2:])
print(word[:4]+word[4:])

'''
D
d
Di
dco
Di
oding
ng
Didcoding
Didcoding
'''

#changing strings
# word[0]='P' not suppported
print('P'+ word[1:])
print(word[:2]+ 'di')

#String length
s = 'bobby-didcoding'
print(len(s))


#handy built-in functions
print('Strings: Handy built-in functions')
'''
When you don't need fancy output but just want a quick display of some vairables for devugging purposes 
you can convert any value to a string with the repr() or str() funcitons. 

The str() funciton is meant to return representations of values 
which are fairly human-readable, while repr() is meant to generate 
representations which can be read by the interpreter

You also have format().
The format() method formats the specified value(s) and insert them insed the 
string's placeholder '{}' .
'''

x=20
y=400
print(repr((x,y, ('spam', 'eggs'))))
print(str((x,y, ('spam', 'eggs'))))

print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# (0:42:43) Lists
'''
Python knows a number of compound data types,
used to group together other values. The most 
versitile is a list.

Others include:
tuple
dictionary
set


Lists are written as a list of comma-seperated values (items) between square brackets

Lists are mutable - this means that items can be changed 

Lists have a bunch of methods available. 
append()adds an element at the end of the list
clear() removes all the elements from the list
copy() returns a copy of the list
count() returns the number of elements with the specified value
extend() add the elements of a list (or any iterable), to the end of the current list
index() returns the index of the first element with the specified value
insert() adds an element at the specified position
pop() removes the element at the specified posistion
remove() removes the first item with the specified value
reverse() reverses the order of the list
sort() sorts the list

'''

print('Lists: the basics')
squares= [1, 4, 9, 16, 25]
print(squares)

# indexing same as strings
'''
+---+---+---+---+---+---+---+---+---+
| D | i | d | c | o | d | i | n | g |
+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   
-9 -8  -7  -6  -5  -4  -3  -2  -1
'''

print(squares[0]) #indexing returns the item
print(squares[-1])
print(squares[-3:]) # slicing returns a new list

#create a list copy
print(squares[:])

#concatenation 
print(squares + [36, 49, 64, 81, 100])

#alter items
cubes = [1, 8, 27, 65, 125]
cubes[-2] = 64
print(cubes)

cubes.append(216)
cubes.append(7**3)

print(cubes)

#length
letters = ['a','b','c','d','e']
print(len(letters))

#nesting
print('Lists: nesting')
a = ['a','b','c']
n = [1, 2, 3]
x = [a, n]

print(x)
print(x[0])
print(x[0][1])


#list comprehension
print('Lists: list comprehension')
y= []
for x in range(10):
    y.append(x**2)

print(y)
y= [x**2 for x in range(10)]
print(y)

#built-in funciton list()
print('Lists: built-in funciton list()')
x = list(('bobby', 'at', 'didcoding', 'dot', 'com')) #creates list object
print(x)

# (0:53:47) Tuples
'''
Python knows numver of compound data types, 
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
print('tuple: basics')

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

# (1:03:04) Sets
'''
Python knows a number of compound data types,
used to group together other values.

They are:
tuple 
dictionary
set 
list


A set is an unordered collection with no duplicate elements. 
Like a dictionary, a set is defiend by a curly bracket.

Sets are mutable - this means that items can be changed.

Set has a whole bunch of methods availible:
add() adds an element to the set
clear() removes all the elements from the set
copy() returns a copy of the set
difference() returns a set containing the difference between two or more sets
difference_update() removes the items in this set that are also included in another, specific set
discard() remove the specified item
intersection() returns a set that is the intersection of two or more sets
intersection_upate() Removes the items in this set that are not present in other, specifc sets
isdisjoint() returns whether two sets have a intersection point
issubset() returns whether another set contains this set or not
issuperset() returns whether this set contains another set or not
pop() removes an element to the set
remove() removes the specified element
symmetric_difference() returns a set with the symmetric differences 
symmetric_difference_update() inserts the symmetric differences from this set and another 
union() return a set containing the union of sets
update() update the set with another set, or any other iterable
'''

print('Sets: The Basics')
#the basics
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #show that duplicates have been removed

print('orange' in basket) #fast membership testing
print('crabgrass' in basket)

#Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alakazam')
a # unique letters in a 
a-b # letters in a but not in b
a | b #letters in a or b or both
a & b #letters both in a and b
a ^ b #letters in a or b but not both

#set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}

#built in funcitons
x = set(('bobby','bobby', 'at', 'didcoding', 'dot', 'com')) # creates set object

print(x)


# (1:10:29) Dictionaries
'''
Python knows a number of compound data types,
used to group together other values.
One of the most used is dictionary
others include:
set
tuple
list

Dictionaries are used to store data values in key value pairs.

some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a_value'],
    'a_key_4': {'a_dict': 'as a_value'}
}


Dictionaries are mutable - this means that item values can be changed 

Dictionaries have a bunch of methods available
clear() removes all the elements from the dictionary
copy() returns a copy of the dictionary
fromkeys() returns a dictionary with the specified keys and value
get() returns the value of the specified key
items() returns a list containing a tuple for each key value pair
keys() returns a list containing the dictionary's key
pop() removes the element with the specified key
popitem() removes the last inserted key-value pair
setdefault() returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update() updates the dictionary with the specified key-value pairs
values() returns a list of all the values in the dictionary
'''
#The Basics

some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a_value'],
    'a_key_4': {'a_dict': 'as_a_value'}

}
print(some_dict)


print(some_dict[0])
print(some_dict['a_key'])
print(some_dict['a_key_4'])

#Create a dict copy
some_dict.copy()

#altering a dict
some_dict['a_key'] = 'new_value'
print(some_dict['a_key'])

#length
len(some_dict)

#show all keys and values
print(some_dict.keys())
print(some_dict.values())

#Dict comprehension 
{x: x**2 for x in (2, 4, 6)}

#built-in function dict()
x = dict(a=1, b=2, c=3, d=4)


# (1:19:29) If statements
'''
Python uses the usual flow control known from other langauages with some twists.
Perhaps the most well know statement type is the if statement.

Think of an if statement as a way to check to see if conditions are met:

If a condition is met, do something...

else do something differrent!

elif stands for else if

both elif and else are optional


'''
#The basics

#defining a function
def number_play(x):
    if x < 0:
        x=0
        print('negative change to zero')

    elif x ==0:
        print ('zero')
    elif x ==1:
        print('single')
    else:
        print('more')

number_play(-1)
number_play(0)
number_play(1)
number_play(2)


# (1:26:43) Match statements
#requires python 3.10



# (1:36:48) Loops
'''
Python's for statement iterates over the items of any sequence 
(a list or a string), in order that they appear in the sequenc.

The built-in range function 'range()' comes in handy if you do need 
to iterate over a sequence of numbers. It generates arithmetic progressions:

range(start, stop, step)
start
the value of the start parameter (or 0 if the parameter was not supplied)
stop
The value of the stop parameter
step 
the value of the step parameter (or 1 if the parameter was not supplied)
'''

#the basics
words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

#create a sample collection
users = {
    'Quinn': 'active',
    'Eleonore': 'inactive',
    'John': 'active'
}    

# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
     del users[user]

#Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
      active_users[user] = status

#using the range function
for i in range(5):
    print(i)

#...remember range(start, stop, step)
list(range(5,10))
list(range(0,10,3))
list(range(-10, -100, -30))

a = ['Mary', 'had','a', 'little','lamb']
for i in range(len(a)):
    print(i, a[i])

#using the built-in sum function
sum(range(4))

# (1:49:50) Loop clauses
'''
Python has a few statements and clauses that we can use in loops.
These are:
break 
continue 
else
pass

Loop statements may have an else clause: it is executed when the 
loop terminates through exhaustion  of the iterable (with for) or
 when the condition becomes false (with while),
but not when the loop is teminated by a break statement.
'''

#Break statement 
for n in range(2, 10): #equivalent of...for n in [2,3,4,5,6,7,8,9]:
    for x in range(2, n): #first loop is for x in range(2, 2):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    #the else runs when no break clause occurs
    else:
        print(n, 'is a prime number')


#Continue statement
for num in range(2, 10): #equivalent of... for n in [2,3,4,5,6,7,8,9]:
    if num % 2 == 0: 
        print("Found an even number", num)
        continue #Will continue with the next loop
    print("Found an odd number", num)

#Pass statement
class MyPassClass:
    pass

def my_pass_def(*args):
    pass #Needs looking at


# (1:55:14) Modules
#see modules.py 

# (2:00:57) Errors and exceptions


# (2:07:37) Classes


# (2:27:26) Virtual environments


# (2:36:02) Building a project


print('freecodecamp intermediate tutorial')
# (0:00:56) Lists


# (0:16:30) Tuples


# (0:29:49) Dictionaries


# (0:42:40) Sets


# (0:58:44) Strings


# (1:22:50) Collections


# (1:36:43) Itertools


# (1:51:50) Lambda Functions


# (2:04:03) Exceptions and Errors


# (2:20:10) Logging


# (2:42:20) JSON


# (2:59:42) Random Numbers


# (3:14:23) Decorators


# (3:35:32) Generators


# (3:53:29) Threading vs Multiprocessing


# (4:07:59) Multithreading


# (4:31:05) Multiprocessing


# (4:53:26) Function Arguments


# (5:17:28) The Asterisk (*) Operator


# (5:30:19) Shallow vs Deep Copying


# (5:40:07) Context Managers

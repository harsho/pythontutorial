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

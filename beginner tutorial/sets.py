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
difference_update() removes the items in this set that are also included in another, specified set
discard() remove the specified item
intersection() returns a set that is the intersection of two or more sets
intersection_upate() Removes the items in this set that are not present in other, specified set(s)
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

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




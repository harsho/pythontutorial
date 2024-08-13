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

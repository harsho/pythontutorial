'''
New in python 3.10

Structural pattern matching has been added in the form of a match 
statement and case statements of patterns with associated actions.
Patterns consist of sequences, mappings, primitive data types as 
well as class instances. Pattern matching enables programs to extract
information from complex data types, branch on the structure of data,
and apply specific actions based on the different forms of data.

A match statement takes an expression and compares its value to succesive patterns given as one or more case blocks.


'''

#basics
def http_error(status):
    match status:
        case 400: 
            return "Bad request"
        case 404:
            return "not found"
        case 418:
            return "I'm a teapot"
        case _: 
            return "something's wrong with the internet"

def http_error(status):
    match status:
        case 400 | 401 | 403 | 404:
            return "Not allowed"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

#Patterns can look like unpacking assignments, and can be used to bind variables:
# point is an (x,y) tuple
def http_error(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"x={x}") 
        case (x, y):
            print(f"x={x}, Y={y}")
        case _:
            raise ValueError("Not a point")      

point_tuple = (0,0)
point_tuple = (0,123)
point_tuple = (123,0)
point_tuple = (123,456)
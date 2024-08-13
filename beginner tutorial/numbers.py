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


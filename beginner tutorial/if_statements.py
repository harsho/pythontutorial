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

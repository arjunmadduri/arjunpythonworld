#import math is the library we will be using just in case we need any built in functions to help us with our final result
import math
#this is the function that we'll be using to give our final output
def power_recursion(x,y):
#this is the if condition we'll be using to say that if our input is equal to 0 we will turn it in to 1 because if it is zero it will always give us 0 as our result 
    if y == 0:
        return 1
#here were saying that if our input is anything other than one save this formula that multiply's our variable of x by the function itself recalling it and subtracting one of y every time this happens 
    else:
        return x*power_recursion(x,y-1)

#these are our inputs we'll be using to call in the function and also for an input
x = int(input("Enter the number of x:::"))
y = int(input("Enter the power:::"))
#this is where we print our final ouput in a standard format
print ("The power of x is", power_recursion(x,y))
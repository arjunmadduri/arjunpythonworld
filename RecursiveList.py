#this is our math library that we'll be adding just in case we need any built in functions from this particular library
import math
#this is our function that we will store our final result in
def addition_of_list(list):
#this is the if condition saying that if our list has no value return the number 0
    if not list:        
        return 0
#this is our else condition saying that if our list has somesort of value we save this formula that is saying that our list starts at 0 adding every number above it and storing it in the function
    else:
        return list[0]+addition_of_list(list[1:])
#this is our list we will be using to get an answer of how much the total value is of all the numbers inside it
list = [1,2,3,4,5,6,7,8,9,10,11]
#this is our final result when we are calling the formula from our function and giving our final result and caling the variable that is stored inside of our function
print (addition_of_list(list))
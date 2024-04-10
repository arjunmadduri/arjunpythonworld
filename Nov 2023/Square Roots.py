#import function for math
import math 
#variables for problem
number = int(input("Enter a number please:"))
#variable determines square root
a = math.sqrt(number)
#if condition for problem in the code and variables to help for the proccess
if a.is_integer:
#print statement for if condition
    print("this is a perfect square number")
#else condition
else:
#print statement for else condition
    print("invalid.please try again")
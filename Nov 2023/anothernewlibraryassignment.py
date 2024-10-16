# Instructions

# Nidhi wants to make her custom random module with the name myRandom(). She wants to make the following functions:
# evenChoice() --> Selects a random even number from a given list.

# oddChoice() --> Selects a random odd number from a given list.

# primeChoice() --> Selects a prime number from a given list.

# Create a similar module to help Nidhi.

import math
import random

Choices = int(input("Enter a number::: "))

def evenchoices(Choices):
    if Choices %2 ==0:
        result = "The first number you entered is a even number, good job!"
        print (result)
    elif Choices:
        result1 = "The first number you entered is not a even number, sorry!"
        print (result1)
            
Choices1 = int(input("Enter another number::: "))

def oddchoice(Choices1):
    if Choices1 %2 !=0:
        result2 = "The second number you entered is a odd number, good job!"
        print (result2)
    elif Choices1:
        result3 = "The second number you entered is not a odd number, sorry!"
        print (result3)
    
Choices2 = int(input("Enter your final number::: "))

def primechoice(Choices2):
    non_prime = 0
    for i in range(2,Choices2):
        if Choices2 %i==0:
            non_prime = 1
            break
    if non_prime == 0:
        result4 = "The third number you have entered is a prime number, great job!"
        print (result4)
    else:
        result5 = "The third number you ahve entered is not a prime number, sorry!"
        print(result5)
evenchoices(Choices)
oddchoice(Choices1)
primechoice(Choices2) 

#area of circle perimeter of circle diameter of circle
#user input radius
#user input another one for shape
#in
#def function
#diameter = radius x 2
#2 x pi x radius
#pi x radius / radius

import math

def diameter(number,n):
    if n == "square":
        print("Square will not be using diameter")
    elif n == "circle":
        result = number*2
        print ("The diameter for this circle is:", result)
def area(number,n):
    if n == "square":
        result = number*number
        print ("The area for this square is:", result)
    elif n == "circle":
        result = 2*math.pi*number
        print ("The area for this circle is:", result)
def perimeter(number,n):
    if n == "square":
        result = number*4
        print ("The perimeter of this square is:", result)
    elif n == "circle":
        result = math.pi*number*number
        print ("The perimeter for this circle is:", result)


number = int(input("Enter A Number for Calculation:"))
n = str(input("Choose which shape: circle or square:"))
n = n.lower()
if n == "square" or n == "circle":
    diameter(number,n)
    area(number,n)
    perimeter(number,n)
else:
    print ("Please Enter Valid Shape Either Square or Circle")
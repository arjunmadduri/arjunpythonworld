
# Shubham wants to create a car racing game. But he is not aware of object-oriented programming.
# Using the concept of OOP, show him how we can create a class of the car.
#  With parameters(brand, color, weight, height, and length) also add methods for start, stop, increase speed, decrease speed, 
#  turn on headlights, and turn off headlights. 
# Also, create different objects(cars) using the class car.

class shape:
    def __init__(self,l,w,h):
        self.length = l
        self.width = w
        self.height = h
    def car_values(length,width,height):
        length = int(input("Enter the length of your car::: "))
        if length <= 1:
            print("SUCCESS!, LENGTH ADDED TO YOUR CAR")
        else:
            print("NOT SUCCESSFUL!, LENGTH COULD NOT BE ADDED TO YOUR CAR")
        width = int(input("Enter the width of your car::: "))
        if width <= 1:
            print("SUCCESS!, WIDTH ADDED TO YOUR CAR")
        else:
            print("NOT SUCCESSFUL, WIDTH COULD NOT BE ADDED TO YOUR CAR")
        height = int(input("Enter the height of your car::: "))
        if height <= 1:
            print("SUCCESS, HEIGHT ADDED TO YOUR CAR")
        else:
            print("NOT SUCCESFUL, HEIGHT COULD NOT BE ADDED TO YOUR CAR")
            
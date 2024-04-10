import math

def mathbasics(n):
    if n == 0:
        print("The Number Entered is Zero")
    else:
        a = math.sqrt(n)
        print(a)

n = int(input("Enter the Number You desire: "))
mathbasics(n)



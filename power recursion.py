import math

def power_recursion(x,y):
    if y == 0:
        #print("Intermediate result:", 1)
        return 1
    else:
        #temp = power_recursion(x, y-1)
        #result =  x * temp
        #print(result)
        return x*power_recursion(x,y-1)


x = int(input("Enter the number of x:::"))
y = int(input("Enter the power:::"))
print ("The power of x is", power_recursion(x,y))
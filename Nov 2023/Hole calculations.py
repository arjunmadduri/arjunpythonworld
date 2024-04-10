import math
l = float(input("Enter the Length of the hole in Meters"))
b = float(input("Enter the Breadth of the hole in Meters"))
d = float(input("Enter the Depth of the hole in Meters"))
vol =  l*b*d 
water = vol*1000
weight = l*d
area = l*b
size = d*b
perceantage = area / size * 100
print (vol)
print (water)
print (weight)
print (area)
print (size)
print (perceantage)
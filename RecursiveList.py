import math

def addition_of_list(list):
    if not list:
        return 0
    else:
        return list[0]+addition_of_list(list[1:])

list = [1,2,3,4,5,6,7,8,9,10,11]
print (addition_of_list(list))
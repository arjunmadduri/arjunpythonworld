#User Inputs for numbers 
a = int(input("Give me a number:"))
b = int(input("Give me another number"))
#Nested loops and if conditions and else with break and g with i
for i in range (a,b+1):
    if i > 1:
        for g in range (2,i):
            if i % g  == 0:
                break
        else:
            print (i)
number = int(input("Enter a number to give factorial of:"))
if number <0:
    print ("Not possible")
elif number ==0:
    print ("1")
else:
    factorial = 1
    for i in range (1,number+1):
        factorial=factorial*i
    print (factorial)
    
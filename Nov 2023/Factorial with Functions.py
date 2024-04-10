def factorial(n):
    if n < 0:
        print ("Not possible")
    elif(n == 0):
        print ("1")
    else:
        f = 1
    for i in range (1,n+1):
        f=f*i
    print (f)
n = int(input("Enter a number"))
print (factorial(n))
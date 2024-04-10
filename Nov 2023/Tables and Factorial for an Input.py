def table(n):
    for i in range(1,11):
        result = n * i
        print(f"{n} * {i} = {result}")

def factorial(n):
    if n < 0:
        print ("Not possible")
    else:
        f = 1
    for i in range (1,n+1):
        f=f*i
    print (f)

n = int(input("Enter a number"))
factorial(n)
table(n)
def addition(n,i):
            result = n+i
            print (result)
def subtraction(n,i):
        if i > n:
            result = "negative result cannot be subtracted"
        else:
            result = n-i
        print (result)

def multiplication(n, i):
        result = n * i
        print(result)
def division(n,i):
        if i == 0:
            result = "invalid"
        else:
            result = n/i
        print(result)        

n = int(input("Enter a number: "))
i = int(input("Enter another number: "))
a = str(input("Enter the Operator +,-,*,/: "))

if a=="+":
        addition(n,i)
elif a=="-":
        subtraction(n,i)
elif a=="*":
        multiplication(n,i)
elif a=="/":
        division(n,i)
else:
        print("Wrong Operator. Please Restart the Program")

        
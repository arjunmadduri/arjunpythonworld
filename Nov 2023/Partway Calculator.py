def factorial(num):
    if num <0:
        print ("Not possible")
    elif num==0:
        print ("1")
    else:
        factorial = 1
    for i in range (1,num+1):
        factorial=factorial*i
    print ("The Factorial for the Given number is: ", factorial)

def multipilication(num):
    print("Table for the Number: ", num)
    for i in range(1,11):
        result = num * i
        print(num , "X", i, "=", result)
    
def oddnumbers(num):
    print ("The odd number for the given number for odd numbers is: ")
    for num in range(1,num):
        if num %2 !=0:
            print(num)


num = int(input("Enter the Number for the All Functions: "))
factorial(num)
multipilication(num)
oddnumbers(num)
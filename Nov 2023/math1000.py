#Declaration of Variables
num = int(input("Enter A Number:"))
total = 0 
a = 1
#First Block of Code that Gets executed if the Number is Greater than 0 and Less than 200
if num > 0 and num <= 200:
    while a <= num:
        total = total + a
        a = a + 1
    print (total)
#Second Block of Code that gets Executed if the Number is greater than 200 and less than 600
elif num > 200 and num <= 600:
    for num in range(200,num):
        if num % 2 != 0:
            print(num)
#Third block of Code that gets executed if number is Greater than 600 and Less than 1000
elif num > 600 and num <= 1000:
    for num in range(600,num):
        if num % 2 ==0:
            print (num)
#Fourth block of Code that Gets Executed if number is greater than 500
else:
    print ("Number Greater Than 1000. Unable To Calculate.")
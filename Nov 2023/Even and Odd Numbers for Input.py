number = int(input("Enter a number:"))
print("The Even Numbers are")
for number in range (1,number):
    if number %2 ==0:
        result = number
        print (number)
print("The Odd Numbers are: ")
for number in range (1,number):
    if number %2 !=0:
        result = number
        print (number)
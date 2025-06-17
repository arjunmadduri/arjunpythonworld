list = []
amount = int(input("Enter the number of numbers you want in the list::: "))
for i in range(amount):
    num = int(input("Please enter the number::: "))
    list.append(num)
print(list)
#linear searching starts
target = int(input("Please enter which number you want to search for?::: "))
found = 0
for i in list:
    if target == i:
        found=1
        break
if found == 1:
    print("Number has been found")
else:
    print("Number is not in list")
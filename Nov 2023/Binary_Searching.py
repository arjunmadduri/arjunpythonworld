#Binary Searching
#Step 1 - Creation of list:
list = []
amount = int(input("How many numbers do you want in the list::: "))
for i in range (amount):
    num = int(input("Enter a number one at a time::: "))
    list.append(num)
print("Unsorted list::: ",list)
#Step 2 = Sorting of list:
for i in range(amount):
    for j in range(amount-i-1):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
print("Sorted List::: ",list)
#Step 3 = Binary searching starts:
Beg = 0
End = amount-1
found = False
target = int(input("Enter a number to find out of the list"))
while True:
    mid =(Beg+End)//2
    if target > list[mid]:
        Beg = mid+1
    elif target < list[mid]:
        End = mid-1
    else:
        found = True
        break
if found == True:
    print("The number has been found::: ",target)
else:
    print("The number is not found please try again")
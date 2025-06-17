#Step 1 - Creating a dynamic list
list = []
amount = int(input("How many number you want to add to the list::: "))
#Step 2 - creating a loop to add the numbers to the list
for i in range(amount):
    num = int(input("Please enter your number one at a time::: "))
    list.append(num)
print("unsorted list", list)
#Step 3 - Creating the bubble sorting code
for i in range(amount):
    for j in range(amount-i-1):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
print(list)
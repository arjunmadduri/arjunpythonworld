list = []
amount = int(input("How many numbers you want to add to your list::: "))
for i in range(amount):
    num = int(input("Enter what number you want::: "))
    list.append(num)
print("unsorted list",list)
list2 = []
for i in range(amount):
    minimum = min(list)
    list2.append(minimum)
    list.remove(minimum)
print("sorted list",list2)
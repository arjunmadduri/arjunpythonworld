list1 = [2, 2, 3, 1, 1, 4]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list1)
print(list2)
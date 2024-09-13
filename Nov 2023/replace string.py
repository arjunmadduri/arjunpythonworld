user_input = input("Enter your sentence here::: ")
list1 = user_input.split()
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
final = ' '.join(list2)
print(final)
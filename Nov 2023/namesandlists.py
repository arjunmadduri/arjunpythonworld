user_input = int(input("How many names do you want to add to your list::: "))
yourlist = []
for i in range(user_input):
    names = (input(f"Enter what names you want to add to your list:::  {i+1}:"))
    yourlist.append(names)
print(yourlist)
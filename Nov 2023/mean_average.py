number_list = []
number_amount = int(input("Enter the amount of numbers you want to enter::: "))
for i in range(number_amount):
    number = int(input("Enter a number::: "))
    number_list.append(number)
print(number_list)
total = sum(number_list)
print(total)
average = total/number_amount
print(average)
import statistics
number = []
number_amount = int(input("Enter how many number do you want to enter::: "))
for i in range(number_amount):
    numbers = int(input("Enter a number::: "))
    number.append(numbers)
print(number)
mode = statistics.mode(number)
print(mode)
multimode = statistics.multimode(number)
print(multimode)
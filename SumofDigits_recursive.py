
def sum_of_digits_recursive(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digits_recursive(num // 10)

num = int(input("Enter a number:::"))

print ("The value of the all the digits combigned is", sum_of_digits_recursive(num))
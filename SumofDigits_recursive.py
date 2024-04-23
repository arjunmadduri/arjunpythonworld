#function for breaking down the digits in the number
def sum_of_digits_recursive(num):
#if our input is = to 0 return 0
    if num == 0:
        return 0
#if our input is not = to 0 use this formula to break down all the digits
    else:
        return (num % 10) + sum_of_digits_recursive(num // 10)
#our input for giving the number with multiple digits to calculate the value of all of them combigned
num = int(input("Enter a number:::"))
#printing our final answer/result
print ("The value of the all the digits combigned is", sum_of_digits_recursive(num))




''' 
num=123
123%10  ==3   123//10===12

12%10== 2    12//10==1

1%10==1       1//10==0


3+2+1

'''
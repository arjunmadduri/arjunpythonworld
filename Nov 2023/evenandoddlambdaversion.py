# User input is where you enter a number and it goes to the formula in the 4th line.
user_input = int(input("Enter a number::: "))
# This is the formula which uses the anonymous function sldo known as the lambda function which is usually used for mathmetics when using python, now it says if our user's input  is dividable by 2 and has no remainder it will be a defined as an even number and if it's anything else it will be defined as an odd number.
calc = lambda user_input: "Even number" if user_input % 2 == 0 else "Odd number"
# This is where our user's input is getting calculated by our formula to see if it is a even or odd number and then prints the result saying if our user's input is an even or odd number.
print(calc(user_input))
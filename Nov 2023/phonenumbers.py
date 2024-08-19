#take a phone number from the user and print it is valid if 

#1- must starts with 9 or 8 or 7-
#2- must have 10 digits-len
#3- all the characters must be numbers-isnumeric

user_input = (input("Enter your phone number::: "))
if user_input.isnumeric() and len(user_input) == 10 and (user_input[0] == "9" or user_input[0] == "8" or user_input[0] == "7"):
    print("This is a valid phone number")
else:
    print("This is an invalid phone number")
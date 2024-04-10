#take username and password using input()

#check for digits in the password using hint1

#ask the user not to use any numbers if there is any number in the password and accept the password again

#once the password is accepted that matches the criteria then show that the password is verified and print welcome to dashboard.
message = ''
messale_ls = []

username = str(input("Enter User Name: "))

while True:
    password = input("Please enter your password: ")
    if  password.isnumeric():
        message = "password weak – contains only numbers"    
    elif password.isalpha():
        message = "password strong"
    messale_ls.append(message)
    print(message)
    if message == "password strong":
         break

#create a variable named total_candies_to_load and take the input from the user on how many candies to be loaded on to the vending machine

#print the vending machine title as "🍬🍬Candy Vending Machine🍬🍬" and  print total number of candies loaded into the vending machine along with it.

#create a variable named numberOfCandiesUserWants to store the number of  candies required by the user

#accept the number of candies the customer wants as an input into the variable numberOfCandiesUserWants that we created in the previous step and if the number of candies required by the customer is less than zero or greater than total number of candies in the machine, print “You have entered number of candies which is either zero or less than zero and is not possible to disperse please try again or visit once again Thanks for shopping with us!!! we will be happy to serve you once again”

#Using the concept of nested loops, print the amount the customer has to pay given cost of 1 candy = 1$.

 #Confirm the money  paid by the customer as input to UserMoney variable.

#If the UserMoney is equal to cost of candies, print delivering as many times as the number of candies ordered by the customer otherwise print “Enter wrong amount. Try again !”

#print the number of candies left in the vending machine and a thank you message.

total_candies_to_load = int(input("How many candies do you want to load into the vending machine::: "))
print("🍬🍬Candy Vending Machine🍬🍬")
number_of_candies_user_wants = int(input("Enter the number of candies you want::: "))

if number_of_candies_user_wants == 0 or number_of_candies_user_wants > total_candies_to_load:
    print("The number you entered in the total number of candies you wanted is less than the number of candies you loaded onto the vending machine. Please Try Again!:::")

else:
    print("you may move on:::")

candyprice = 1
print(candyprice)
total_candy_price = number_of_candies_user_wants*candyprice
print(total_candy_price)
print("This is the price you need to pay for the candies",total_candy_price)
user_money_paid = int(input("Enter the amount of money you need to get the candy you wanted::: "))

if user_money_paid != total_candy_price:
    print("This is not the price needed to pay for the candies you wanted please try again:::")
else:
    print("You may continue to checkout:::")

candies = ("🍬")
number_of_candies_left = total_candies_to_load-number_of_candies_user_wants
print(number_of_candies_left)
candies_given_to_user = print(total_candy_price*candies)
print(candies_given_to_user)
recipt = input("Do you want a recipt please enter::: ").lower()
if recipt == "yes":
    print("The total amount of candies you loaded was::: ",total_candies_to_load)
    print("The total candies you wanted was::: ",number_of_candies_user_wants)
    print("The price of each candy was::: ",candyprice)
    print("The total price for all the candies you wanted was::: ",total_candy_price)
    print("the total money you paid for all the candy was::: ",user_money_paid)
    print("The candies you got were:::",candies_given_to_user)
else:
    print("Okay thank you for shopping at Arjun's Candy Machine, Bye! Bye!::: ")
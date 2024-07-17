# homework 1
# Himanshu sells notebooks. Sometimes it becomes a bit difficult for him to calculate the total amount to charge from the customer. To help Himanshu create a program that asks the user to enter the number of books to buy and then print the amount to be paid.


def books(book_cost,book_input):
    if book_input <= 0:
        print("Invalid input please retry")
    elif book_input >= 1:
        result = book_input*book_cost
        print(result, " Dollars")

book_cost = 3.00
book_input = int(input("Enter the amount of books you want to buy::: "))

books(book_cost,book_input)
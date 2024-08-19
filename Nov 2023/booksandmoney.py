# homework 1
# Himanshu sells notebooks. Sometimes it becomes a bit difficult for him to calculate the total amount to charge from the customer. To help Himanshu create a program that asks the user to enter the number of books to buy and then print the amount to be paid.


TaxCode = {
     "TX":6,
     "OR":0,
     "WA":10,
     "CA":6
}



def books(book_cost,book_input,taxrate):
    if book_input <= 0:
        print("Invalid input please retry")
    elif book_cost >= 15.00 or book_cost <= 3.00:
        print("Invlaid input please retry") 
    elif book_input >= 1:
        result = book_input*book_cost
        price = result+(result*taxrate/100)
        print(price, " Dollars")

book_cost = int(input("Enter the amount your book is from 3.00$-15.00$"))
book_input = int(input("Enter the amount of books you want to buy::: "))
Statecode = (input("Enter State Code from these Choices - OR,WA,CA,TX:"))
taxrate = TaxCode[Statecode]

books(book_cost,book_input,taxrate)
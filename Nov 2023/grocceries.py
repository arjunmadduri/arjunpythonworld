# create a grocery dictionary in that ask what u want to buy and price and print total bill

grocceryitem ={

}

while True:
    choice = int(input("Press 1 for adding an item, press 2 for exit::: "))
    if choice == 1:
        item = input("Enter the item you want to add::: ")
        quantity = int(input("Enter the amount of the item you wanted to add::: "))
        price = int(input("What is the price of your item"))
        totalprice = quantity*price
        grocceryitem[item]=totalprice
    else:
        break
print(sum(grocceryitem.values()))
print(grocceryitem)
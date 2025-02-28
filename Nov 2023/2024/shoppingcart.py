Shoppingcart = {}
cart_items = int(input("Enter the amount of items you want in the cart::: "))
for i in range(cart_items):
    item_name = str(input("Enter the item you want::: ")).lower()
    quantity = int(input(f"How much quantity of this item {item_name}::: "))
    Shoppingcart[item_name] = quantity
print(Shoppingcart)
total_quantity = sum(Shoppingcart.values())
print("total quantity::: ", total_quantity)
choice = input("would you like to remove something:::").lower()
if choice == "yes":
    item_remove = input("please enter item you want to remove::: ").lower()
    Shoppingcart.pop(item_remove)
    print("Thank you for shopping at the PANEER STORE, here is your shopping cart with what you have took out::: ", Shoppingcart) 
elif choice == "no":
    print("Thank you for shopping at the PANEER STORE, here is your shopping cart with what you have took out::: ", Shoppingcart) 
else:
    print("Error please retry")
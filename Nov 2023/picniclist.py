#Inputs for how many people are coming with you and how many items each person is bringing 
people = int(input("How many people are coming in your group including you::: "))
items = int(input("How many items is each person bringing in your group::: "))
#The list where we will store the result for this program
picniclist = []
#for loop for the amount of people coming and to represent the first person second person etc... while asking what items they are bringing
for i in range(people):
    print (f"person {i+1}")
#second for loop/nested loops this time it is for the items that the people are bringing
    for j in range(items):
#"moreitems" is the variable that we will ask what items they are bringing so that after they are done entering what each person is bringing they can go to our result list which is "picniclist"      
        moreitems = (input(f"Enter what are the items that you are bringing:::  {j+1}:"))
#this is where we append all the inputs from "moreitems" from each person that is coming with you including yourselves, which is all going to go into the list called "picniclist"
        picniclist.append(moreitems)
#remove_items is the variable where you get to answer if you want to remove anything every time you enter something in the variable called "moreitems"
remove_items = input("Do you want to remove any items from the list? (yes/no): ").strip().lower()
#this is the if condition that says if you say yes in the input from the variable such as "remove_items" a while loop will be triggered and make you say which item you want to remove if the input from "item_to_remove" that you have enetered is done it will end the code without printing our result list which is known as "picniclist"
if remove_items == 'yes':
    while True:
        item_to_remove = input("Enter the item you want to remove (or type 'done' to finish): ").strip()
        if item_to_remove == 'done':
            break
#this is saying that the variable "item_to_remove"'s input will be removed from "picniclist"
        if item_to_remove in picniclist:
            picniclist.remove(item_to_remove)
            print(f"Removed {item_to_remove} from the list.")
        else:
            print(f"Item {item_to_remove} not found in the list.")
#this is the last line of code where we print our final result which is known as "picniclist "
print(picniclist)
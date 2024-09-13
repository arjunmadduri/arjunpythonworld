#this is our list where we have our numbers stored
numbers = [4, 4, 3, 3, 2, 2,]
#this is where we convert our list into a set
unique_numbers = set(numbers)
#here is where we convert it back but with the effects of our previous variable in the line above
unique_numbers_list = list(unique_numbers)
#these are the print statements for the previous list and the list with out duplicates also known as the one that was a set
print("Original list:", numbers)
print("List with duplicates removed:", unique_numbers_list)
#this is our list where we have our numbers stored 
numbers = [1, 2, 3, 2, 4, 5, 6, 1, 7, 8, 4]
#this is where we convert our list into a set
unique_numbers = set(numbers)
#here is where we convert it back but with the effects of our previous variable in the line above
unique_numbers_list = list(unique_numbers)
#these are the print statements for the previous list and the list with out duplicates also known as the one that was a set
print("Original list:", numbers)
print("List with duplicates removed:", unique_numbers_list)

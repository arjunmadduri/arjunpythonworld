# Instructions
# Ella, a passionate mathematician, is working on a project involving prime numbers. She needs to sort a list of prime numbers in ascending order to analyze their distribution and patterns. 
# Ella decides to use the merge sort algorithm for this task, known for its efficiency and stability. Can you assist Ella in writing a Python program to sort the list of prime numbers in ascending order?
# Hint:
# Define a function merge_sort that takes a list numbers as input.
# Check the base case: If the length of the list numbers is less than or equal to 1, return the list as it is already sorted.
# Split the list numbers into two halves: left and right.
# Recursively apply the merge_sort function to both halves.
# Merge the sorted left and right halves to obtain the final sorted list.
# Define a function merge that takes two sorted lists left and right as input and merges them into a single sorted list.
# Define a function is_prime to check if a number is prime.
# Generate a list of prime numbers and store them in the list prime_numbers.
# Call the merge_sort function with the list of prime numbers as input.
# Print the sorted list of prime numbers.


list1 = []

for i in range (1,1000):
    flag = 0
    for j in range (2,i):
        if i%j == 0:
            flag = 1   
            break
    if flag == 0:
        list1.append(i)
print(list1)
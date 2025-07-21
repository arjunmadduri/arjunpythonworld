# Nidhi is interested to know how many palindrome numbers are there in the first one thousand numbers. 
# Also, she wants to look at all the palindrome numbers in one place.
#  Write a python program that can create a list of all palindrome numbers in the first one thousand numbers
palindrome = []
number = 1000
for i in range(number):
    j = str(i)
    reverse_j = j[::-1]
    if reverse_j == j:
        palindrome.append(reverse_j)
    else:
        print("Not a palindrome")
print(palindrome)
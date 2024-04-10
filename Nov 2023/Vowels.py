#Variables for storage of input and value of how many vowels in the code
a = input(str("Can you give me a word?:"))
vowel = ["a","e","i","o","u","A","E","I","O","U"]
b = 0
#If statements and for program
for i in range (len(a)):
    if a[i] in vowel:
        b += 1
print ("The number of vowels is:",b)
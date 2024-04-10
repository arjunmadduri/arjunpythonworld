user_input = input('Enter the Text: ')
a = user_input.count('a')
e = user_input.count('e')
i = user_input.count('i')
o = user_input.count('o')
u = user_input.count('u')
spaces = user_input.count(' ')
l = len(user_input)
variable_count = a + e + i + u + o
total_count = len(user_input) - spaces
vowel_percantage = variable_count / total_count * 100
print('The Input entered by user is : ' +user_input)
print('The length including Spaces is: ', l)
print('The amount of total number of spaces is: ', spaces)
print('The total Vowels count is :', variable_count)
print('The Length of Sentence without Spaces is : ', total_count)
print('The Percentage of Vowels in the Sentence is :', vowel_percantage)

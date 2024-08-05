#def functioin for the code
def wordremoverrepetition(user_input):
#using with open to open the user input and put it in read and more mode    
    with open(user_input, 'r+') as f:
#variable for opening user input which is stored as f
        opening = f.read()
#variable for spliting all words
        words = opening.split()
#array for storing answer        
        result = []
#for loop for saying that a word that is not inside of words the variable do... "next line says about this"        
        for word in words:
#if the word is not in the array do... "says in next line"
            if word not in result:
#the result which is the array appends the word that wasn't in there before        
                result.append(word)
# f.seek means going to the start of the line and end        
        f.seek(0)
# then f.truncate erases everything
        f.truncate()
# then finally f.write newly refreshes it with the updates that we wanted
        f.write(" ".join(result))
#userinput for which file we are using
user_input = str(input("Enter a file to revise and edit:::"))
#calling function to print and successfully use
wordremoverrepetition(user_input)
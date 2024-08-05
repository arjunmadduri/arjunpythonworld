#try statement to say for files instead of if
try:
#user input
    users = str(input("Enter a file:"))
#variable for opening the file and putting it in read mode    
    Filing = open(users, "r")
#printint the variable to open the file and confirming it is in read mode    
    print(Filing.read())
#closing the file
    Filing.close()
#except instead of else, FileNotFoundError used for saying that if file does not exist    
except FileNotFoundError:
#saying that if file does not exist print this:::
    print("Filenotfound")
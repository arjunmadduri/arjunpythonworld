#Function for adding a entry to the text file
def addentry():
#Variable for entering the text you want to add to the file    
    addingentries = str(input("Enter the data you wnat to store in your notepad diary that will be saved automatically::: "))
#opening thetext file your adding it to
    with open("diary.txt", "a") as file:
#Making a way that it makes a new line for each thing you say on the variable above
        file.write(addingentries + "\n")
#Printing task is complete to make sure your work is done and a reminder to check your file
    print("Task is complete you can check to make sure.")
#Function for reading what you have in the file
def readentry():
#Try and catch statements way
    try:
#With open to open the text file or any file and store it into file a new variable we created in this function        
        with open("diary.txt", "r") as file:
#This makes a variable for opening the tect file or any file which is stored or known as a variable called file and what it does here is that it reads all the lines in the format            
            entries = file.readlines()
#Now were making the variable on the 18th liine into entry
        for entry in entries:
#And here were striping the variable entry
            print(entry.strip())
#Catch or except part for the filenotfounderror
    except FileNotFoundError:
#Printing the output if the except happens        
        print("No entries or text found in the file")
#This print is to print the information in the for loop
    print()

#This is the main function
def main():
#While looop for making sure is True
    while True:
#The three choices for your input
        print("Welcome to your diary")
        print("1. Add a new entry")
        print("2. Read all entries")
        print("3. Exit")
#Your input for one of the choices
        choice = input("Enter one of the numbers above to represent your choice::: ")
#If condition for when this number is called call this function or print this sentence
        if choice == "1":
            addentry()
        elif choice == "2":
            readentry()
        elif choice == "3":
            print("Code is shutting down. Bye Bye.")
#Break for the whole code            
            break
#Else for saying that your choice is invalid        
        else:
            print("Invalid Choice")



#Here it is finally saying that if the name is main then print or call the main function itself
if __name__ == "__main__":
    main()





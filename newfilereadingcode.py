#creating a function
def Filecaller(file):
#try instead of if since this is file handling    
    try:
#creating another variable to open the file and put into read mode
        File = open(file,"r")
# saying that for each line in the file that we called
        for line in File:
#saying that if any charcter has a digit in any line we will call that specific line
            if any(char.isdigit() for char in line):
#saying that print thatline with a numerical value in it just like the line above decribed
                print(line.strip())        
#saying except instead of else for file handling for this error just print this because this doesn't exist
    except FileNotFoundError:
#print this for that above line 
        print("File does not exist")
        
#input from user
file = str(input("Enter a file:"))
#printing function
Filecaller(file)
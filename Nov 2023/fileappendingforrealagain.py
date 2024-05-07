def fileappending(files,oldword,newword):
    try:
        with open(files,"r") as file:   
            filecontent = file.read()
        
        newcontent = filecontent.replace(oldword,newword)
        with open(files,"w") as file:
            file.write(newcontent)
    except FileNotFoundError:
        print ("This file does not exist please ")


files = str(input("Which file or text file do you want to edit this grammar:::"))
oldword = str(input("Type in the wrong spelling of the word you choose in this file:::"))
newword = str(input("Enter the correct spelling of the word above:::"))
fileappending(files,oldword,newword)
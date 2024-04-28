def Filecaller(file):
    try:
        File = open(file,"r")
        #print (File.read())
        for line in File:
            if any(char.isdigit() for char in line):
                print(line.strip())        
        #print("Lines in File",a)
    except FileNotFoundError:
        print("File does not exist")
        

file = str(input("Enter a file:"))
Filecaller(file)
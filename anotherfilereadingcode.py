def Serialnumber(file):
        Lines = []
        File = open(file,"r")
        i = 1
        for line in File:
                Lines.append(f"{i}:{line.strip()}")
                i=i+1
        File.close()
        return Lines
    

file = str(input("Enter a file:::"))
try:
        numberedlines = Serialnumber(file)
        for line in numberedlines:
                print (line)
except FileNotFoundError:
        print ("Invalid file, this file does not exist::")
print(Serialnumber(file))
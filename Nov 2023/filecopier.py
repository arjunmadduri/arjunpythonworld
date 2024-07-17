#function for code and process
def copyfile(source, destination):
#Try and catch functions to make sure file exist and for code to be in    
    try:
#
        with open (source, "r") as file:
            contents = file.read()
        with open (destination, "w") as file:
            file.write(contents)
        print ("your file has been copied sucessfully")
    except FileNotFoundError:
        print ("File is not found")
    except Exception as excepted:
        print("An error occurred:", excepted)

source = str(input("Enter the file path that you want to copy into another file::: "))
destination = str(input("Enter the Destination Path:"))
copyfile(source, destination)
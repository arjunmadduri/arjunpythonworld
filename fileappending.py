def adding_appending_the_file(files):
    try:
        with open (files,'r') as file:
            contents = file.read()
        
        contents = contents.replace('. ','.\n')
        print(contents)
    except FileNotFoundError:
        print ("FileNotFoundError")

"""with open(files,'w') as file:
            file.write(contents)
            file.close()
        
        with open (files,'r') as file:
            print(file.read())
            file.close()"""

files = str(input("Enter a file please to edit and create:::"))
adding_appending_the_file(files)
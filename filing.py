try:
    user_input = str(input("Enter a file name:::"))
    Filed = open(user_input,"w")
    print (Filed.write("my name is hello"))
    Filed.close
except FileNotFoundError:
    print("File does not exist")
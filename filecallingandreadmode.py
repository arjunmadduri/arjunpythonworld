try:
    users = str(input("Enter a file:"))
    Filing = open(users, "r")
    print(Filing.read())
    Filing.close()
    
except FileNotFoundError:
    print("Filenotfound")
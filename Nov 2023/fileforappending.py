def addentry():
    addingentries = str(input("Enter the data you wnat to store in your notepad diary that will be saved automatically::: "))
    with open("diary.txt", "a") as file:
        file.write(addingentries + "\n")
        
    print("Task is complete you can check to make sure.")

def readentry():
    try:
        with open("diary.txt", "r") as file:
            entries = file.readlines()
        for entry in entries:
            print(entry.strip())
    except FileNotFoundError:
        print("No entries or text found in the file")
    print()


def main():
    while True:
        print("Welcome to your diary")
        print("1. Add a new entry")
        print("2. Read all entries")
        print("3. Exit")
        choice = input("Enter one of the numbers above to represent your choice::: ")
        if choice == "1":
            addentry()
        elif choice == "2":
            readentry()
        elif choice == "3":
            print("Code is shutting down. Bye Bye.")
            break
        else:
            print("Invalid Choice")




if __name__ == "__main__":
    main()





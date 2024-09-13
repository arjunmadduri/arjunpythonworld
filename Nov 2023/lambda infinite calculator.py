
additions = lambda number,numbers:number+numbers
subtractions = lambda number,numbers:number-numbers
multiplications = lambda number,numbers:number*numbers
divisions = lambda number,numbers:number/numbers
while True: 
    number = int(input("Enter the number you want to use first::: "))
    numbers = int(input("Enter the number you want to use second::: "))
    operation = str(input("Enter the operation you want to use for these to numbers::: ")).lower()

    if operation == "addition":
        print(additions(number,numbers))
    if operation == "subtraction":
        print(subtractions(number,numbers))
    if operation == "multipilication":
        print(multiplications(number,numbers))
    if operation == "division":
        print(divisions(number,numbers))
    else:
        print("")

    # Ask the user if they want to repeat or quit
        choice = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if choice == 'no':
            print("Exiting the application. Goodbye!")
            break
        elif choice != 'yes':
            print("Invalid choice. Exiting the application.")
            break


age = int(input("Enter your age::: "))
if age >= 1 and age <= 3:
    print("You are a baby")
elif age >= 4 and age <= 6:
    print("You are a kid")
elif age >= 7 and age <= 9:
    print("You are a child")
elif age >= 10 and age <= 12:
    print("You are a tween")
elif age >= 13 and age <= 19:
    print("You are a teenager")
elif age >= 20 and age <= 28:
    print("You are a Young Citizen")
elif age >= 29 and age <= 50:
    print("You are a Adult")
elif age >= 51 and age <= 100:
    print("You are a Grandparent")
else:
    print("You are really old :::)")
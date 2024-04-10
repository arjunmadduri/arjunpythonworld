age = int(input("Enter your age::"))
gender = str(input("Enter your gender::"))
if age >= 55 and gender == "female".lower() or age >=60 and gender == "male".lower():
    print ("Your retired")
else:
    print ("Not retired")

income = float(input("What is your annual income in lakhs?.:"))
if income <= 2.5:
    print ("0%")
elif income > 2.5 and income <= 5:
    print ("5%")
elif income > 5 and income <= 7.5:
    print ("10%")
elif income > 7.5 and income <= 10:
    print ("15%")
elif income > 10 and income <= 12.5:
    print ("20%")
elif income > 12.5 and income <= 15:
    print ("25%")
elif income > 15:
    print ("30%")
jet = int(input("Enter a number between 1-100:"))
if jet <= 100:
    for jet in range(0,jet):
        if jet % 2 ==0:
            print (jet)
else:
    print ("PLease enter a number between 1-100")

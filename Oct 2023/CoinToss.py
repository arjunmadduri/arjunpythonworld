import random
coin = ["Heads","Tails"]
userchoice = str(input("Choose Heads or Tails:"))
toss= random.choice(coin)
if userchoice == toss:
    print("You won the toss and its", toss)
else:
    print("You lost the toss", toss)
print(toss)
import random 
gaming = ["Rock","Paper","Scissors"]
computer = random.choice(gaming)
games = int(input("1 = rock, 2 = paper, 3 = scissors, choose one: "))
print ("The computer chose:", computer)
while True:
    if games == 1 and computer == "Rock":    
        print ("Draw")
    elif games == 2 and computer == "Paper":
        print ("Draw")
    elif games == 3 and computer == "Scissors":
        print ("Draw")
    elif games == 1 and computer == "Paper":
        print ("Computer wins")
    elif games == 1 and computer == "Scissors":
        print ("Games wins")
    elif games == 2 and computer == "Rock":
        print ("Games wins")
    elif games == 2 and computer == "Scissors":
        print ("Computer wins")
    elif games == 3 and computer == "Rock":
        print ("Computer wins")
    elif games == 3 and computer == "Paper":
        print ("Games wins")
    asking = str(input("Do you want to play again, Yes No: "))
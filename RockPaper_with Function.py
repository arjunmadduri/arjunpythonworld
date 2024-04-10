import random

def get_user_choice():
    while True:
        user_choice = input("Enter your Choice (Rock, Paper, Scissor): ").lower()
        if user_choice in ['rock', 'paper', 'scissor']:
            return user_choice
        else:
            print ("Invalid choice please retry")

def computers_choice():
    computer_choice = random.choice(['rock', 'paper', 'scissor'])
    return computer_choice

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice =="rock" and  computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        return "You win"
    else:
        return "Computer wins"

def playgame():
    while True:
        print ("Welcome to rock, paper, scissor")
        user_choice = get_user_choice()
        computer_choice = computers_choice()
        print ("Your choice is:::", user_choice )
        print ("The computer chose:::", computer_choice)
        print (winner(user_choice, computer_choice))
        repeat = input("Do you want to play again(Yes,No):::").lower()
        if repeat != "yes":
            print ("Thank you for playing")
            break

playgame()
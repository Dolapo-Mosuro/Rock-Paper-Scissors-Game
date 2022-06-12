import random
    
while True:
    user_select= input("Pick an option- 'rock' 'paper' 'scissors'?: \n")
    game= ["rock","paper","scissors"]
    computer_select = random.choice(game)


    if user_select == computer_select:
            print("You selected: " + user_select)
            print("Computer selected: " +  computer_select)
            print("Tie!")

    elif user_select == "rock":
            if  computer_select == "scissors":
                print("You selected: " + user_select)
                print("Computer selected: " +  computer_select)
                print("You lose!")

            if computer_select == "paper":
                print("You selected: " +user_select)
                print("Computer selected: " +  computer_select)
                print("You win!")

    elif user_select == "scissors":
            if  computer_select == "rock":
                print("You selected: " +user_select)
                print("Computer selected: " +  computer_select)
                print("You lose!")

            if  computer_select == "paper":
                print("You selected: " + user_select)
                print("Computer: " +  computer_select )
                print("You win!")
    elif user_select == "paper":
            if computer_select == "scissors":
                print("You selected: " + user_select)
                print("Computer selected: " +computer_select)
                print("You lose!")

            if computer_select== "rock":
                print("You selected: " + user_select)
                print("Computer selected: " + computer_select)
                print("You win!")
   
    play_again = input("Play again? (y/n): \n")
    if play_again.lower() != "y":
        break

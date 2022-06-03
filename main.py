import random

while True:

    Game = ["rock","paper","scissors"]

    Player = None
    CPU = random.choice(Game)

    while Player not in Game:
            Player = input("Pick an option- 'r' 'p' 's'?: ").lower()

    if Player == CPU:
            print("You selected: " + Player)
            print("You selected: " +  CPU)
            print("Tie!")

    elif Player == "rock":
            if  CPU == "paper":
                print("You selected: " + Player)
                print("You selected: " +  CPU)
                print("You lose!")

            if CPU == "scissors":
                print("You selected: " +Player)
                print("You selected: " +  CPU)
                print("You win!")

    elif Player == "scissors":
            if  CPU == "rock":
                print("You selected: " + Player)
                print("You selected: " +  CPU)
                print("You lose!")

            if  CPU == "paper":
                print("You selected: " + Player)
                print("You selected: " +  CPU )
                print("You win!")
    elif Player == "paper":
            if CPU == "scissors":
                print("You selected: " + Player)
                print("You selected: " +)
                print("You lose!")

            if CPU == "rock":
                print("You selected: " + Player)
                print("You selected: " + CPU)
                print("You win!")

    replay = input("Play again? (yes/no): ").lower()
    if replay != "yes":
            break
    print(" That was fun. Goodbye.")


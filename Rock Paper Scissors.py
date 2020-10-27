from random import randint
print("Welcome to Rock Paper Scissors Game.")

# create list of play options
t = ["Rock", "Paper", "Scissors"]

# set player to False.
play = False

while play is False:

    # assign a Random play to the computer
    computer = t[randint(0, 2)]
    player_input = input("Choose Rock, Paper or Scissors: ")
    if player_input == computer:
        print("Draw")
    elif player_input == "Rock":
        if computer == "Paper":
            print("You Lose")
        else:
            print("You Win")
    elif player_input == "Paper":
        if computer == "Scissors":
            print("You Lose")
        else:
            print("You Win")
    elif player_input == "Scissors":
        if computer == "Rock":
            print("You Lose")
        else:
            print("You Win")
    elif player_input == "end":
        # end loop if user inputs end
        break
    else:
        print("Invalid input!")

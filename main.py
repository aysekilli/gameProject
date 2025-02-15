import random
options = ["rock" , "paper" , "scissors"]

def get_choices():
    player_choice = input("Please enter a choice (rock, paper, scissors) : ").lower()
    while player_choice not in options:
        player_choice = input("Invalid choice. Please enter a choice (rock, paper, scissors) : ")

    com_choice = random.choice(options)

    #f-string usage
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {com_choice}")

    return com_choice, player_choice


def check_win(player, com):
    if player == com:
        print("It is a tie.")
    elif player == "rock":
        if com == "scissors":
            print("You beat the computer!")
        else:
            print("Oh no, computer won :(")
    elif player == "paper":
        if com == "scissors":
            print("Oh no, computer won :(")
        else:
            print("You beat the computer!")
    else:
        if com == "rock":
            print("Oh no, computer won :(")
        else:
            print("You beat the computer!")
    return True


def play_again():
    while True:
        inpyesno = input("Do you want to play again? (y/n): ").lower()
        if inpyesno == "y":
            return main()
        elif inpyesno == "n":
            print("Bye!")
            return False
        else:
            print("Invalid choice. Please type 'y' for yes or 'n' for no.")


def main():
    player_choice, com_choices = get_choices()
    result = check_win(player_choice, com_choices)
    tryplay = play_again()

main()
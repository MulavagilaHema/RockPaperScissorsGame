import random
def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices
def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "its a tie!"
    elif player == "rock":
        if computer  == "paper":
            return "Paper covers rock! Computer wins!"
        else:
            return "rock smashes scissors! You win!"
    elif player == "paper":
        if computer  == "scissors":
            return "scissors cuts the paper! Computer wins!"
        else:
            return "Paper covers rock! You win!"
    elif player == "scissors":
        if computer  == "paper":
            return "scissors cut the paper! You win!"
        else:
            return "rock smashes scissors! Computer wins!"
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)


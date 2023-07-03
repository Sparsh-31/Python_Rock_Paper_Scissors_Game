import random


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif player_choice == "rock":
        if computer_choice == "paper":
            return "computer"
        else:
            return "player"
    elif player_choice == "paper":
        if computer_choice == "scissors":
            return "computer"
        else:
            return "player"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            return "computer"
        else:
            return "player"


# Initialize scores
player_score = 0
computer_score = 0
tie = 0
draws = 0

while True:
    player_choice = input(
        "Enter your choice (rock, paper, scissors) or 'q' to quit: ")

    # Handle quit option
    if player_choice.lower() == "q":
        break

    # Validate user input
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'q' to quit.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    winner = determine_winner(player_choice, computer_choice)

    # Update scores
    if winner == "player":
        player_score += 1
        draws += 1
    elif winner == "computer":
        computer_score += 1
        draws += 1
    else:
        tie += 1
        draws += 1

    print(f"\nPlayer's choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")

    if winner == "player":
        print("You win!")
    elif winner == "computer":
        print("Computer wins!")
    else:
        print("It's a tie!")

    # Display scores
    print(f"\n-------------------------------")
    print(f"Scores:")
    print("-------------------------------")
    print("Player | Computer | Tie | Draws")
    print("-------------------------------")
    print(f"{player_score}      | {computer_score}        | {tie}   | {draws}")
    print("-------------------------------")

# Game over
print("Thank you for playing!")
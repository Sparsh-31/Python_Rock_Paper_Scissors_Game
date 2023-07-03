import random


def play_game():
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    user_choice = user_choice.lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a draw!")
        return 'draw'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        print("You win!")
        return 'user'
    else:
        print("Computer wins!")
        return 'computer'



def main():
    user_score = 0
    computer_score = 0
    draw_count = 0

    while True:
        print("Rock, Paper, Scissors Game")
        print("----------------------------")

        result = play_game()

        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1
        else:
            draw_count += 1

        print("----------------------------")
        print("Score:")
        print(f"User: {user_score}")
        print(f"Computer: {computer_score}")
        print(f"Draws: {draw_count}")
        print("----------------------------")

        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() != 'yes':
            break

    print("Thank you for playing!")

if __name__ == '__main__':
    main()

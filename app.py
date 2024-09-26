import random

def get_computer_choice():
    """
    Randomly selects and returns one of the three choices: 'rock', 'paper', or 'scissors'.

    Returns:
        str: The computer's choice, which can be 'rock', 'paper', or 'scissors'.
    """
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    choice = input("Enter rock, paper, or scissors: ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter rock, paper, or scissors: ").strip().lower()
    return choice

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "win"
    else:
        return "lose"

def play_round():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("It's a tie!")
    return result

def play_game():
    wins = 0
    rounds = 0
    while True:
        result = play_round()
        rounds += 1
        if result == "win":
            wins += 1
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
    print(f"Game over! You won {wins} out of {rounds} rounds.")

if __name__ == "__main__":
    play_game()
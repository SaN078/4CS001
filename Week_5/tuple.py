import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def play_game():
    print("Welcome to the Dice Game!")

    rounds_played = 0
    wins = 0

    while True:
        # Get player's guess
        guess = input("Guess the total value of two dice rolls (2-12), or enter 'q' to quit: ")

        # Check if the player wants to quit
        if guess.lower() == 'q':
            break

        # Validate the guess
        try:
            guess = int(guess)
            if guess < 2 or guess > 12:
                print("Invalid guess. Please enter a number between 2 and 12.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

        # Roll the dice
        die1, die2 = roll_dice()
        total = die1 + die2

        # Display the result
        print(f"Rolled: {die1} + {die2} = {total}")

        # Check if the player's guess is correct
        if guess == total:
            print("Congratulations! You guessed correctly.")
            wins += 1

        rounds_played += 1

        # Display the number of rounds played and win percentage
        print(f"Rounds played: {rounds_played}")
        print(f"Win percentage: {wins / rounds_played * 100:.2f}%")

# Start the game
play_game()
import random

NUM_ROUNDS = 5  # Number of rounds to play

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0  # player's score

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate random numbers for the player and the computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        
        # Get the player's guess
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either 'higher' or 'lower': ").lower()
        
        # Determine the result of the round
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Increment the score for a correct guess
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
        print()  # Add a blank line to separate rounds

    # Conditional ending messages
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
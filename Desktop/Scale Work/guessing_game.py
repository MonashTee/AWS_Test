import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts =  0
    max_attempts = 3
    
    while True:
        guess = input("\nEnter your guess (between 1 and 10): ")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            continue

        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break

        if attempts == max_attempts:
            print(f"\nSorry, you've used up all your attempts. The number was {secret_number}. Better luck next time!")
            break

if __name__ == "__main__":
    guessing_game()

import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    attempts = 0
    while True:
        # Prompt the user to input their guess
        guess = input("Enter your guess: ")
        
        # Check if the input is a valid number
        if not guess.isdigit():
            print("Invalid input! Please enter a number between 1 and 100.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        # Compare the guess to the generated number
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {number} in {attempts} attempts.")
            break

# Run the game
guess_number()

import random

def number_guessing_game():
    secret_number = random.randint(1, 10)
    print("Guess number between 1 and 10.")
    
    attempts = 0
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break

import random

def number_guessing_game():
    secret_number = random.randint(1, 10)
    print("Guess number between 1 and 10.")
    
    attempts = 0
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break

number_guessing_game()
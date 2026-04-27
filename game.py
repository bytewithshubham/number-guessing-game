import random

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

target = random.randint(1, 10)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
        elif guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input! Enter a number.")

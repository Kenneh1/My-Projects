# Simple guessing game

secret_number = 20  # You can change this
guess = int(input("Guess the secret number (between 1 and 10): "))

if guess == secret_number:
    print("Congratulations! You guessed it right.")
else:
    print("Oops! Try again.")

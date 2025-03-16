# Number guessing game with multiple tries

secret_number = 5
guess = 0
while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))
    if guess != secret_number:
        print("Wrong! Try again.")
print("You got it!")

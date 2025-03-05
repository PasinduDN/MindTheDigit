import random

def guessTheNumber(x):
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'Guess a number between 1 and {x} : '))
        if guess < randomNumber:
            print("Too low. Guess again.")
        elif guess > randomNumber:
            print("Too high. Guess again.")
    print(f"Congrats. You guessed the number {randomNumber} correctly..!")
guessTheNumber(10)
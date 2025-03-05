import random
import pyfiglet
ascii_banner = pyfiglet.figlet_format("MindTheDigit", justify="center", width=100)

def guessTheNumber(x):
    print(ascii_banner)
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        try:
            guess = int(input(f'Guess a number between 1 and {x} : '))
            if guess < randomNumber:
                print("Too low. Guess again.")
            elif guess > randomNumber:
                print("Too high. Guess again.")
        except ValueError:
                print("Invalid input... Please enter a valid number.")
    print(f"Congrats. You guessed the number {randomNumber} correctly..!")
    
    while True:
        userChoice = input("Are you sure want to run this program again (Y/N) :").strip().upper() # .strip() for Remove starting ending spaces and .upper() use convert to upper case
        if (userChoice=="Y") :
            guessTheNumber(10)
        elif (userChoice=="N"):
            print("Thank You..!")
            break
        else :
            print("Invalid input...")
            
guessTheNumber(10)
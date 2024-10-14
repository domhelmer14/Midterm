import random

def guessing_game():
    number_to_guess = random.randint(1, 50)
    guess = None

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 50. Can you guess what it is?")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")

if __name__ == "__main__":
    guessing_game()
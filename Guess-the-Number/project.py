import random

def guess_game():
    target = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100 or type 'Q' to exit.")

    while True:
        user_input = input("\nEnter your guess or type 'Q' to exit: ")

        if user_input.lower() == "q":
            print("You exited the game. \n")
            break

        # Input validation
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number or type 'Q' to exit.")
            continue

        attempts += 1

        if guess == target:
            print(f"\n🎉 Congratulations! You guessed the target number {target} in {attempts} attempts!\n")
            break
        elif guess < target:
            print("Your guess is too low. Try a bigger number.")
        else:
            print("Your guess is too high. Try a smaller number.")

    print("\t -----GAME OVER----- \n")

if __name__ == "__main__":
    guess_game()

import random

emojis = { 'r': '🪨', 's': '✂️', 'p': '📃' }
choices = ('r','p','s')

while True:
    user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()

    if user_choice not in choices:
        print("Invalid input! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or \
        (user_choice == 's' and computer_choice == 'p') or \
        (user_choice == 'p' and computer_choice == 'r')):
        print("You win!")
    else:
        print("You lose!")

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break



# def play_rps():
#     options = ['rock', 'paper', 'scissors']
#     print("Welcome to Rock, Paper, Scissors!")
#     user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
#     computer_choice = random.choice(options)
    
#     if user_choice not in options:
#         print("Invalid input! Please choose rock, paper, or scissors.")
#         return

#     print(f"Computer chose: {computer_choice}")
    
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == 'rock' and computer_choice == 'scissors') or \
#          (user_choice == 'scissors' and computer_choice == 'paper') or \
#          (user_choice == 'paper' and computer_choice == 'rock'):
#         print("You win!")
#     else:
#         print("You lose!")
        

# if __name__ == "__main__":
#     play_rps()

import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃' }
choices = tuple(emojis.keys())

def get_user_choice():
  while True:
    user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
    if user_choice in choices:
      return user_choice      
    else:
      print('Invalid choice!')
      
def display_choices(user_choice, computer_choice):
  print(f'You chose {emojis[user_choice]}')
  print(f'Computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print('Tie!')
  elif (
    (user_choice == ROCK and computer_choice == SCISSORS) or 
    (user_choice == SCISSORS and computer_choice == PAPER) or 
    (user_choice == PAPER and computer_choice == ROCK)):
    print('You win')
  else:
    print('You lose')  

def play_game():
  while True:
    user_choice = get_user_choice()

    computer_choice = random.choice(choices)

    display_choices(user_choice, computer_choice)

    determine_winner(user_choice, computer_choice)

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
      break

play_game()

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

from random import randint

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print("Invalid choice!")
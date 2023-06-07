# Option 2: with asking to continue the game.
from random import randint
computer_guess = randint(1, 11)
# player_guess = None
while True:  # player_guess != computer_guess://it always will be true so we don't need to write it and the aboveline
    player_guess = int(input('Guess a number between 1 and 10: '))
    if player_guess < computer_guess:
        print('Too low, try again!')
    elif player_guess > computer_guess:
        print('Too high, try again!')
    else:
        print('You guessed it! You won!')
        play_again = input('Do you want to play again? (y/n) ').lower()
        if play_again == 'y':
            computer_guess = randint(1, 11)
            player_guess = None
        else:
            print('Thank you for playing!')
            break

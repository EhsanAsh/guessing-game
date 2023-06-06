from random import randint
computer_guess = randint(1, 11)
player_guess = None
while player_guess != computer_guess:
    player_guess = int(input('Guess a number between 1 and 10: '))
    if player_guess < computer_guess:
        print('Too low, try again!')
    elif player_guess > computer_guess:
        print('Too high, try again!')
    else:
        print('You guessed it! You won!')
print('Game over!')

# guess the number game
import random as rn
import sys
secret_number = rn.randint(1, 20)

#ask the user to play, binary
ask = input ('welcome to the official number_game, would you like to play? (y/n)')

#ask if yes
if ask.lower() == 'y':
    print('great, let\'s play')

else:
	print('ok, goodbye')
	sys.exit()

print('I\'m thinking of a number between 1 and 20...you have 6 guesses')

# ask the user to guess
for guesses in range(6):
	guess = int(input())

# if correct guess
	if guess < secret_number:
		print('Sorry, your guess is too low')
	elif guess > secret_number:
		print('Sorry your guess is too high')
	else: # if incorrect guess 
		print('Nailed it, but it took you ' + str(guesses) + ' guesses')
else:
	print('sorry you lose, the secret number is ' + str(secret_number))

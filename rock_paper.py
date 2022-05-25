#rock_paper
import random, sys

#score
wins = 0 
losses = 0
ties = 0 

while True: #game loop
	print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
	while True: #user input
		print('enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
		playerMove = input()
		if playerMove == 'q': 
			sys.exit() #quit program
		if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
			break
		print('Type r, p, s, or q')

	#display what player chooses
	if playerMove == 'r':
		print('rock vs. ')
	elif playerMove == 'p':
		print('paper vs. ')
	elif playerMove == 's':
		print('scissors vs.')

	#computer guess
	randnumber == random.randint(1, 3)
	if randnumber == 1:
		computerMove == 'r'
		print('rock')
	elif computerGuess == 2:
		computerMove == 'p'
		print('paper')
	elif computerGuess == 3:
		computerMove == 's'
		print('scissors')

	#record wins/losses
	if playerMove == computerMove: #if tie
		print('tie!')
		ties = ties + 1
	elif playerMove == 'r' and computerMove == 's': #player win
		print('player win')
		wins = wins + 1
	elif playerMove == 'p' and computerMove == 'r': #player win
		print('player win')
		wins = wins + 1
	elif playerMove == 's' and computerMove == 'p': #player win
		print('player win')
		wins = wins + 1
	elif playerMove == 'r' and computerMove == 'p': #computer win
		print('computer win')
		losses = losses + 1
	elif playerMove == 'p' and computerMove == 's': #computer win
		print('computer win')
		losses = losses + 1
	elif playerMove == 's' and computerMove == 'r': #computer win
		break







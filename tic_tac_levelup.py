# tic tac game leved up

board = [' ' for x in range(10)]

def insertBoard(letter, pos):
	global board
	board[pos] = letter


def spaceIsFree(pos):
	return board[pos] == ' '


def isWinner(bo, le):
	# returns true if a player has won
	# bo = board and le = letter (x or O)
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or #top row
	(bo[4] == le and bo[5] == le and bo[6] == le) or # middle row
	(bo[1] == le and bo[2] == le and bo[3] == le) or # bottom row
	(bo[1] == le and bo[4] == le and bo[7] == le) or # left column
	(bo[2] == le and bo[5] == le and bo[8] == le) or # middle colummn
	(bo[3] == le and bo[6] == le and bo[9] == le) or # right column
	(bo[1] == le and bo[5] == le and bo[9] == le) or # diagonal
	(bo[3] == le and bo[5] == le and bo[7] == le)) # diagonal

def playerMove():
	run = True
	while run:
		move = input('where u wanna play? (1-9) 1 = upper left 9 = bottom right: ')
		try:
			move = int(move)
			if move > 0 and move < 10:
				if spaceIsFree(move):
					run = False
					insertBoard('X', move)
				else:
					print('taken, choose a new space')
			else:
				print('what are you doing?? Type within the range... ')
		except:
			print('a number fool')


def selectRandom(li):
	import random
	ln = len(li)
	r = random.randrange(0, ln)
	return li[r]

def compMove():
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
	move = 0

	# check for winning move to take or to block
	for let in ['O', 'X']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] = let
			if isWinner(boardCopy, let):
				move = i
				return move

	# try to take corners
	cornersOpen = []
	for i in possibleMoves:
		if i in [1, 3, 7, 9]:
			cornersOpen.append(i)
	if len(cornersOpen) > 0:
		move = selectRandom(cornersOpen)
		return move

	# try to take center
	if 5 in possibleMoves:
		move = 5
		return move 		 

	# take any edge
	edgesOpen = []
	for i in possibleMoves:
		if i in [2, 4, 6, 8]:
			edgesOpen.append(i)
	
	if len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)
	
	return move


def isBoardFull(board):
	if board.count(' ') > 1:
		return False
	else:
		return True


def printBoard(board):
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | '+ board[3])
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | '+ board[6])
	print('-----------')
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | '+ board[9])
	print('   |   |')



# main loop
def main():
	print('This tic-tac-toe level up version')
	print('%s wins, %s ties, %s losses' % (wins, ties, losses))
	printBoard(board)
	while not(isBoardFull(board)):
		if not(isWinner(board, 'O')):
			playerMove()
			printBoard(board)
		else:
			print('O\'s victory, u lose sucka')		
			break

		if not(isWinner(board, 'X')):
			move = compMove()
			if move == 0:
				print('tie')
			else:
				insertBoard('O', move)
				print('computer placed an O in position', move, ': ')
				printBoard(board)
		else:
			print('X\'s victory, gg')	
			print(score(wins, ties, losses))
			break

# score
wins = 0
ties = 0
losses = 0

main()














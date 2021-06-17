#2-player Tic-Tac-Toe in Python

grid = {'1':' ', '2':' ', '3':' ',
		'4':' ', '5':' ', '6':' ',
		'7':' ', '8':' ', '9':' '}

def resetGrid():
	for i in grid:
		grid[i] = ' '

def printGrid(grid):
	print(grid['1'] + '|' + grid['2']+ '|' + grid['3'])
	print('-+-+-')
	print(grid['4'] + '|' + grid['5']+ '|' + grid['6'])
	print('-+-+-')
	print(grid['7'] + '|' + grid['8']+ '|' + grid['9'])

def game():
    print("LET'S PLAY!\n")

    turn = 'X'
    endGame = 0

    while endGame < 9:
    	printGrid(grid)
    	print("It is Player " + turn + " turn.")

    	move = input("Choose location:")
    	
    	if grid[move] == ' ':
    		grid[move] = turn
    		endGame += 1
    	else:
    		print('Location is already filled.\n')
    		endGame -= 1
    		continue

    	#Check winning combinations after 5 moves
    	if endGame >= 5:
    		if grid['1'] == grid['2'] == grid['3'] != ' ': #top row
    			print('Player ' + turn +' won!')
    			break
    		elif grid['4'] == grid['5'] == grid['6'] != ' ': #middle row
    			print('Player ' + turn +' won!')
    			break
    		elif grid['7'] == grid['8'] == grid['9'] != ' ': #bottom row
    			print('Player ' + turn +' won!')
    			break
    		elif grid['1'] == grid['5'] == grid['9'] != ' ': #right diagonal
    			print('Player ' + turn +' won!')
    			break
    		elif grid['7'] == grid['5'] == grid['3'] != ' ': #left diagonal
    			print('Player ' + turn +' won!')
    			break
    		elif grid['1'] == grid['4'] == grid['7'] != ' ': #left vertical
    			print('Player ' + turn +' won!')
    			break
    		elif grid['2'] == grid['5'] == grid['8'] != ' ': #middle vertical
    			print('Player ' + turn +' won!')
    			break
    		elif grid['3'] == grid['6'] == grid['9'] != ' ': #right vertical
    			print('Player ' + turn +' won!')
    			break
    	
    	if endGame == 9:
    		print("Tie!") 

    	if turn == 'X':
    		turn = 'O'
    	else:
    		turn = 'X'

    restart = input("Do you want to play again? (Y/N)")
    

    if(restart == 'Y' or restart == 'y'):
    	resetGrid()
    	game()
    else:
    	print("Thanks for playing!")

if __name__ == "__main__":
	print("Welcome to Tic-Tac-Toe text version!\n")
	print('1' + '|' + '2' + '|' + '3')
	print('-+-+-')
	print('4' + '|' + '5' + '|' + '6')
	print('-+-+-')
	print('7' + '|' + '8' + '|' + '9')
	print('\nThe grid above shows which number corresponds to each location\n')
	game()

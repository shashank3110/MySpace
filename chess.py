import copy
from itertools import product



def check_diag(board,row,col):
	'''
	Checks possible victims along the diagonal
	before placing a Queen or a bishop.  Returns 
	False if a diagonal is non-empty(finds a victim).
	'''
	for i, j in zip(range(row, -1, -1),range(col, -1, -1)): 
	    if board[i][j] != '0': 
	    	return False
	# print('Upper Left victims')
	for i, j in zip(range(row, M, 1),range(col, N, 1)):
		if board[i][j] != '0':
			return False
	# print('Lower Right victims')
	for i, j in zip(range(row, M, 1),range(col, -1, -1)): 
	    if board[i][j] != '0': 
	    	return False
	# print('Lower Left victims')
	for i, j in zip(range(row, -1, -1),range(col, N, 1)):
  		if board[i][j] != '0':
  			return False
	return True

def check_straight(board,row,col):
	'''
	Checks possible victims along the straight lines
	before placing a Queen or a Rook.  Returns 
	False if a straight path is non-empty(finds a victim).
	'''
	board_col=list(zip(*board)) #to traverse the columns
	for e in board[row]:
		if e!='0':
		   return False
	for e in board_col[col]:
		if e!='0':
			return False
	return True

def place_bishop(board,row,col):
	'''
	Checks victims aand attackers of and for the Bishop.
	eg: check_diag -> checks victims of bishop
		place -> checks attackers surrounding this bishop.
	'''
	if check_diag(board,row,col) and place(board,row,col):
		return True
	return False

def place_queen(board,row,col):
	'''
	Checks victims aand attackers of and for the Queen.
	'''
	if check_straight(board,row,col) and check_diag(board,row,col)\
		 and place(board,row,col):
		return True
	return False

def place_rook(board,row,col):
	'''
	Checks victims aand attackers of and for the Rook.
	'''
	if check_straight(board,row,col) and place(board,row,col):
		return True
	return False

def place_knight(board,row,col):
	'''
	Checks victims aand attackers of and for the Knight.
	'''
	knight_positions=[(row-2,col-1),(row-1,col-2),\
	(row-2,col+1),(row-1,col+2), (row+1,col-2),(row+2, col-1),\
	(row+2,col+1),(row+1,col+2)]
	for i,j in knight_positions:
		
		if i<0 or j<0 or i>=M or j>=N:
			continue

		if board[i][j]!='0':
			return False

	if place(board,row,col):
		return True
	return False


def place_king(board,row,col):
	'''
	Checks victims aand attackers of and for the Bishop.
	'''
	for i in range(max(row-1,0),min(row+2,M)):
		for j in range(max(col-1,0),min(col+2,N)):
			if board[i][j] != '0':
				return False
	if place(board,row,col):
		return True
	return False

def place(board,row,col):
	'''
	Common function for surrounding attackers
	for a given piece. 

	board: current board config.
	row: current row index for the piece
	col: current col. index for the piece
	'''
	board_col=list(zip(*board))
	knight_positions=[(row-2,col-1),(row-1,col-2),\
	(row-2,col+1),(row-1,col+2), (row+1,col-2),(row+2, col-1),\
	(row+2,col+1),(row+1,col+2)]

	if 'Q' in board[row] or 'Q' in board_col[col]:
		return False
	if 'R' in board[row] or 'R' in board_col[col]:
		return False
	# print('Queen & Rook straight lines checked')

	for i,j in knight_positions:
		
		if i<0 or j<0 or i>=M or j>=N:
			continue

		if board[i][j]=='N':
			return False
	# print('Knight Checked')

	for i in range(max(row-1,0),min(row+2,M)):
		for j in range(max(col-1,0),min(col+2,N)):
			if board[i][j] == 'K':
				return False
	# print('King Checked')

	for i, j in zip(range(row, -1, -1),range(col, -1, -1)): 
	    if board[i][j] == 'Q' or board[i][j] == 'B': 
	    	return False
	# print('Upper Left Queen/Bishop checked')
	for i, j in zip(range(row, M, 1),range(col, N, 1)):
		if board[i][j] == 'Q' or board[i][j] == 'B':
			return False
	# print('Lower Right Queen/Bishop checked')
	for i, j in zip(range(row, M, 1),range(col, -1, -1)): 
	    if board[i][j] == 'Q' or board[i][j] == 'B': 
	    	return False
	# print('Lower Left Queen/Bishop checked')
	for i, j in zip(range(row, -1, -1),range(col, N, 1)):
  		if board[i][j] == 'Q' or board[i][j] == 'B':
  			return False
	# print('Upper Right Queen/Bishop checked')

	return True


def get_board(m,n):
	'''
	Initializes the chess board.
	m: number of rows
	n: number of columns
	'''
	board=[]
	
	for _ in range(m):
		row=['0' for j in range(n)]
		board.append(row)
	
	return board

def place_pieces(m,n,pieces,board):
	'''
	Function to places all the pieces safely on the board.
	m: no. of rows
	n: no.of cols.
	pieces: list of pieces eg: ['K','K','Q','R','N']
	board: current board configuration
	'''

	if len(pieces)==0:
		return True
	print(f'Number of pieces left={len(pieces)}')

	for ix,p in enumerate(pieces):

		display_board(board)
		for i,j in product(range(m),range(n)): 
			#generates all board positions (0,0),(0,1),(1,0),etc.

				if board[i][j] != '0': 
					#check if a square is empty
					continue

				if piece_dict[p](board,i,j): 
					#try placing a piece at location (i,j)
					board[i][j]=p

					if place_pieces(m,n,pieces[ix+1:],board):
						#using current board config. try placing other pieces
						return True

					'''
					incase of unsuccessful placement of subsequent pieces
					reset the board at (i,j).
					'''
					board[i][j]='0'	
					pieces=copy.deepcopy(all_pieces[-(len(pieces)+1):])
					
	return False

def display_board(board):
	'''
	Displays current board config.
	'''
	for board_row in board:
		print(board_row)
	print("############")

if __name__ == '__main__':
	
	M=int(input("Enter number of rows: ")) #number of rows
	N=int(input("Enter number of columns: ")) #number of columns
	board=get_board(M,N)
	piece_dict={'K':place_king,'Q':place_queen,'B':place_bishop,'R':place_rook,'N':place_knight}
	all_pieces=input("Enter pieces eg: Q,K,K,R,B,N: ")
	all_pieces=all_pieces.split(',')

	print(all_pieces)
	result=place_pieces(M,N,all_pieces,board)
	print('Final Board')
	'''
	safest possible placementin if all pieces can be placed safely
	or atmost how many pieces can be placed safely
	'''
	display_board(board)
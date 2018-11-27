def printboard(): 
    
    print(' ')
    print(' '+ board[6] +' | '+ board[7] +' | '+ board[8])
    print('-----------')
    print(' '+ board[3] +' | '+ board[4] +' | '+ board[5])
    print('-----------')
    print(' '+ board[0] +' | '+ board[1] +' | '+ board[2])
    print(' ')

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

printboard()

def add_player_name():
    print('Welcome to Tic Tac Toe')
    print ('Player 1s name: ')
    Player1 = input()
    print ('Player 2s name: ')
    Player2 = input()
    print (' ')
    print ((Player1) +' is X and '+ (Player2) + ' is O')

add_player_name()

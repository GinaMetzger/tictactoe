import os


# the program draw a board where the players can be play
def printboard():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print(' ')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(' ')


printboard()


# player1 and player2 can give their names
def add_player_name():
    print('Welcome to Tic Tac Toe')
    print('Player 1s name: ')
    Player1 = input()
    print('Player 2s name: ')
    Player2 = input()
    print(' ')
    print((Player1) + ' is X and ' + (Player2) + ' is O')

    printboard()


add_player_name()


# checks the winner
def check_win_game(board, win_player):
    if (board[1] == win_player and board[2] == win_player and board[3] == win_player or
        board[4] == win_player and board[5] == win_player and board[6] == win_player or
        board[7] == win_player and board[8] == win_player and board[9] == win_player or
        board[1] == win_player and board[4] == win_player and board[7] == win_player or
        board[2] == win_player and board[5] == win_player and board[8] == win_player or
        board[3] == win_player and board[6] == win_player and board[9] == win_player or
        board[1] == win_player and board[5] == win_player and board[9] == win_player or
            board[3] == win_player and board[5] == win_player and board[7] == win_player):
        return True
    else:
        return False


# which player is the winner
def player_win():
    if check_win_game(board, 'X'):
        print('Congratulations! X win!')
    if check_win_game(board, 'O'):
        print('Congratulations! O win!')

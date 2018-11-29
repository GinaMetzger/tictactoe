import os

# the program draw a board where the players can be play
def printboard(board):
    print(' ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' ')


# player1 and player2 can give their names
def add_player_name():
    print('Welcome to Tic Tac Toe')
    print('Player 1s name: ')
    Player1 = input()
    print('Player 2s name: ')
    Player2 = input()
    print(' ')
    print((Player1) + ' is X and ' + (Player2) + ' is O')


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
def play_game(board, player1, player2):
    movecount = 0
    while True:
        if (movecount % 2 == 0):
            try:
                move = input('Xs turn (1-9):')
                move = int(move)
                if move >= 1 and move <= 9:
                    if board[move] == ' ':
                        board[move] = 'X'
                        printboard(board)
                        movecount = movecount + 1
                    else:
                        print('This position is already taken, choose another one!')
            except ValueError:
                print('Invalid move! Try again')
        os.system("clear")
        printboard(board)
        if check_win_game(board, 'X'):
            print('Congratulations, X won!')
            break
        else:
            try:
                move = input('Os turn (1-9):')
                move = int(move)
                if move >= 1 and move <= 9:
                    if board[move] == ' ':
                        board[move] = 'O'
                        printboard(board)
                        movecount = movecount + 1
                    else:
                        print('This position is already taken, choose another one!')
            except ValueError:
                print('Invalid move! Try again')
        os.system("clear")
        printboard(board)
        if check_win_game(board, 'O'):
            print('Congratulations! O won!')
            break


def replay(board):
    play_again = input('Would you like to play again? Please type Y for YES or N for NO.')
    if play_again.upper() == 'Y':
        main()
        os.system("clear")
        printboard(board)
    elif play_again.upper() == 'N':
        print('See you later!')


# start the game
def main():
    b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    printboard(b)
    add_player_name()
    os.system("clear")
    play_game(b, 'X', 'O')
    check_win_game(b, 'winner')
    replay(b)


main()

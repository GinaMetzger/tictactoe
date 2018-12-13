import os
import time
import random


# welcome title
def print_header():
    print("""
WELCOME TO
 _____  _  ____     _____   ____    ____     _____  ____  _____
/__ __\| |/   _\   /__ __\ /  _ \  /   _\   /__ __\/  _ \/  __/  
  | |  | ||  / _____ | |   | | | | |  / _____ | |  | / \||  \ 
  | |  | ||  \_\____\| |   | |-| | |  \_\____\| |  | \_/||  /_
  |_|  |_|\____/     |_|   |_| |_| \____/     |_|  \____/\____\ 

""")


# the program draw a board where the players can be play
def printboard(board):
    print(' ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '    ' + '      ' + '7' + ' | ' + '8' + ' | ' + '9')
    print('-----------' + '        ' + '-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '    ' + '      ' + '4' + ' | ' + '5' + ' | ' + '6')
    print('-----------' + '        ' + '-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '    ' + '      ' + '1' + ' | ' + '2' + ' | ' + '3')
    print(' ')


# game menü to different player mode
def menu(board):
    print('\n' + '---------MAIN MENU---------')
    print('\n' + '1. Single player' + '\n' + '2. Multiplayer' + '\n' + '3. Exit game')
    try:
        choice = input(">>> ")
        choice = int(choice)
        if choice == 1:
            singleplayer_game(board)
        elif choice == 2:
            main()
        elif choice == 3:
            print('See you next time!')
            exit(0)
        else:
            print('Wrong number! Choose 1, 2 or 3!')
            time.sleep(1)
            os.system("clear")
            menu()
    except ValueError:
        print('Invalid choice! Try again')
        time.sleep(1)
        os.system("clear")
        menu()


# player1 and player2 can give their names
def add_player_name():
    print('Player 1s name: ')
    Player1 = input()
    print('Player 2s name: ')
    Player2 = input()
    print(' ')
    print((Player1) + ' is X and ' + (Player2) + ' is O')
    time.sleep(1)


# checks the winner on board
def check_win_game(board, win_player):
    return (board[1] == win_player and board[2] == win_player and board[3] == win_player or
            board[4] == win_player and board[5] == win_player and board[6] == win_player or
            board[7] == win_player and board[8] == win_player and board[9] == win_player or
            board[1] == win_player and board[4] == win_player and board[7] == win_player or
            board[2] == win_player and board[5] == win_player and board[8] == win_player or
            board[3] == win_player and board[6] == win_player and board[9] == win_player or
            board[1] == win_player and board[5] == win_player and board[9] == win_player or
            board[3] == win_player and board[5] == win_player and board[7] == win_player)


# write who is the winner
def win_game(board):
    if check_win_game(board, 'X'):
        print('Congratulations, X won!')
        replay()
    elif check_win_game(board, 'O'):
        print('Congratulations, O won!')
        replay()
    else:
        no_winner(board)


# when the game is tied
def no_winner(board):
    count = 0
    for i in range(1, 10):
        if board[i] == "X" or board[i] == "O":
            count += 1
    if count == 9:
        print("The game ends in a Tie")
        replay()
        return True
    return False


# program can clear the whole board
def clear_board(board):
    os.system("clear")
    printboard(board)


# player full move function
def move_player(board):
    while True:
        clear_board(board)
        move_on_board(board, 'X')
        time.sleep(1)
        clear_board(board)
        move_on_board(board, 'O')
        time.sleep(1)


# player moves on board
def move_on_board(board, player):
    movecount = 0
    try:
        move = input('Next move (1-9):')
        move = int(move)
        if move in range(1, 10):
            if board[move] == ' ':
                board[move] = player
                movecount = movecount + 1
            else:
                print('This position is already taken, choose another')
    except ValueError:
        print('Invalid move! Try again')
    win_game(board)


# AI moves
def computer_move(board, computer):
    move = random.randint(1, 10)
    if board[move] == ' ':
        board[move] = computer
    else:
        print('This position is already taken, choose another')
    win_game(board)


# start singleplayer game
def singleplayer_game(board):
    print('Player is X and Computer is O.')
    print('Player is start the game.')
    time.sleep(2)
    while True:
        clear_board(board)
        move_on_board(board, 'X')
        time.sleep(1)
        clear_board(board)
        print('Computer turns')
        computer_move(board, 'O')
        time.sleep(1)


# restart the game
def replay():
    while True:
        print('Would you like to play again? (Please type y for yes or n for no.)')
        choice = input("> ")
        if choice.lower().startswith('y'):
            menu(board=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        elif choice.lower().startswith('n'):
            print('See you next time!')
            exit(0)
        else:
            print("I don't understand what you mean?")


# start the game
def main():
    b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    os.system("clear")
    print_header()
    printboard(b)
    add_player_name()
    os.system("clear")
    move_player(b)


menu(board=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

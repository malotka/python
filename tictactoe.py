from IPython.display import clear_output

"""Function for displaying the board"""
def display_board(board):

    clear_output()
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")

"""Taking an input from a player"""
def player_input():

    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Do you want to be X or O: ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

"""Placing input on the board"""
def place_marker(board, marker, position):

    board[int(position)-1] = marker

"""Checking for win"""
def win_check(board, mark):

    return ((board[6] == mark and board[7] == mark and board[8] == mark) or
    (board[3] == mark and board[4] == mark and board[5] == mark) or
    (board[0] == mark and board[1] == mark and board[2] == mark) or
    (board[6] == mark and board[3] == mark and board[0] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[6] == mark and board[4] == mark and board[2] == mark) or
    (board[8] == mark and board[4] == mark and board[0] == mark))

"""Random choosing of player"""
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"

"""Checking if space on board is availabaila"""
def space_check(board, position):
    return board[position - 1] == " "

"""Checking if board is full"""
def full_board_check(board):
    for i in range(0,9):
        if space_check(board, i):
            return False

    return True

"""Player's choice of position"""
def player_choice(board):
    position = " "
    while position not in "1 2 3 4 5 6 7 8 9".split() or not space_check(board, int(position)):
        position = input("Please choose where to put a mark: (1-9): ")

    return int(position)

"""Ask if play again"""
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

if __name__ == '__main__':
    print("TIC TAC TOE GAME")
    while True:

        #new empty board:
        board = [' '] * 9
        #who starts first:
        turn = choose_first()
        #chosen marks:
        player1_maker, player2_maker = player_input()
        print(turn, " will start a game!")

        game_on = True

        while game_on:
            if turn == "Player 1":
                display_board(board)
                position = player_choice(board)
                place_marker(board, player1_maker, position)

                if win_check(board, player1_maker):
                    display_board(board)
                    print("PLAYER 1 WON!")
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("NO WINNER :<")
                        break
                    else:
                        turn = "Player 2"

            else:
                display_board(board)
                position = player_choice(board)
                place_marker(board, player2_maker, position)

                if win_check(board, player2_maker):
                    display_board(board)
                    print("PLAYER 2 WON!")
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("NO WINNER :<")
                        break
                    else:
                        turn = "Player 1"

        if not replay():
            break


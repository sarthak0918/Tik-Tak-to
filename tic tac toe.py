board = ['-','-','-',
         '-','-','-',
         '-','-','-',]
#-------GLOBAL VARIABLE------
game_is_still_going = True
current_player = 'X'
winner = None

def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

#display_board()
def play_game(): # it will drive the whole game
    display_board()#Display intial board
    while game_is_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()# Here what we are using a game is while loop so that game still goes on but if someone wins its gonna stop

    if winner == 'X' or winner == 'O':
        print(winner+' WON')
    elif winner == None:
        print("Tie")

def handle_turn(current_player):
    valid = False
    while not valid:
        print(current_player + "'s turn")
        position = input("choose a position from 1-9:")  # this will ask the input we want to give
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Invalid input, choose a position from 1-9:")
        position = int(
            position) - 1  # this will correct the position as position in board list start with 0 and here we are starting from 1-9
        if board[position] == '-':
            valid = True
        else:
            print("you can't go there, GO again")
        board[position] = current_player  # in this way we are changing - from board to X
        display_board()


def check_if_game_over():# so the game will be over if someone wins or the board is full or the game is tied
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    row_winner =  check_row()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner  = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
        return

def check_row():# this will be defined when all elements in a row are equal
    global game_is_still_going
    row_1 = board[0] == board[1] == board[2] != '-'# this ! says that all must not be equal to -
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
        game_is_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_columns():
    global game_is_still_going
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[5] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    if column_1 or column_2 or column_3:
        game_is_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[2]
    elif column_3:
        return board[3]

def check_diagonals():
    global game_is_still_going
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'
    if diagonal_1 or diagonal_2:
        game_is_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

def check_if_tie():
    global game_is_still_going
    if '-' not in board:
        game_is_still_going = False

    return
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

    return
play_game()

# board
# display board
# play game
# check tie
# check win
  # check row
  # check columns
  # check diagonals
# flip player
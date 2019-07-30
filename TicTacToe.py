# Just added this to check if my code commits.


import sys
from random import randint
# GENERATE A RANDOM NUMBER TO PICK WHO STARTS FIRST
rand_player = randint(0, 1)


def intro():
    print("Welcome to Tic-Tac-Toe!")
    response = input("Do you want to play? ")

    # CHECK IF RESPONSE IS YES OR NO.
    while True:
        if response == 'Yes':
            return 'There will be two players. The first player will be chosen at random. \n'

        elif response == 'No':
            print('Sorry to see you go :( :( :(')
            sys.exit()
        else:
            response = input('Enter either Yes or No: ')


def game_board(in_board):
    print(in_board[0] + '|' + in_board[1] + '|' + in_board[2])
    print(in_board[3] + '|' + in_board[4] + '|' + in_board[5])
    print(in_board[6] + '|' + in_board[7] + '|' + in_board[8])


g_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# GET THE POSITION AND SYMBOL FROM "the_game" TO POPULATE THE BOARD.
def board(position, symbol):
    g_board[position - 1] = symbol
    return g_board


# RETURN WHICH PLAYER GOES FIRST
def player():
    if rand_player == 0:
        return 'One'
    else:
        return 'Two'


# TAKES IN THE GAME BOARD AND SYMBOL TO DETERMINE THE WINNER
def winner(gameboard, winning_symbol):
    # CHECK FOR MATCHING ROWS
    if (gameboard[0] == winning_symbol and gameboard[1] == winning_symbol and gameboard[2] == winning_symbol) or \
            (gameboard[3] == winning_symbol and gameboard[4] == winning_symbol and gameboard[5] == winning_symbol) or \
            (gameboard[6] == winning_symbol and gameboard[7] == winning_symbol and gameboard[8] == winning_symbol):
        return winning_symbol

    # CHECK FOR MATCHING COLUMNS
    elif (gameboard[0] == winning_symbol and gameboard[3] == winning_symbol and gameboard[6] == winning_symbol) or \
            (gameboard[1] == winning_symbol and gameboard[4] == winning_symbol and gameboard[7] == winning_symbol) or \
            (gameboard[2] == winning_symbol and gameboard[5] == winning_symbol and gameboard[8] == winning_symbol):
        return winning_symbol

    # CHECK FOR MATCHING DIAGONALS
    elif (gameboard[0] == winning_symbol and gameboard[4] == winning_symbol and gameboard[8] == winning_symbol) or \
            (gameboard[2] == winning_symbol and gameboard[4] == winning_symbol and gameboard[6] == winning_symbol):
        return winning_symbol


def play_gain():
    return input('Do you want to play again: ')


# THE GAME
def the_game():
    players_inputs = []
    decision = True

    # USE THE "player" FUNCTION TO ALLOCATE WHICH PLAYER GOES FIRST
    if player() == 'One':
        player1_name = 'Player One'
        player2_name = 'Player Two'
    else:
        player1_name = 'Player Two'
        player2_name = 'Player One'

    print('{} will go first! ' .format(player1_name))

    # ASK THE PLAYERS TO CHOSE THEIR SYMBOLS TO BE PLACED ON THE BOARD
    first_symbol = input('{} chose a symbol: ' .format(player1_name))
    second_symbol = input('{} chose a symbol: ' .format(player2_name))

    # PLAYER MAKES A MOVES, CALL THE BOARD AND PASS IN THE MOVE MADE BY THE PLAYER
    while decision:
        first_input = int(input('{} make a move: ' .format(player1_name)))
        while first_input in players_inputs:
            first_input = int(input('Not too quick, make a different move {}: ' .format(player1_name)))
        players_inputs.append(first_input)
        print(game_board(board(first_input, first_symbol)))

        # CHECK WHICH PLAYER WIN BASED ON THE SYMBOL
        if (winner(g_board, first_symbol)) == first_symbol:
            return'Player {} wins!!!!!!!!!\n' .format(player1_name)

        second_input = int(input('{} make a move: ' .format(player2_name)))
        while second_input in players_inputs:
            second_input = int(input('Not too quick, make a different move {}: ' .format(player2_name)))
        players_inputs.append(second_input)
        print(game_board(board(second_input, second_symbol)))

        # CHECK WHICH PLAYER WIN BASED ON THE SYMBOL
        if (winner(g_board, second_symbol)) == second_symbol:
            return 'Player Two wins!!!!!!!!! \n' .format(player2_name)


if __name__ == "__main__":
    # CALL THE "intro" FUNCTION
    print(intro())
    print(the_game())

    # ASK IF THE PLAYERS WANT TO PLAY AGAIN
    choice = input('Do you want to play again? ')
    print(' ')

    while choice == 'Yes':
        if choice == 'Yes':
            g_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            print(the_game())
        elif choice == 'No':
            sys.exit()
        else:
            choice = input("Enter either 'Yes' or 'No'? ")
        choice = input('Do you want to play again? ')
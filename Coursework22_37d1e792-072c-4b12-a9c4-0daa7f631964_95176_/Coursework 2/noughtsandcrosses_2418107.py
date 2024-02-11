import random
import os.path
import json
random.seed()

ENCODING = 'utf-8'

def draw_board(board):
    print("-"*5)
    for row in board:
        print("|".join(row))
        print("-"*5)
    pass


def welcome(board):
    # prints the welcome message
    print("""Welcome to the "Unbeatable Noughts and Crosses" game. 
          The Board layout is shown below  ;)  """)
    # display the board by calling draw_board(board)
    print("When prompted, please enter the number corresponding to the board to place your input.")
    draw_board(board)

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for i in range(3):
        for j in range(3):
            board[i][j]=' '
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    valid_choice = False
    while not valid_choice:
        user_choice = int(input("Enter your move \n 1 2 3 \n 4 5 6 \n 7 8 9::  "))
        if user_choice >= 1 and user_choice <= 9:
            valid_choice = True
        else:
            print("Invalid Input. Please Enter your choice again..")
            continue
    row = (user_choice - 1) // 3 + 1
    col = (user_choice - 1) % 3 + 1
    return row, col

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    while True:
        # Choose a random row and column
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        # Check if the chosen cell is unoccupied
        if board[row][col] == ' ':
            return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows
        if all(board[i][j] == mark for j in range(3)):
            return True

        # Check columns
        if all(board[j][i] == mark for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    # Check if all cells are occupied
    return all(all(cell != ' ' for cell in row) for row in board)
        
def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    initialise_board(board)
    # then draw the board
    draw_board(board)
    # then in a loop, get the player move, update and draw the board
    while True:
        # Get the player's move, update and draw the board

        player_row, player_col = get_player_move(board)
        board[player_row - 1][player_col - 1] = 'X'
        draw_board(board)
    
    
    
        # Check if the player has won
        if check_for_win(board, 'X'):
            print("Congratulations! You won!")
            return 1

        # Check for a draw
        if check_for_draw(board):
            print("It's a draw!")
            return 0

        # Choose a move for the computer
        print("-"*10)
        print("Computer moves::")
        computer_row, computer_col = choose_computer_move(board)
        board[computer_row][computer_col] = 'O'
        draw_board(board)

        # Check if the computer has won
        if check_for_win(board, 'O'):
            print("Oops! The computer won. Well that is a bummer")
            return -1
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    print("Menu:")
    print("1 - Play the game")
    print("2 - Save score in file 'leaderboard.txt'")
    print("3 - Load and display the scores from 'leaderboard.txt'")
    print("q - End the program")

    choice = input("Enter your choice: ")
    return choice

def load_scores():
    """
    Opens the leaderboard file and retrieves the data as a dictionary

            Parameters:
                    None

            Returns:
                    leaders (dictionary)
    """
    filename = 'leaderboard.txt'

    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding = ENCODING) as file:
                leaders = json.load(file)

        except json.JSONDecodeError:
            leaders = {}
    else:
        leaders = {}

    return leaders


def save_score(score):
    """
    Opens the leaderboard file and saves user score in the file

            Parameters:
                    score (int)

            Returns:
                    None
    """
    if not score:
        score = 0

    name = input("Please enter your name: ")
    filename = 'leaderboard.txt'

    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding = ENCODING) as file:
                leaders = json.load(file)

        except json.JSONDecodeError:
            leaders = {}
    else:
        leaders = {}

    leaders[name] = score

    with open(filename, 'w', encoding = ENCODING) as file:
        json.dump(leaders, file)
        print('Updated the leaderboard!')


def display_leaderboard(leaders):
    """
    Prints the leaderboard from the leaderboard.txt file

            Parameters:
                    score (int)

            Returns:
                    None
    """
    leaders_list = list(leaders.items())
    sorted_leaders = []

    while leaders_list:
        high_score = leaders_list[0]

        for item in leaders_list:
            if item[1] > high_score[1]:
                high_score = item

        leaders_list.remove(high_score)
        sorted_leaders.append(high_score)

    for item in sorted_leaders:
        print(f"{item[0]}: {item[1]}")
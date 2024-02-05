import random
import os.path
import json
random.seed()


def draw_board(board):
    for row in board:
        print("|".join(row))
        print("-"*5)
    print("When prompted, please enter the number corresponding to the board to place your input.")
    pass


def welcome(board):
    # prints the welcome message
    print("""Welcome to the "Unbeatable Noughts and Crosses" game. 
          The Board layout is shown below  ;)  """)
    # display the board by calling draw_board(board)
    draw_board(board)
    pass

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
        user_choice = int(input("Enter your move:: "))
        if user_choice >= 1 and user_choice <= 9:
            valid_choice = False
        else:
            print("Invalid Input. Please Enter your choice again..")
            continue
    row = (user_choice - 1) // 3 + 1
    col = (user_choice - 1) % 3 + 1
    return row, col

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    return True
        
def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    initialise_board(board)
    # then draw the board
    
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop
    return 0
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    return leaders
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    pass


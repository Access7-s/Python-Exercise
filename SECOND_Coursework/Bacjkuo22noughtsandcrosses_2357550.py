import random
import os.path
import json
random.seed()

def draw_board(board):
    # develop code to draw the board
    for row in range(3):
        print("-----------")
        for col in range(3):
            print(f"| {board[row][col]}", end="")
        print('|')
    print("-----------")
    
    pass

def welcome(board):
    # prints the welcome message
    print(''''Welcome to the "Unbeatable Noughts and Crosses" game.\nThe board layout is shown below''')
    
    # display the board by calling draw_board(board)
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")

    pass

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    valid = True
    while valid:
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            n_row = row - 1
            n_col = col - 1
            if (n_row < 3 and n_row >= 0) and (n_col < 3 and n_col >=0) :
                if board[n_row][n_col] == " ":
                    valid = False
                # and return row and col
                    return n_row, n_col
                else:
                    print("It has been occupied ")
            else:
                print("Invalid row or column, please enter again !!!")
        except ValueError:
            print("Invalid Input. please input integer value among [0,1,2]")
        

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        # and return row and col
        if board [row][col] == ' ':
            return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0]== board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    
    # return True if someone won, False otherwise
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    cells = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":
                cells += 1

    if cells == 9:
        return True
    # return True if it is, False otherwise

    return False
        
def play_game(board):
    # star with a call to the initialise_board(board) function to set
    board = initialise_board(board)
    
    # then draw the board
    draw_board(board)
    
    # then in a loop, get the player move, update and draw the board
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        
        # check if the player has won by calling check_for_win(board, mark),
        if check_for_win(board, 'X'):
            print("You Won!!!")
            return 1
        
        # if not check for a draw by calling check_for_draw(board)
        if check_for_draw(board):
            print("OOps it's Draw")
            return 0
        
        # if not, then call choose_computer_move(board)
        row, col = choose_computer_move(board)
        print("Computer has played....")
        
        # to  choose a move for the computer 
        board[row][col] = 'O'
        
        # update and draw the board
        draw_board(board)
        
        # check if the computer has won by calling check_for_win(board, mark),
        if check_for_win(board, "O"):
            print("You lose, Computer won")
            return -1
        
        # if not check for a draw by calling check_for_draw(board)
        if check_for_draw(board):
            print("Its draw")
            return 0
        
    #repeat the loop
    return 0
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    while True:
        menu='''Please select an option:

                1 - Play the game
                2 - Save scores in the 'leaderboard.txt'
                3 - Load and display the scores from the 'leaderboard.txt'
                q - End the program
                '''
        print(menu)
        choice = input("Enter of either '1', '2', '3' or 'q' to continue : ")

        if choice in ['1', '2', '3', 'q']:
            return choice
        else:
            print("Invalid choice. Please try again.")
    return choice

def load_scores():

    leaders = {}
    if os.path.isfile("leaderboard.txt") and (os.path.getsize("leaderboard.txt")==0) is False:
        with open("leaderboard.txt", encoding="utf-8") as file:
            scores = json.load(file)
            for name, score in scores.items():
                leaders[name] = score

    return leaders


def save_score(score):
    """
    Takes socre as a argument.
    Prompts the user for their name and adds it with the score in a file in Json format.
    """

    # Prompt the user for their name.
    name = input("Enter your name: ").strip().title()

    # Get the players from the file
    players = load_scores()

    # If there are players, add the user with thier score and overwrite the file.
    # Else, Create a new dictionary and add it to the file.
    if players:
        with open("leaderboard.txt", "w", encoding="utf-8") as file:
            players[name] = score
            json.dump(players, file)
    else:
        with open("leaderboard.txt", "w", encoding="utf-8") as file:
            player = {name: score}
            json.dump(player, file)
    print("Scored Saved !!!!")


def display_leaderboard(leaders):
    """
    Displays the leaderboard if there is one.
    """
    if leaders:
        print("Leaderboard:")
        for name, score in leaders.items():
            print(f"{name}: {score}")

    # passed in the Python dictionary parameter leader
    pass

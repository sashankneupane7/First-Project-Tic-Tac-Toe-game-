#prints the instructions for the user to understand the basics of game...
print("\n"+"The instructions:"+"\n")
print("This is a game played by two players.")
print("1"+" | "+"2"+" | "+"3")
print("4"+" | "+"5"+" | "+"6")
print("7"+" | "+"8"+" | "+"9")
print("Your response will be received as a number from 1 to 9, each number representing the position as shown above."+"\n")

#-----Global variables-----
game_still_going = True
board = ["-","-","-","-","-","-","-","-","-"]
player1 = input("Who wants to play as X?"+"\n")
player2 = input("\n"+"And who wants to play as O?" + "\n")
current_player = "X"
winner = None

#displays the tic tac toe board
def display_board():
    print(board[0], " | ", board[1], " | ", board[2])
    print(board[3], " | ", board[4], " | ", board[5])
    print(board[6], " | ", board[7], " | ", board[8])
    return

#runs the program until the user ends the game
def play_game():
    global board
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    while game_still_going:
        display_board()
        handle_turn()
        check_if_win()
        check_if_tie()
        flip_player()
    return

#handles turns of the user, and checks if the provided input is valid
def handle_turn():
    global current_player
    global player1
    global player2
    position = None
    
    #prints player's name to make the game process be less confusing to players
    if current_player == "X":
        position = input("\n"+"It's "+player1+"'s turn. Enter any number from 1 to 9:")
    elif current_player == "O":
        position = input("\n"+"It's "+player2+"'s turn. Enter any number from 1 to 9:")
    
    #checks whether the provided input above is valid
    while position not in ["1","2","3","4","5","6","7","8","9"] or board[int(position)-1] != "-":
        position = input("Invalid input. Enter non-repeated number from only 1 to 9:")

    board[int(position)-1] = current_player
    return

#checks if any of two users has already won the game
def check_if_win():
    global player1
    global player2
    winner_by_row = won_by_row()
    winner_by_column = won_by_column()
    winner_by_diagonal = won_by_diagonal()
    if winner_by_row or winner_by_column or winner_by_diagonal == "X":
        display_board()
        print("\n"+player1+" won this game.")
        once_more()
    elif winner_by_row or winner_by_column or winner_by_diagonal == "O":
        display_board()
        print("\n"+player2+" won this game.")
        once_more()
    return

#checks if three elements in a single row is same
def won_by_row():
    winner_by_row = None
    if board[0] == board[1] == board[2] != "-":
        winner_by_row = board[0]
    elif board[3] == board[4] == board[5] != "-":
        winner_by_row = board[3]
    elif board[6] == board[7] == board[8] != "-":
        winner_by_row = board[7]
    return(winner_by_row)

#checks if three elements in a single column is same
def won_by_column():
    winner_by_column = None
    if board[0] == board[3] == board[6] != "-":
        winner_by_column = board[0]
    elif board[1] == board[4] == board[7] != "-":
        winner_by_column = board[1]
    elif board[2] == board[5] == board[8] != "-":
        winner_by_column = board[2]
    return(winner_by_column)

#checks if any of two diagonal's elements are same
def won_by_diagonal():
    winner_by_diagonal = None
    if board[0] == board[4] == board[8] != "-":
        winner_by_diagonal = board[0]
    elif board[6] == board[4] == board[2] != "-":
        winner_by_diagonal = board[6]
    return(winner_by_diagonal)

#checks if the game is tied
def check_if_tie():
    if "-" not in board:
        print("\n"+"It's a tie.")
        once_more()
    return

#flips the player on each move
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

#asks user if they want to play again
def once_more():
    do_you_wanna_play = input("Do you want to play the game once again? Answer in a yes or no:")
    while do_you_wanna_play.lower() != "yes" and do_you_wanna_play.lower() != "no":
        do_you_wanna_play = input("Invalid response. Do you want to play the game again?"+"\n")
    if do_you_wanna_play.lower() == "yes":
        play_game()
    elif do_you_wanna_play.lower() == "no":
        print("\n"+"Thank you for playing this game. Have a wonderful day ahead."+"\n")
        input("Press enter to exit this window.")
        quit()
    return

#calls the function to start the game
play_game()

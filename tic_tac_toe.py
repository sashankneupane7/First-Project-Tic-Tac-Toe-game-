#prints the instructions for the user to understand the basics of game...
print()
print('Hello and Welcome to our Tic Tac Toe game')
print('This is the standard notation of the board positions that you might need to use later.')

for j in range(1,9,3):
    print(str(j),'|',str(j+1),'|',str(j+2))
print()
print("Your response will be received as a number from 1 to 9, each number representing the position as shown above."+"\n")

def play_game():
    the_board()
    position_checker()
    game_checker()

def the_board():
    print()
    for i in range(0,8,3):
        print(moves[i],'|',moves[i+1],'|',moves[i+2])

def change_turn():
    global current_player
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

def position_checker():
    while True:
        try:
            play_position = int(input('It is ' + current_player + "'s turn. Enter the position where you want to play. (1-9): "))-1
        except ValueError:
            print('You must be kidding, right? Input a number from 1 to 9, or you would just end up messing with this infinite loop. :)')
            continue
        if play_position >= 9:
            print('Let me take a moment to remind you that there are only nine spaces in traditional TicTacToe.')
            continue
        elif moves[play_position] == '-':
            if current_player == player1:
                moves[play_position] = 'O'
            else:
                moves[play_position] = 'X'
            break
        else:
            print('The position is already used up. Please make sure you choose an empty position to continue playing.')
            continue

def game_checker():
    draw_checker()
    row_checker()
    diagonal_checker()
    column_checker()

def won_the_game():
    global winner
    the_board()
    winner = current_player
    print(winner, 'won the game. Thanks for playing with us!')

def row_checker():
    if moves[0] == moves[1] == moves[2] != '-' or moves[3] == moves[4] == moves[5] != '-' or moves[6] == moves[7] == moves [8] != '-':
        won_the_game()

def column_checker():
    if moves[0] == moves[3] == moves[6] != '-' or moves[1] == moves[4] == moves[7] != '-' or moves[2] == moves[5] == moves[8] != '-':
        won_the_game()

def diagonal_checker():
    if moves[0] == moves[4] == moves[8] != '-' or moves[2] == moves[4] == moves[6] != '-':
        won_the_game()

def draw_checker():
    global winner
    if '-' not in moves.values():
        print('It is a draw. Thanks for playing with us!')
        winner = 'No one'

def player_response():
    while True:
        player_interest = input('Do you want to play again? Answer in (yes/no)? ')
        if player_interest.lower() == 'yes':
            print('Alright! Here we go again.')
            return 'yes'
        elif player_interest.lower() == 'no':
            print('Thank you again for playing with us. See you again.')
            return 'no'
        else:
            print('Invalid input. Please read the instructions carefully!')
            continue

while True:
    moves = {0: '-', 1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-'}
    player1 = input('Enter the name of the player who is going to play with O: ')
    player2 = input('Enter the name of the player who is going to play with X: ')
    current_player = player1
    winner = ''

    while winner == '':
        play_game()
        change_turn()

    if player_response() == 'yes':
        continue
    else:
        break

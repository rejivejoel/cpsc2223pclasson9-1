# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 9 Assignment 3

def print_board(board):
    size = len(board)
    line = "-" * (size * 2 + 1)

    for row in board:
        print(line)
        print("|", end="")

        for item in row:
            print(item + "|", end="")

        print()

    print(line)


board1_list = [['*','*','*'],
               ['*','+','*'],
               ['*','*','*']]

print_board(board1_list)
print()

board2_list = [['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*']]

print_board(board2_list)
print()

board3_list = [['*',' ','*',' ','*'],
               [' ','*',' ','*',' '],
               [' ',' ',' ',' ',' '],
               [' ','+',' ','+',' '],
               ['+',' ','+',' ','+']]

print_board(board3_list)
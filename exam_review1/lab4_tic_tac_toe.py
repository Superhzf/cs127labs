#Tic-tac-toe game run watch
import time

#initial board shows valid board positions
board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#print board
#1. Get input string nine moves, eg: 1 3 5 4 2 7 9 8 6
steps=input("Please input the steps of two players: ")
steps=steps.split(" ")
steps=list(map(int,steps))
print("steps",steps)

#2. Assume the first move is player X. Alternate between player X and player O
#   Assume that the game keeps going until all the holes are filled. Do not stop even if a player wins.
#   Assume that the entry is correct, for eg: has all number between 1 and 9 and no numbers are repeated

#2.1 Move 1 Player X
board_list[steps[0]-1]="X"
#print board
print(" {} | {} | {} \n{}\n {} | {} | {} \n{}\n {} | {} | {} \n".format(board_list[0],
                                                                board_list[1],
                                                                board_list[2],
                                                                '-'*10,
                                                                board_list[3],
                                                                board_list[4],
                                                                board_list[5],
                                                                '-'*10,
                                                                board_list[6],
                                                                board_list[7],
                                                                board_list[8]))



#2.2 Time lag
time.sleep(2)

#2.3 Move 2 Player O
board_list[steps[1]-1]="O"
#print board
print(" {} | {} | {} \n{}\n {} | {} | {} \n{}\n {} | {} | {} \n".format(board_list[0],
                                                                board_list[1],
                                                                board_list[2],
                                                                '-'*10,
                                                                board_list[3],
                                                                board_list[4],
                                                                board_list[5],
                                                                '-'*10,
                                                                board_list[6],
                                                                board_list[7],
                                                                board_list[8]))

#2.4 Time lag
time.sleep(2)

#2.5 Move 3 Player X
board_list[steps[2]-1]="X"
#print board
print(" {} | {} | {} \n{}\n {} | {} | {} \n{}\n {} | {} | {} \n".format(board_list[0],
                                                                board_list[1],
                                                                board_list[2],
                                                                '-'*10,
                                                                board_list[3],
                                                                board_list[4],
                                                                board_list[5],
                                                                '-'*10,
                                                                board_list[6],
                                                                board_list[7],
                                                                board_list[8]))

#2.6 Time lag
time.sleep(2)

#2.7 Move 4 Player O
board_list[steps[3]-1]="O"
#print board
print(" {} | {} | {} \n{}\n {} | {} | {} \n{}\n {} | {} | {} \n".format(board_list[0],
                                                                board_list[1],
                                                                board_list[2],
                                                                '-'*10,
                                                                board_list[3],
                                                                board_list[4],
                                                                board_list[5],
                                                                '-'*10,
                                                                board_list[6],
                                                                board_list[7],
                                                                board_list[8]))

#2.8 Time lag
time.sleep(2)

#2.9 Move 5 Player X
board_list[steps[4]-1]="X"
#print board
print(" {} | {} | {} \n{}\n {} | {} | {} \n{}\n {} | {} | {} \n".format(board_list[0],
                                                                board_list[1],
                                                                board_list[2],
                                                                '-'*10,
                                                                board_list[3],
                                                                board_list[4],
                                                                board_list[5],
                                                                '-'*10,
                                                                board_list[6],
                                                                board_list[7],
                                                                board_list[8]))

#2.10 Time lag
time.sleep(2)

#2.11 Move 6 Player O
board_list[steps[5]-1]="O"
#print board
print(" {} | {} | {} \n{}\n {} | {} | {} \n{}\n {} | {} | {} \n".format(board_list[0],
                                                                board_list[1],
                                                                board_list[2],
                                                                '-'*10,
                                                                board_list[3],
                                                                board_list[4],
                                                                board_list[5],
                                                                '-'*10,
                                                                board_list[6],
                                                                board_list[7],
                                                                board_list[8]))

#2.8 Time lag
time.sleep(2)

#2.9 Move 7 Player X
board_list[steps[6]-1]="X"
#print board
print(" {} | {} | {} \n{}\n {} | {} | {} \n{}\n {} | {} | {} \n".format(board_list[0],
                                                                board_list[1],
                                                                board_list[2],
                                                                '-'*10,
                                                                board_list[3],
                                                                board_list[4],
                                                                board_list[5],
                                                                '-'*10,
                                                                board_list[6],
                                                                board_list[7],
                                                                board_list[8]))

#2.10 Time lag
time.sleep(2)

#2.11 Move 8 Player O
board_list[steps[7]-1]="O"
print(" {} | {} | {} \n{}\n {} | {} | {} \n{}\n {} | {} | {} \n".format(board_list[0],
                                                                board_list[1],
                                                                board_list[2],
                                                                '-'*10,
                                                                board_list[3],
                                                                board_list[4],
                                                                board_list[5],
                                                                '-'*10,
                                                                board_list[6],
                                                                board_list[7],
                                                                board_list[8]))

#2.8 Time lag
time.sleep(2)

#2.9 Move 9 Player X
board_list[steps[8]-1]="X"
#print board
print(" {} | {} | {} \n{}\n {} | {} | {} \n{}\n {} | {} | {} \n".format(board_list[0],
                                                                board_list[1],
                                                                board_list[2],
                                                                '-'*10,
                                                                board_list[3],
                                                                board_list[4],
                                                                board_list[5],
                                                                '-'*10,
                                                                board_list[6],
                                                                board_list[7],
                                                                board_list[8]))
# check for x
# check for row conditions about X
row0_win_x = board_list[0] == board_list[1] and board_list[1] == board_list[2] \
                and board_list[0]=="X"
row1_win_x = board_list[3] == board_list[4] and board_list[4] == board_list[5] \
                and board_list[3]=="X"
row2_win_x = board_list[6] == board_list[7] and board_list[7] == board_list[8] \
                and board_list[6]=="X"
# check for column conditions about X
col0_win_x = board_list[0] == board_list[3] and board_list[3] == board_list[6] \
                and board_list[0]=="X"
col1_win_x = board_list[1] == board_list[4] and board_list[4] == board_list[7] \
                and board_list[3]=="X"
col2_win_x = board_list[2] == board_list[5] and board_list[5] == board_list[8] \
                and board_list[6]=="X"
# check for diagonal conditions about X
diag0_win_x = board_list[0] == board_list[4] and board_list[4] == board_list[8] \
                and board_list[0]=="X"
diag1_win_x = board_list[2] == board_list[4] and board_list[4] == board_list[6] \
                and board_list[0]=="X"

# check for X win
x_win=row0_win_x or row1_win_x or row2_win_x or col0_win_x or col1_win_x or \
      col2_win_x or diag0_win_x or diag1_win_x

# check for O
# check for row conditions about O
row0_win_o = board_list[0] == board_list[1] and board_list[1] == board_list[2] \
                and board_list[0]=="O"
row1_win_o = board_list[3] == board_list[4] and board_list[4] == board_list[5] \
                and board_list[3]=="O"
row2_win_o = board_list[6] == board_list[7] and board_list[7] == board_list[8] \
                and board_list[6]=="O"
# check for column conditions about O
col0_win_o = board_list[0] == board_list[3] and board_list[3] == board_list[6] \
                and board_list[0]=="O"
col1_win_o = board_list[1] == board_list[4] and board_list[4] == board_list[7] \
                and board_list[1]=="O"
col2_win_o = board_list[2] == board_list[5] and board_list[5] == board_list[8] \
                and board_list[2]=="O"
# check for diagonal conditions about O
diag0_win_o = board_list[0] == board_list[4] and board_list[4] == board_list[8] \
                and board_list[0]=="O"
diag1_win_o = board_list[2] == board_list[4] and board_list[4] == board_list[6] \
                and board_list[0]=="O"
# check for X win
o_win=row0_win_o or row1_win_o or row2_win_o or col0_win_o or col1_win_o or \
      col2_win_o or diag0_win_o or diag1_win_o

winner_statement=(not o_win)*x_win*"Winner is X"+\
                 (not x_win)*o_win*"Winner is O"+\
                 x_win*o_win*"Both X & O are winners"+\
                 (not o_win)*(not x_win)*"No winner or loser"
print(winner_statement)

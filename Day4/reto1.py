import os
from Board import *

BOARD_LINES_LENGTH = 5


input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()

draw_line = lines[0]
board_list = []
for i in range(1, len(lines)):
    if lines[i] == '\n':
        ##Empty line -> New board
        new_board = Board(len(board_list))
        new_board.loadValuesFromLines(lines[i+1:i+BOARD_LINES_LENGTH + 1])
        new_board.print()
        board_list.append(new_board)
        i += BOARD_LINES_LENGTH

board_list[0].MarkValue(17)
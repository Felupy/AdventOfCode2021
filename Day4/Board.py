import os
import numpy as np

class Board:

    BOARD_ROWS = 5
    BOARD_COLS = 5
    matrix = []
    board_num = -1
    def __init__(self, _number) -> None:
        self.board_num = _number
        self.matrix = [[-1 for x in range(self.BOARD_COLS)] for y in range(self.BOARD_ROWS)] 
        

    def loadValuesFromLines(self, input_lines):
        row_idx = 0
        col_idx = 0
        for row in input_lines:
            row_values = row.split(' ')
            for v in row_values:
                if v != '':
                    self.matrix[row_idx][col_idx] = {v:False}
                    col_idx += 1
            row_idx += 1
            col_idx = 0

    def print(self):
        print("-------------------------------")
        for r in self.matrix:
            for c in r:
                print(c,end = " ")
            print()
        print("-------------------------------")

    def MarkValue(self, value):
        coords = zip(np.where(self.matrix == value))
        print(coords)

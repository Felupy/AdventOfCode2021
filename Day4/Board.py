import os

class Board:

    BOARD_ROWS = 5
    BOARD_COLS = 5
    matrix = []
    board_num = -1

    last_marked_num = -1

    bingo = False
    winning_row = []
    winning_col = []

    def __init__(self, _number) -> None:
        self.board_num = _number
        self.matrix = [[-1 for x in range(self.BOARD_COLS)] for y in range(self.BOARD_ROWS)] 
        

    def loadValuesFromLines(self, input_lines):
        row_idx = 0
        col_idx = 0
        for row in input_lines:
            row = row.strip()
            row_values = row.split(' ')
            for v in row_values:
                if v != '':
                    self.matrix[row_idx][col_idx] = (v,False)
                    col_idx += 1
            row_idx += 1
            col_idx = 0

    def print(self):
        print("-------------------------------")
        print("BOARD: ", self.board_num)
        print("-------------------------------")
        for r in self.matrix:
            row_str = ""
            for c in r:
                row_str = row_str + "{0:2}:{1}".format(c[0], c[1]) + " | "
            print(row_str)
            print("--------------------------------------------------------------------------------")
        print("-------------------------------")

    ### Marks value if exists and is not already marked.
    def MarkValue(self, value):

        #Stop marking element if already has bingo
        if self.bingo:
            return

        search_value = (value,False)
        #print(search_value)
        (founded, coord_x, coord_y) = self.FindInMatrix(search_value)
        if founded:
            self.matrix[coord_x][coord_y] = (value, True)
            self.last_marked_num = int(value)

    ### Returns 'True' if value exists and is marked, 'False' otherwise
    def isValueMarked(self, value):
        search_value = (value, True)
        (founded, coord_x, coord_y) = self.FindInMatrix(search_value)
        if founded:
            return True
        else:
            return False

    def calculateBingo(self):
        bingo_r = 0
        bingo_c = 0

        ##If already has bingo -> exit
        if self.bingo:
            return

        for i in range(self.BOARD_ROWS):
            for j in range(self.BOARD_COLS):
                cell = self.matrix[i][j]
                sts = cell[1]
                if sts:
                    bingo_c += 1

            if bingo_c == self.BOARD_COLS:
                self.bingo = True
                self.winning_row = self.matrix[i]
            else:
                bingo_c = 0

        for i in range(self.BOARD_COLS):
            for j in range(self.BOARD_ROWS):
                cell = self.matrix[j][i]
                sts = cell[1]
                if sts:
                    bingo_r += 1

            if bingo_r == self.BOARD_ROWS:
                self.bingo = True
                self.winning_col = self.matrix[i]
            else:
                bingo_r = 0

        
    def hasBingo(self):
        if not self.bingo:
            self.calculateBingo()
        return self.bingo

    def sumWinnerLine(self):
        if not self.bingo:
            return -1

        
        if self.winning_col:
            line = self.winning_col
        if self.winning_row:
            line = self.winning_row
        
        line_sum = 0
        for tup in line:
            print(tup)
            line_sum += int(tup[0])

        return line_sum

    def getFinalScore(self):
        unmarked_sum = 0
        
        for r in self.matrix:
            for c in r:
                if not c[1]:
                    unmarked_sum += int(c[0])


        score = unmarked_sum * self.last_marked_num

        return score

    #### Tools ####
    def FindInMatrix(self, element):
        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == element:
                    return (True, i, j)
                
        return (False, -1, -1)

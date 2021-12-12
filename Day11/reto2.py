import os
import numpy as np

FLASH_LEVEL = 10
MAX_STEPS = 1000

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

### class ###

##### FUNCTIONS #####
def octopus_flash(matrix, x, y, control_matrix):

    if matrix[x][y] >= FLASH_LEVEL and control_matrix[x][y] == False:
        control_matrix[x][y] = True
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < matrix.shape[0] and j >= 0 and j < matrix.shape[1]:
                        matrix[i][j] += 1
                        octopus_flash(matrix, i, j, control_matrix)

##### MAIN #####

lines = f.readlines()

matrix = []
for line in lines:
    line = line.strip()
    line_array = []
    for c in line:
        line_array.append(int(c))
    matrix.append(line_array)
    print(line_array)

total_octopus_flases = 0
matrix = np.array(matrix)
all_octopus_flashed = (False,0)

for i in range(MAX_STEPS):
    control_matrix =  [[False for x in range(matrix.shape[0])] for y in range(matrix.shape[1])] 

    # 1. Increase level by 1
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            matrix[x][y] += 1
    
    # 2. Flash and increment surrounding octopus levels
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            octopus_flash(matrix, x, y, control_matrix)

    # 3. After falshing return flash level to 0
    matrix_sum = 0
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if matrix[x][y] >= FLASH_LEVEL:
                total_octopus_flases += 1
                matrix[x][y] = 0
            matrix_sum += matrix[x][y] 

    # 4. Check if all octopus have flash
    if matrix_sum == 0:
        all_octopus_flashed = (True,i+1)
        break;
    if (i < 11):
        print("After step ", i + 1)
        print(matrix)
print("#Flash: ", total_octopus_flases)
print("Sum: ", matrix_sum)
print ("Iteration: ", all_octopus_flashed[1])
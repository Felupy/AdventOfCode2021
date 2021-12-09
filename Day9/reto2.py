import os

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from math import ceil

from numpy.core.numeric import binary_repr

#### FUNCTIONS #####



MAX = 100
#Point is tuple for a coordinate on a 2D array: (x,y)
def isLocalMin(matrix, x, y):
    actual_value = matrix[x,y]
    local_x_min = isLocalMinX(matrix, x, y)
    local_y_min = isLocalMinY(matrix, x, y)

    if local_x_min and local_y_min:
        return (True, actual_value)
        
    return (False, -1)

def isLocalMinX(matrix, x, y):
    max_array_x = matrix.shape[0] - 1
    actual_value = matrix[x,y]

    if x > 0 and x < max_array_x:
        left_value = matrix[x-1][y]
        right_value = matrix[x+1][y]
        return  (actual_value < left_value and actual_value < right_value)
    else:
        if x == 0:
            right_value = matrix[x+1][y]
            return actual_value < right_value
        if x == max_array_x:
            left_value = matrix[x-1][y]
            return actual_value < left_value



def isLocalMinY(matrix, x, y):
    max_array_y = matrix.shape[1] - 1
    actual_value = matrix[x,y]

    if y > 0 and y < max_array_y:
        top_value = matrix[x][y - 1]
        bot_value = matrix[x][y + 1]
        return  (actual_value < top_value and actual_value < bot_value)
    else:
        if y == 0:
            bot_value = matrix[x][y + 1]
            return actual_value < bot_value
        if y ==  max_array_y:
            top_value = matrix[x][y - 1]
            return actual_value < top_value


def findBasin(marked_matrix, matrix, value, coords):
    max_array_y = matrix.shape[1] - 1
    max_array_x = matrix.shape[0] - 1
    STOP_VALUE = 9
    y = coords[1]
    x = coords[0]

    basin_value = 1

    if value == STOP_VALUE:
        return 0

    if marked_matrix[x,y] == -1:
        return 0

    marked_matrix[x][y] = -1

    if x > 0 and x < max_array_x:
        if y > 0 and y < max_array_y:
            left_value = matrix[x][y - 1]
            right_value = matrix[x][y + 1]
            top_value = matrix[x - 1][y]
            bot_value = matrix[x + 1][y]
            if value < left_value:
                basin_value += findBasin(marked_matrix,matrix, left_value, (x, y - 1))
            if value < right_value:
                basin_value += findBasin(marked_matrix,matrix, right_value, (x, y + 1))
            if value < top_value:
                basin_value += findBasin(marked_matrix,matrix, top_value, (x -1, y))
            if value < bot_value:
                basin_value += findBasin(marked_matrix,matrix, bot_value, (x + 1, y))
        else:
            if y == 0:
                top_value = matrix[x - 1][y]
                right_value = matrix[x][y + 1]
                bot_value = matrix[x + 1][y]
                if value < top_value:
                    basin_value += findBasin(marked_matrix,matrix,top_value, (x -1, y))
                if value < right_value:
                    basin_value += findBasin(marked_matrix,matrix, right_value, (x, y + 1))
                if value < bot_value:
                    basin_value += findBasin(marked_matrix,matrix, bot_value, (x + 1, y))
            if y == max_array_y:
                top_value = matrix[x - 1][y]
                left_value = matrix[x][y - 1]
                bot_value = matrix[x + 1][y]
                if value < top_value:
                    basin_value += findBasin(marked_matrix,matrix, top_value, (x -1, y))
                if value < left_value:
                    basin_value += findBasin(marked_matrix,matrix, left_value, (x, y - 1))
                if value < bot_value:
                    basin_value += findBasin(marked_matrix,matrix, bot_value, (x + 1, y))
    else:
        if x == 0:
            if y > 0 and y < max_array_y:
                left_value = matrix[x][y - 1]
                right_value = matrix[x][y + 1]
                bot_value = matrix[x + 1][y]
                if value < left_value:
                    basin_value += findBasin(marked_matrix,matrix, left_value, (x, y - 1))
                if value < right_value:
                    basin_value += findBasin(marked_matrix,matrix, right_value, (x, y + 1))
                if value < bot_value:
                    basin_value += findBasin(marked_matrix,matrix, bot_value, (x + 1, y))
            else:
                if y == 0:
                    right_value = matrix[x][y + 1]
                    bot_value =  matrix[x + 1][y]
                    if value < right_value:
                        basin_value += findBasin(marked_matrix,matrix, right_value, (x, y + 1))
                    if value < bot_value:
                        basin_value += findBasin(marked_matrix,matrix, bot_value, (x + 1, y))
                if y == max_array_y:
                    left_value = matrix[x][y - 1]
                    bot_value =  matrix[x + 1][y]
                    if value < left_value:
                        basin_value += findBasin(marked_matrix,matrix, left_value, (x, y - 1))
                    if value < bot_value:
                        basin_value += findBasin(marked_matrix,matrix, bot_value, (x + 1, y))

        if x == max_array_x:
            if y > 0 and y < max_array_y:
                left_value = matrix[x][y - 1]
                top_value = matrix[x - 1][y]
                right_value = matrix[x][y + 1]
                if value < left_value:
                    basin_value += findBasin(marked_matrix,matrix, left_value, (x, y - 1))
                if value < top_value:
                    basin_value += findBasin(marked_matrix,matrix, top_value, (x - 1, y))
                if value < right_value:
                    basin_value += findBasin(marked_matrix,matrix, right_value, (x, y + 1))
            else:
                if y == 0:
                    right_value = matrix[x][y + 1]
                    top_value = matrix[x - 1][y]
                    if value < right_value:
                        basin_value += findBasin(marked_matrix,matrix,right_value, (x, y + 1))
                    if value < top_value:
                        basin_value += findBasin(marked_matrix,matrix, top_value, (x - 1, y))
                if y == max_array_y:
                    left_value = matrix[x][y - 1]
                    top_value = matrix[x - 1][y]
                    if value < left_value:
                        basin_value += findBasin(marked_matrix,matrix, left_value, (x, y - 1))
                    if value < top_value:
                        basin_value += findBasin(marked_matrix,matrix, top_value, (x - 1, y))


    return basin_value




#### MAIN ####


input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()

matrix = []
for line in lines:
    line = line.strip()
    matrix.append([int(line[i]) for i in range(len(line))])





matrix = np.array(matrix)
local_mins_coords = []
local_mins = []
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        isMin, value = isLocalMin(matrix, i, j)
        if isMin:
            local_mins_coords.append((i, j))
            local_mins.append(value)
        
print (local_mins)

#find risk level
inital_risk = 1
total_risk = 0
for value in local_mins:
    total_risk += inital_risk + value
print ("Total risk: ",total_risk)

basin_list = []
for i in range(len(local_mins)):
    marked_matrix = matrix.copy()
    basin_list.append(findBasin(marked_matrix, matrix, local_mins[i], local_mins_coords[i]))

print(basin_list)

basin_list.sort(reverse=True)

print("Ordered list: ", basin_list)

product = basin_list[0] * basin_list[1] * basin_list[2]
print("Result: ", product)








#PLOTTING
plt.figure()
plt.title('Matrix as 2d heat map')
legend = plt.imshow(matrix)
plt.colorbar(legend)
plt.show()
print(matrix.shape)
print(matrix)
x, y = np.meshgrid(range(matrix.shape[0]), range(matrix.shape[1]))
matrix = matrix.transpose()

# show hight map in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, matrix)
plt.title('Matrix as 3d height map')
plt.show()



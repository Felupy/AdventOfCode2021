import os


input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()


#table
MAX_ROWS = 1000
MAX_COLS = 1000
table =  [[0 for x in range(MAX_ROWS)] for y in range(MAX_COLS)] 

#Paint lines
for line in lines:
    line = line.strip()
    orig, dest = line.split("->")
    orig_y = int(orig.split(",")[0]) #x1
    orig_x = int(orig.split(",")[1]) #x2
    dest_y = int(dest.split(",")[0]) #y1
    dest_x = int(dest.split(",")[1]) #y2

    idx_start = 0
    idx_end = 0
    #Only straigth lines
    if orig_x == dest_x:
        if orig_y >= dest_y:
            idx_start = dest_y
            idx_end = orig_y
        else:
            idx_start = orig_y
            idx_end = dest_y
        for i in range (idx_start, idx_end+1):
            table[orig_x][i] += 1

    if orig_y == dest_y:
        if orig_x >= dest_x:
            idx_start = dest_x
            idx_end = orig_x
        else:
            idx_start = orig_x
            idx_end = dest_x
        for i in range (idx_start, idx_end+1):
            table[i][orig_y] += 1

    #Diagonal lines
    dist_x = dest_x - orig_x
    dist_y = dest_y - orig_y
    if abs(dist_x) == abs(dist_y):
        print("Diagonal: ", orig, " -> ", dest, " | Distancia: ", dist_x, " - ", dist_y)
        ejex=-1
        ejey=-1
        counter = 0
        for i in range(abs(dist_x) + 1): 
            if (dist_x > 0 and dist_y > 0):
                #print("Diagonal UP+LEFT:", orig, " -> ", dest)
                table[orig_x + i][orig_y + i] += 1 
            if (dist_x > 0 and dist_y < 0):
                #print("Diagonal DOWN+LEFT:", orig, " -> ", dest)
                table[orig_x + i][orig_y - i] += 1 
            if (dist_x < 0 and dist_y > 0):
                #print("Diagonal UP+RIGHT:", orig, " -> ", dest)
                table[orig_x - i][orig_y + i] += 1 
            if (dist_x < 0 and dist_y < 0):
                #print("Diagonal DOWN+RIGHT:", orig, " -> ", dest)
                table[orig_x - i][orig_y - i] += 1 


    

#Generate output
overlap_lines_count = 0
output_file = "output.txt"
output_lines = []
for i in range(MAX_ROWS):
    row_str = ""
    for j in range(MAX_COLS):
        row_str = row_str + str(table[i][j]) +  " "
        if table[i][j] >= 2:
            overlap_lines_count+=1
    output_lines.append(row_str + "\n")

fo = open(output_file, "w")
fo.writelines(output_lines)
print("Overlaps: ", overlap_lines_count)

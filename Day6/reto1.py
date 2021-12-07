import os

MAX_DAYS = 80
POPULATE_TIME = 6
POPULATE_OFFSET = 2

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()

lanternfishs = [int(x) for x in lines[0].split(',')]
print("Inital state: ", lanternfishs)

for day in range(MAX_DAYS):
    for i in range(len(lanternfishs)):
        lanternfishs[i] -= 1

        if (lanternfishs[i] == -1):
            #Reset and spawn new
            lanternfishs[i] = POPULATE_TIME
            lanternfishs.append(POPULATE_TIME + POPULATE_OFFSET)
        
    print("After ", day + 1, " day: ", lanternfishs)

lanternfishs_count = len(lanternfishs)

print("#Lanternfish: ", lanternfishs_count)

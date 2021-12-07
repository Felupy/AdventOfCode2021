import os
import numpy as np
import matplotlib.pyplot as plt
MAX_DAYS = 130
POPULATE_TIME = 6
POPULATE_OFFSET = 2

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()

lanternfishs = [int(x) for x in lines[0].split(',')]
lanternfishs_ori = [int(x) for x in lines[2].split(',')]
#lanternfishs_full = [int(x) for x in lines[1].split(',')]
unos_ori = lanternfishs_ori.count(1)
doses_ori = lanternfishs_ori.count(2)
treses_ori = lanternfishs_ori.count(3)
cuatros_ori = lanternfishs_ori.count(4)
cincos_ori = lanternfishs_ori.count(5)

initial_len = len(lanternfishs)
len_by_days = []
total_at_days = {}
print("Inital state: ", lanternfishs)
for day in range(MAX_DAYS):
    # print("Day: ", day)
    for i in range(len(lanternfishs)):
        lanternfishs[i] -= 1

        if (lanternfishs[i] == -1):
            #Reset and spawn new
            lanternfishs[i] = POPULATE_TIME
            lanternfishs.append(POPULATE_TIME + POPULATE_OFFSET)
    
    len_by_days.append(len(lanternfishs))

    if day > 119  and day < 131:
        total_at_days[day] = lanternfishs.copy()


    # print("After ", day + 1, " day: ", lanternfishs)

lanternfishs_count = len(lanternfishs)

print("#Lanternfish: ", lanternfishs_count)
# result = unos*day256 + doses*day255 + treses*day254 + cuatros*day253 + cincos*day252
# print("Cheat result: ", result)
center_num = 127
unos256 = unos_ori * (                  
                    (total_at_days[center_num].count(0) * len(total_at_days[center_num + 1])) +
                    (total_at_days[center_num].count(1) * len(total_at_days[center_num])) + 
                    (total_at_days[center_num].count(2) * len(total_at_days[center_num - 1])) +
                    (total_at_days[center_num].count(3) * len(total_at_days[center_num - 2])) +
                    (total_at_days[center_num].count(4) * len(total_at_days[center_num - 3])) +
                    (total_at_days[center_num].count(5) * len(total_at_days[center_num - 4])) +
                    (total_at_days[center_num].count(6) * len(total_at_days[center_num - 5])) +
                    (total_at_days[center_num].count(7) * len(total_at_days[center_num - 6])) +
                    (total_at_days[center_num].count(8) * len(total_at_days[center_num - 7])) 
                )

doses256 = doses_ori * (                  
                    (total_at_days[center_num - 1].count(0) * len(total_at_days[center_num + 1])) +
                    (total_at_days[center_num - 1].count(1) * len(total_at_days[center_num])) + 
                    (total_at_days[center_num - 1].count(2) * len(total_at_days[center_num - 1])) +
                    (total_at_days[center_num - 1].count(3) * len(total_at_days[center_num - 2])) +
                    (total_at_days[center_num - 1].count(4) * len(total_at_days[center_num - 3])) +
                    (total_at_days[center_num - 1].count(5) * len(total_at_days[center_num - 4])) +
                    (total_at_days[center_num - 1].count(6) * len(total_at_days[center_num - 5])) +
                    (total_at_days[center_num - 1].count(7) * len(total_at_days[center_num - 6])) +
                    (total_at_days[center_num - 1].count(8) * len(total_at_days[center_num - 7])) 
                )

treses256 = treses_ori * (                  
                    (total_at_days[center_num- 2].count(0) * len(total_at_days[center_num + 1])) +
                    (total_at_days[center_num- 2].count(1) * len(total_at_days[center_num])) + 
                    (total_at_days[center_num- 2].count(2) * len(total_at_days[center_num - 1])) +
                    (total_at_days[center_num- 2].count(3) * len(total_at_days[center_num - 2])) +
                    (total_at_days[center_num- 2].count(4) * len(total_at_days[center_num - 3])) +
                    (total_at_days[center_num- 2].count(5) * len(total_at_days[center_num - 4])) +
                    (total_at_days[center_num- 2].count(6) * len(total_at_days[center_num - 5])) +
                    (total_at_days[center_num- 2].count(7) * len(total_at_days[center_num - 6])) +
                    (total_at_days[center_num- 2].count(8) * len(total_at_days[center_num - 7])) 
                )

cuatros256 = cuatros_ori * (                  
                    (total_at_days[center_num - 3].count(0) * len(total_at_days[center_num + 1])) +
                    (total_at_days[center_num - 3].count(1) * len(total_at_days[center_num])) + 
                    (total_at_days[center_num - 3].count(2) * len(total_at_days[center_num - 1])) +
                    (total_at_days[center_num - 3].count(3) * len(total_at_days[center_num - 2])) +
                    (total_at_days[center_num - 3].count(4) * len(total_at_days[center_num - 3])) +
                    (total_at_days[center_num - 3].count(5) * len(total_at_days[center_num - 4])) +
                    (total_at_days[center_num - 3].count(6) * len(total_at_days[center_num - 5])) +
                    (total_at_days[center_num - 3].count(7) * len(total_at_days[center_num - 6])) +
                    (total_at_days[center_num - 3].count(8) * len(total_at_days[center_num - 7])) 
                )

cincos256 = cincos_ori * (                  
                    (total_at_days[center_num - 4].count(0) * len(total_at_days[center_num + 1])) +
                    (total_at_days[center_num - 4].count(1) * len(total_at_days[center_num])) + 
                    (total_at_days[center_num - 4].count(2) * len(total_at_days[center_num - 1])) +
                    (total_at_days[center_num - 4].count(3) * len(total_at_days[center_num - 2])) +
                    (total_at_days[center_num - 4].count(4) * len(total_at_days[center_num - 3])) +
                    (total_at_days[center_num - 4].count(5) * len(total_at_days[center_num - 4])) +
                    (total_at_days[center_num - 4].count(6) * len(total_at_days[center_num - 5])) +
                    (total_at_days[center_num - 4].count(7) * len(total_at_days[center_num - 6])) +
                    (total_at_days[center_num - 4].count(8) * len(total_at_days[center_num - 7])) 
                )

total = unos256 + doses256 + treses256 + cuatros256 + cincos256
print("Total: ", total)
difference = 26984457539 - total
print("Diffrence: ", difference)



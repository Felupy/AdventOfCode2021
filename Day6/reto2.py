import os
import numpy as np
import matplotlib.pyplot as plt
MAX_DAYS = 128
POPULATE_TIME = 6
POPULATE_OFFSET = 2

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()

lanternfishs = [int(x) for x in lines[0].split(',')]
# lanternfishs_full = [int(x) for x in lines[1].split(',')]
# unos = lanternfishs_full.count(1)
# doses = lanternfishs_full.count(2)
# treses = lanternfishs_full.count(3)
# cuatros = lanternfishs_full.count(4)
# cincos = lanternfishs_full.count(5)

initial_len = len(lanternfishs)
len_by_days = []
print("Inital state: ", lanternfishs)
# dia256 = 0
# dia255 = 0
# dia254 = 0
# dia253 = 0
# dia252 = 0
for day in range(MAX_DAYS):
    # print("Day: ", day)
    for i in range(len(lanternfishs)):
        lanternfishs[i] -= 1

        if (lanternfishs[i] == -1):
            #Reset and spawn new
            lanternfishs[i] = POPULATE_TIME
            lanternfishs.append(POPULATE_TIME + POPULATE_OFFSET)
    
    len_by_days.append(len(lanternfishs))

    # if (day == 255):
    #     day256 = len(lanternfishs)
    # if (day == 254):
    #     day255 = len(lanternfishs)
    # if (day == 253):
    #     day254 = len(lanternfishs)
    # if (day == 252):
    #     day253 = len(lanternfishs)
    # if (day == 251):
    #     day252 = len(lanternfishs)

    # print("After ", day + 1, " day: ", lanternfishs)

lanternfishs_count = len(lanternfishs)

print("#Lanternfish: ", lanternfishs_count)
print("Ceros: ", lanternfishs.count(0))
# result = unos*day256 + doses*day255 + treses*day254 + cuatros*day253 + cincos*day252
# print("Cheat result: ", result)

days = [x for x in range(MAX_DAYS)]
x = np.array(days)
y = np.array(len_by_days)
print("X Len: " , len(x), " | ", x)
print("Y Len: " , len(y), " | ", y)
p = np.polyfit(x,np.log(y), 1, w=np.sqrt(y))

ecuacion_str = "".format("y={0} + {1}*x + {1}*x^2", p[1], p[0])
y_calc = np.exp(p[0]*x) * np.exp(p[1])
print("Curve: ", ecuacion_str)
#plot
plt.plot(x, y, 'ko')
plt.plot(x, y_calc, 'b')
plt.show()





x_calc = 256
y_new = np.exp(p[0]*x_calc) * np.exp(p[1])
difference = 26984457539 - y_new
print("Result:", y_new)
print("Diffrence: ", difference)


import sys
import os

#definitions
MAX_MEAS_LENGTH = 3

saved_values = []


#functions
def process_3_sum():
    print(saved_values)
    return sum(saved_values)


#MAIN

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")



lastSuma = -1
increased_counter= 0
decreased_counter= 0
nochange_counter= 0
lines = f.readlines()

for line in lines:
    value = int(line)

    #Manage queue
    if (len(saved_values) < MAX_MEAS_LENGTH):
        saved_values.append(value)
    else:
        saved_values.pop(0)
        saved_values.append(value)

    #Sum calculation
    if (len(saved_values) < MAX_MEAS_LENGTH):
        print("No enougth data yet")
    else:
        suma = process_3_sum()

        #Increased decision
        if (lastSuma == -1):
            lastSuma = suma
            print(lastSuma, " N/A")
        else:
            if (suma > lastSuma):
                increased_counter+=1
                print("Suma: ", suma, " increased")
            elif (suma == lastSuma):
                nochange_counter+=1
                print("Suma: ", suma, " no change")
            else:
                decreased_counter+=1
                print("Suma: ", suma, " decreased")

            lastSuma = suma



print("Output: ",increased_counter, " increased times")
print("Output: ",decreased_counter, " decreased times")
print("Total lines: ", len(lines))
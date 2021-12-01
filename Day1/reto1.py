import sys
import os


input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lastvalue = -1
increased_counter= 0
decreased_counter= 0
lines = f.readlines()
for line in lines:
    value = int(line)
    if (lastvalue == -1):
        ##Initial case
        lastvalue = value
        print(lastvalue, " N/A")
    else:
        if value > lastvalue:
            increased_counter+=1
            print(value, " increased", )
        else:
            decreased_counter+=1
            print(value, " decreased")
    lastvalue = value

print("Output: ",increased_counter, " increased times")
print("Output: ",decreased_counter, " decreased times")
print("Total lines: ", len(lines))
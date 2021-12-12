import os

ONE_LENTH = 2
FOUR_LENGTH = 4
SEVEN_LENGTH = 3
EIGTH_LENGTH = 7

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()

total_aperances = 0
for line in lines:
    line = line.strip()
    input_digits, output_digits = line.split('|')
    
    for digit in output_digits.split():
        digit_len = len(digit)
        if digit_len == ONE_LENTH or digit_len == FOUR_LENGTH or digit_len == SEVEN_LENGTH or digit_len == EIGTH_LENGTH:
            total_aperances += 1

print("Total aperances: ", total_aperances)
import os

total_horizontal_pos = 0
total_depth = 0

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()
for line in lines:
    (direction, value_str) = line.split(' ')
    amount = int(value_str)
    if direction == "forward":
        total_horizontal_pos += amount
    if direction == "down":
        total_depth += amount
    if direction == "up":
        total_depth -= amount


product = total_horizontal_pos * total_depth

print("Output:", product)
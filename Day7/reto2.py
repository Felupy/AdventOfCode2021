import os




input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()

crabs_fuel = [int(x) for x in lines[0].split(',')]

min_value = min(crabs_fuel)
max_value = max(crabs_fuel)

fuel_needed_by_pos = []
for i in range(min_value, max_value):
    fuel_needed = 0
    for value in crabs_fuel:
        distance_to_target_value = abs(i-value)
        fuel_consumption = 1
        for j in range(distance_to_target_value):
            fuel_needed += fuel_consumption + j
            
    fuel_needed_by_pos.append(fuel_needed)    

min_fuel_needed = min(fuel_needed_by_pos)
print("Min fuel needed: %d" % min_fuel_needed)
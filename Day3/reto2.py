import os


### Retruns: The most common bit in this position (1 or)
def CalculateMostCommonBitByPos(input_data, bit_pos):
    one_count = 0
    zero_count = 0
    for value in input_data:
        if value[bit_pos] != '\n':
            if value[bit_pos] == '1':
                one_count+=1
            else:
                zero_count+=1
    
    return one_count >= zero_count






#### MAIN ####

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()

#Populate dictionary
bit_dict = {}
for line in lines:
    for i in range(0,len(line)):
        bit_key = "bit" + str(i)
        if line[i] != "\n":
            if bit_key in bit_dict.keys():
                bit_dict[bit_key].append(int(line[i]))
            else:
                bit_dict[bit_key] = []
                bit_dict[bit_key].append(int(line[i]))

#Filter by bit criteria
oxygen_original_list = lines.copy()
co2_original_list = lines.copy()
data_len = len(lines[0])

for i in range(0,data_len-1):
    oxygen_crit = CalculateMostCommonBitByPos(oxygen_original_list, i)
    co2_crit = not CalculateMostCommonBitByPos(co2_original_list, i)

    if len(oxygen_original_list) > 1:
        oxygen_filtered_data = []
        for line in oxygen_original_list:
            if int(line[i]) == oxygen_crit:
                oxygen_filtered_data.append(line)

    if len(co2_original_list) > 1:
        co2_filtered_data = []
        for line in co2_original_list:
            if int(line[i]) == co2_crit:
                co2_filtered_data.append(line);

    oxygen_original_list = oxygen_filtered_data
    co2_original_list = co2_filtered_data
    print("-------------------------------------")
    print(oxygen_original_list)
    print(co2_original_list)
    print("-------------------------------------")


oxygen_rating = int(oxygen_original_list[0], 2)
co2_rating = int(co2_original_list[0], 2)
life_support = oxygen_rating * co2_rating

print("Oxygen: ", oxygen_rating)
print("Co2: ", co2_rating)
print("Life Support: ", life_support);
   






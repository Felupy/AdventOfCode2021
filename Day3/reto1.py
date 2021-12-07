import os



input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()


bit_dict = {}
for line in lines:
    for i in range(0,len(line)):
        bit_key = "bit" + str(i)
        if line[i] is not "\n":
            if bit_key in bit_dict.keys():
                bit_dict[bit_key].append(int(line[i]))
            else:
                bit_dict[bit_key] = []
                bit_dict[bit_key].append(int(line[i]))

most_common = []
less_common = []

for key in bit_dict.keys():
    one_count = 0
    zero_count = 0
    for value in bit_dict[key]:
        if value:
            one_count+=1
        else:
            zero_count+=1
    
    if one_count >= zero_count:
        most_common.append("1")
        less_common.append("0")
    else:
        most_common.append("0")
        less_common.append("1")

print(most_common)
print(less_common)
gamma_rate = int("".join(most_common), 2)
epsilon_rate = int("".join(less_common), 2)
power = gamma_rate * epsilon_rate;

print("Gamma:\t\t", gamma_rate)
print("Epsilon:\t", epsilon_rate)
print("Power consumption:", power)
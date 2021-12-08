import os

ONE_LENTH = 2
FOUR_LENGTH = 4
SEVEN_LENGTH = 3
EIGTH_LENGTH = 7

DEF_A_TIMES = 8
DEF_B_TIMES = 6
DEF_C_TIMES = 8
DEF_D_TIMES = 7
DEF_E_TIMES = 4
DEF_F_TIMES = 9
DEF_G_TIMES = 7

def IndentifyValue(sum_value):
    value = -1
    try:
        values_total_sum = {42: 0 , 17:1, 34:2, 39:3, 30:4, 37:5, 41:6, 25:7, 49:8, 45:9}
        value = values_total_sum[sum_value]
    except:
        print("Sum: ", sum_value, " not found!")
        value = -2
    return value

def Indentify(input_str_values, output_str_values):

    char_count_dict = { "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0}
    char = ["a", "b", "c", "d", "e", "f", "g"]   
    eigth_digit_str = ""
    for str_value in input_str_values:
        if len(str_value) == EIGTH_LENGTH:
                eigth_digit_str = str_value
        for c in char:
            if c in str_value:
                char_count_dict[c] += 1
    
    print(char_count_dict)

    new_char_weigths_dict = {}
    print("Eigth: ", eigth_digit_str)
    for i in range(len(eigth_digit_str)):
        new_char_weigths_dict[eigth_digit_str[i]] = char_count_dict[eigth_digit_str[i]]


    
    row_str = []
    values = []
    for str_value in input_str_values:
        value = 0
        for c in str_value:
            value += new_char_weigths_dict[c]
        # row_str.append(value)
        values.append(IndentifyValue(value))
        
    # print(row_str)
    print(values)

    #output
    output_values = []
    for str_value in output_str_values:
        value = 0
        for c in str_value:
            value += new_char_weigths_dict[c]
        # row_str.append(value)
        output_values.append(str(IndentifyValue(value)))

    str_output = "".join(output_values)
    output = int(str_output)
    print("Output: ", output)

    return output

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")

lines = f.readlines()

output_values = []
for line in lines:
    line = line.strip()
    input_digits, output_digits = line.split('|')
    input_str_values = [i for i in input_digits.split()]
    output_str_values = [o for o in output_digits.split()]
    
    output_values.append(Indentify(input_str_values, output_str_values))



print("Total output: ", sum(output_values))
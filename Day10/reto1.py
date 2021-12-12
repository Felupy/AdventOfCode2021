import os

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")


lines = f.readlines()

open_chars = [ "(", "[", "{", "<" ]
close_chars = [ ")", "]", "}", ">" ]
char_values_dict = { ")":3, "]":57, "}":1197, ">":25137 }

opened_chunck_stack = []
last_open_char = ""
first_corrupted_character_list = []
for i in range(len(lines)):
    line = lines[i]
    for c in line:
        if c in open_chars:
            last_open_char = c
            opened_chunck_stack.append(c)
        if c in close_chars:
            open_char_pos = open_chars.index(last_open_char)
            close_char_pos = close_chars.index(c)
            if (open_char_pos == close_char_pos):
                #Correct chunk closure
                opened_chunck_stack.pop(-1)
                last_open_char = opened_chunck_stack[-1]
            else:
                #Incorrect chunk closure
                first_corrupted_character_list.append((i, c))
                break

print("Num corrupted lines: ", len(first_corrupted_character_list))
print(first_corrupted_character_list)

syntax_error_score = 0
for value in first_corrupted_character_list:
    c = value[1]
    syntax_error_score += char_values_dict[c]

print("Syntax error score: ", syntax_error_score)

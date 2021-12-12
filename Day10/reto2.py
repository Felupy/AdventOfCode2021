import os

input_file = "input.txt"
cwd = os.getcwd()
input_file_path = cwd + "\\" + input_file
print(input_file_path)
f = open(input_file_path, "r")


lines = f.readlines()

open_chars = [ "(", "[", "{", "<" ]
close_chars = [ ")", "]", "}", ">" ]
char_corrupted_values_dict = { ")":3, "]":57, "}":1197, ">":25137 }
char_missing_values_dict = { ")":1, "]":2, "}":3, ">":4 }
TOTAL_SCORE_MULTIPLIER = 5


last_open_char = ""
first_corrupted_character_list = []
missing_characters_list = []
for i in range(len(lines)):
    line = lines[i]
    line = line.strip()
    opened_chunck_stack = []
    corrupted_char_found = False
    for c in line:
        if c in open_chars:
            last_open_char = c
            opened_chunck_stack.append(last_open_char)
        if c in close_chars:
            open_char_pos = open_chars.index(last_open_char)
            close_char_pos = close_chars.index(c)
            if (open_char_pos == close_char_pos):
                #Correct chunk closure
                opened_chunck_stack.pop(-1)
                if len(opened_chunck_stack) > 0:
                    last_open_char = opened_chunck_stack[-1]
                else:
                    last_open_char = ""
            else:
                #Incorrect chunk closure
                first_corrupted_character_list.append((i, c))
                corrupted_char_found = True
                break
    #Find missing characters
    if len(opened_chunck_stack) > 0 and not corrupted_char_found:
        close_chars_missing = []
        opened_chunck_stack.reverse()
        for open_char in opened_chunck_stack:
            open_char_pos = open_chars.index(open_char)
            close_char = close_chars[open_char_pos]
            close_chars_missing.append(close_char)
        missing_characters_list.append((i, close_chars_missing))

print("Num corrupted lines: ", len(first_corrupted_character_list))
print(first_corrupted_character_list)
print("Num missing lines: ", len(missing_characters_list))
print(missing_characters_list)


syntax_error_score = 0
for value in first_corrupted_character_list:
    c = value[1]
    syntax_error_score += char_corrupted_values_dict[c]
print("Syntax error score: ", syntax_error_score)

missing_chars_score_list = []
for tuple in missing_characters_list:
    total_score = 0
    for c in tuple[1]:
        total_score = total_score * TOTAL_SCORE_MULTIPLIER + char_missing_values_dict[c]
    missing_chars_score_list.append(total_score)

missing_chars_score_list.sort()
middle_score = missing_chars_score_list[int(len(missing_chars_score_list)/2)]
print(missing_chars_score_list)
print("Middle score: ", middle_score)
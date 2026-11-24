import sys
import os


args = sys.argv  # we get the list of arguments from command line
# print('Arguments:', args)
if len(args) == 3:
    if args[1] == '-dataType':
        if args[2] in ['long', 'line', 'word']:
            data_type = args[2]


# reading input

list_of_lines = []
while True:
    try:
        list_of_lines.append(input())
    except EOFError:
        break
# print(list_of_lines)

match data_type:
    case 'long':
        total_numbers = 0
        the_greatest_number = None
        the_greatest_number_count = 0
        for line in list_of_lines:
            numbers_list = line.split()
            for number in numbers_list:
                number = int(number)
                total_numbers += 1
                if the_greatest_number is None or number > the_greatest_number:
                    the_greatest_number = number
                    the_greatest_number_count = 1
                elif number == the_greatest_number:
                    the_greatest_number_count += 1
        print(f'Total numbers: {total_numbers}.')
        print(f'The greatest number: {the_greatest_number} ({the_greatest_number_count} time(s), {int(the_greatest_number_count/total_numbers * 100)}%).')

    case 'line':
        total_lines = len(list_of_lines)
        the_longest_line_number = 0
        the_longest_line_string_list = []
        for line in list_of_lines:
            if not the_longest_line_string_list or len(line) > len(the_longest_line_string_list[0]):
                the_longest_line_string_list = []
                the_longest_line_string_list.append(line)
                the_longest_line_number = 1
            elif line in the_longest_line_string_list:
                the_longest_line_number += 1
            elif len(line) == len(the_longest_line_string_list[0]) and line > the_longest_line_string_list[0]:
                the_longest_line_string_list.append(line)
                the_longest_line_number = 1
        print(f'Total lines: {total_lines}.')
        print(f'The longest line:\n{the_longest_line_string_list[0]}')
        print(f'({the_longest_line_number} time(s), {the_longest_line_number/total_lines:.0%}).')
    case 'word':
        total_words = 0
        longest_word = ''
        longest_word_count = 0
        for line in list_of_lines:
            line_split = line.split()
            total_words += len(line_split)
            for word in line_split:
                if not longest_word or len(word) > len(longest_word):
                    longest_word = word
                    longest_word_count = 1
                elif word == longest_word:
                    longest_word_count += 1
        print(f'Total words: {total_words}.')
        print(f'The longest word: {longest_word} ({longest_word_count} time(s){longest_word_count/total_words:.0%}).')





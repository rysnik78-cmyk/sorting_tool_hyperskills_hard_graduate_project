import sys
import os


# parsing commands
args = sys.argv  # we get the list of arguments from command line
# print('Arguments:', args)
parameters = ['long', 'natural']

if '-sortingType' in args and 'byCount' in args:
    parameters[1] = 'byCount'
if '-dataType' in args:
    if 'long' in args:
        parameters[0] = 'long'
    if 'line' in args:
        parameters[0] = 'line'
    if 'word' in args:
        parameters[0] = 'word'



# reading input
list_of_lines = []
while True:
    try:
        list_of_lines.append(input())
    except EOFError:
        break
# print(list_of_lines)

match parameters[0], parameters[1]:
    case 'long', 'natural':
        # total_numbers = 0
        # the_greatest_number = None
        # the_greatest_number_count = 0
        # for line in list_of_lines:
        #     numbers_list = line.split()
        #     for number in numbers_list:
        #         number = int(number)
                # # total_numbers += 1
                # if the_greatest_number is None or number > the_greatest_number:
                #     the_greatest_number = number
                #     the_greatest_number_count = 1
                # elif number == the_greatest_number:
                #     the_greatest_number_count += 1
        # print(f'Total numbers: {total_numbers}.')
        # print(f'The greatest number: {the_greatest_number} ({the_greatest_number_count} time(s), {int(the_greatest_number_count/total_numbers * 100)}%).')
        list_of_integers = []
        for line in list_of_lines:
            line_split = line.split()
            list_of_integers.extend([int(x) for x in line_split])
        # print(list_of_integers)
        print(f'Total numbers: {len(list_of_integers)}.')

        sorted_list = sorted(list_of_integers)
        sorted_list_string = ''
        for number in sorted_list:
            sorted_list_string += ' ' + str(number)
        print(f'Sorted data:{sorted_list_string}')

    case 'line', 'natural':
        total_lines = len(list_of_lines)
        # the_longest_line_number = 0
        # the_longest_line_string_list = []
        # for line in list_of_lines:
        #     if not the_longest_line_string_list or len(line) > len(the_longest_line_string_list[0]):
        #         the_longest_line_string_list = []
        #         the_longest_line_string_list.append(line)
        #         the_longest_line_number = 1
        #     elif line in the_longest_line_string_list:
        #         the_longest_line_number += 1
        #     elif len(line) == len(the_longest_line_string_list[0]) and line > the_longest_line_string_list[0]:
        #         the_longest_line_string_list.append(line)
        #         the_longest_line_number = 1
        sorted_list = sorted(list_of_lines)

        print(f'Total lines: {total_lines}.')
        print('Sorted data:')
        for line in sorted_list:
            print(line)


        # print(f'The longest line:\n{the_longest_line_string_list[0]}')
        # print(f'({the_longest_line_number} time(s), {the_longest_line_number/total_lines:.0%}).')
    case 'word', 'natural':
        # total_words = 0
        # longest_word = ''
        # longest_word_count = 0
        list_of_words = []
        for line in list_of_lines:
            line_split = line.split()
            # total_words += len(line_split)
            for word in line_split:
                list_of_words.append(word)
        total_words = len(list_of_words)
                # if not longest_word or len(word) > len(longest_word):
                #     longest_word = word
                #     longest_word_count = 1
                # elif word == longest_word:
                #     longest_word_count += 1
        print(f'Total words: {total_words}.')
        sorted_list_of_words = sorted(list_of_words)
        sorted_list_string = ''
        for word in list_of_words:
            sorted_list_string += ' ' + word
        print(f'Sorted data:{sorted_list_string}')

    case 'long','byCount':
        list_of_integers = []
        dict_of_integers = {}
        for line in list_of_lines:
            line_split = line.split()
            list_of_integers.extend([int(x) for x in line_split])
        # print(list_of_integers)
        print(f'Total numbers: {len(list_of_integers)}.')
        for number in list_of_integers:
            if number not in dict_of_integers:
                dict_of_integers[number] = 1
            else:
                dict_of_integers[number] += 1
        # print(dict_of_integers)
        dict_of_integers_sorted = dict(sorted(dict_of_integers.items(), key=lambda item: item[0]))
        dict_of_integers_sorted = dict(sorted(dict_of_integers_sorted.items(), key=lambda item: item[1]))
        # print(dict_of_integers_sorted)
        for number, count in dict_of_integers_sorted.items():
            print(f'{number}: {count} time(s), {int(count/len(list_of_integers) * 100)}%')

    case 'word','byCount':
        # TODO finish this case
        list_of_words = []
        for line in list_of_lines:
            line_split = line.split()
            # total_words += len(line_split)
            for word in line_split:
                list_of_words.append(word)
        total_words = len(list_of_words)
        print(f'Total words: {total_words}.')
        word_dict = {}
        for word in list_of_words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        word_dict_sorted = dict(sorted(word_dict.items(), key=lambda item: item[1]))
        for word, count in word_dict_sorted.items():
            print(f'{word}: {count} time(s), {int(count/total_words * 100)}%')

    case 'line','byCount':
        total_lines = len(list_of_lines)
        line_dict = {}
        for line in list_of_lines:
            if line not in line_dict:
                line_dict[line] = 1
            else:
                line_dict[line] += 1
        line_dict_sorted = dict(sorted(line_dict.items(), key=lambda item: item[0]))
        line_dict_sorted = dict(sorted(line_dict_sorted.items(), key=lambda item: item[1]))

        print(f'Total lines: {total_lines}.')
        # print('Sorted data:')
        for line in line_dict_sorted:
            print(f'{line}: {line_dict_sorted[line]} time(s), {int(line_dict_sorted[line]/total_lines * 100)}%')


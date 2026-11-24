import sys
import os


# parsing commands
args = sys.argv  # we get the list of arguments from command line
# print('Arguments:', args)
parameters = {'-sortingType': 'natural', '-dataType':None, '-inputFile':None, '-outputFile':None}
number_of_args = len(args)


if '-sortingType' in args:
    sort_type_index = args.index('-sortingType')
    if sort_type_index + 1 < number_of_args:
        if args[sort_type_index + 1] in ['byCount', 'natural']:
            parameters['-sortingType'] = args[sort_type_index + 1]
        else:
            parameters['-sortingType'] = None
    else:
        parameters['-sortingType'] = None

if '-dataType' in args:
    data_type_index = args.index('-dataType')
    if data_type_index + 1 < number_of_args:
        if args[data_type_index + 1] in ['long', 'line', 'word']:
            parameters['-dataType'] = args[data_type_index + 1]

if '-inputFile' in args:
    input_file_index = args.index('-inputFile')
    if input_file_index + 1 < number_of_args:
        if os.path.isfile(args[input_file_index + 1]):
            parameters['-inputFile'] = args[input_file_index + 1]

if '-outputFile' in args:
    output_file_index = args.index('-outputFile')
    if output_file_index + 1 < number_of_args:
        parameters['-outputFile'] = args[output_file_index + 1]


if not parameters['-sortingType']:
    print('No sorting type defined!')

elif not parameters['-dataType']:
    print('No data type defined!')

for arg in args:
    if arg.startswith('-') and arg not in ['-sortingType', '-dataType', '-inputFile', '-outputFile']:
        print(f'"{arg}" is not a valid parameter. It will be skipped.')


if parameters['-sortingType'] and parameters['-dataType']:



# reading input
    if parameters['-inputFile']:
        with open(parameters['-inputFile'], 'r') as file:
            list_of_lines = file.readlines()
    else:
        list_of_lines = []
        while True:
            try:
                list_of_lines.append(input())
            except EOFError:
                break
    # print(list_of_lines)
    output_string = ''

    match parameters['-dataType'], parameters['-sortingType']:
        case 'long', 'natural':
            list_of_integers = []
            for line in list_of_lines:
                line_split = line.split()
                list_of_integers.extend([int(x) for x in line_split])
            # print(list_of_integers)
            output_string += f'Total numbers: {len(list_of_integers)}.\n'

            sorted_list = sorted(list_of_integers)
            sorted_list_string = ''
            for number in sorted_list:
                sorted_list_string += ' ' + str(number)
            output_string += f'Sorted data:{sorted_list_string}\n'

        case 'line', 'natural':
            total_lines = len(list_of_lines)

            sorted_list = sorted(list_of_lines)

            output_string += f'Total lines: {total_lines}.\n'
            output_string += 'Sorted data:'
            for line in sorted_list:
                output_string += line + '\n'

        case 'word', 'natural':

            list_of_words = []
            for line in list_of_lines:
                line_split = line.split()

                for word in line_split:
                    list_of_words.append(word)
            total_words = len(list_of_words)

            output_string += f'Total words: {total_words}.\n'
            sorted_list_of_words = sorted(list_of_words)
            sorted_list_string = ''
            for word in list_of_words:
                sorted_list_string += ' ' + word
            output_string += f'Sorted data:{sorted_list_string}\n'

        case 'long','byCount':
            list_of_integers = []
            dict_of_integers = {}
            for line in list_of_lines:
                line_split = line.split()
                for x in line_split:
                    try:
                        list_of_integers.append(int(x))
                    except ValueError:
                        output_string += f'"{x}" is not a long. It will be skipped.\n'
                        continue

            # print(list_of_integers)
            output_string += f'Total numbers: {len(list_of_integers)}.\n'
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
                output_string += f'{number}: {count} time(s), {int(count/len(list_of_integers) * 100)}%\n'

        case 'word','byCount':
            # TODO finish this case
            list_of_words = []
            for line in list_of_lines:
                line_split = line.split()
                # total_words += len(line_split)
                for word in line_split:
                    list_of_words.append(word)
            total_words = len(list_of_words)
            output_string += f'Total words: {total_words}.\n'
            word_dict = {}
            for word in list_of_words:
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
            word_dict_sorted = dict(sorted(word_dict.items(), key=lambda item: item[0]))
            word_dict_sorted = dict(sorted(word_dict_sorted.items(), key=lambda item: item[1]))
            for word, count in word_dict_sorted.items():
                output_string += f'{word}: {count} time(s), {int(count/total_words * 100)}%\n'

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

            output_string += f'Total lines: {total_lines}.\n'
            # print('Sorted data:')
            for line in line_dict_sorted:
                output_string += f'{line}: {line_dict_sorted[line]} time(s), {int(line_dict_sorted[line]/total_lines * 100)}%\n'

    if not parameters['-outputFile']:
        print(output_string[:-1])
    else:
        with open(parameters['-outputFile'], 'w') as file:
            file.write(output_string)

total_numbers = 0
the_greatest_number = None
the_greatest_number_count = 0
while True:
    try:
        data = input()
        numbers_list = data.split()
        for number in numbers_list:
            number = int(number)
            total_numbers += 1
            if the_greatest_number is None or number > the_greatest_number:
                the_greatest_number = number
                the_greatest_number_count = 1
            elif number == the_greatest_number:
                the_greatest_number_count += 1
        # print(data)
    except EOFError:
        break

print(f'Total numbers: {total_numbers}.')
print(f'The greatest number: {the_greatest_number} ({the_greatest_number_count} time(s)).')

#CS175L
#Jimmy Kong
#averagefrominputfile

def main():
    numbers_file = open('numbers.txt', 'r')
    line = numbers_file.readline()
    line_num = 0
    total = 0

    for line in numbers_file:
        line_num = line_num + 1
        number = float(line)
        total = total + number
        print('I read in', line_num, 'number(s)')
        print(f'Current number is: {number:.2f}')
        print(f'Total number is: {total:.2f}')
        print('')

    numbers_file.close()
    average = total / line_num
    print(f'Average: {average:.2f}')

if __name__ == '__main__':
    main()

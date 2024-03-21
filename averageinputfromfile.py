#CS175L
#Jimmy Kong
#averageinputfromfile

import sys

def main():
    try:
        numbers = open('numbers.txt', 'r')
    except IOError:
        sys.exit('SystemExit: File not found: numbers.txt - exiting')

    line = int(numbers.readline())    
    line_num = 0
    total = 0

    for line in numbers:
        line_num = line_num + 1
        total = total + line
        try:
            print('I read in', line_num, 'number(s)')
            print(f'Current number is: {line:.2f}')
            print(f'Total number is: {total:.2f}')
            print('')
        except line is not int(line):
            print('Bad data: xyz skipping')  

        numbers.close()
        average = total / line_num
        print(f'Average: {average:.2f}')

if __name__ == '__main__':
    main()


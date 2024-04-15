#CS175L
#Jimmy Kong
#expensePieChart

import matplotlib.pyplot as plt
import os
import sys

def main():
    try:
        expensedata = open('expenses.txt','r')      
    except IOError:
        print('SystemExit: File not found: expenses.txt - exiting')
        sys.exit()

    listtabs = []
    labels = []
    
    for line in expensedata:
        try:
            tabs = line.strip().split('\t')
            listtabs.append(float(tabs[1]))
            labels.append(tabs[0])
        except ValueError:
            print('Could not convert string to float',tabs[1])

    plt.pie(listtabs, labels=labels)
    plt.title('Monthly Expenses')
    plt.show()

if __name__ == '__main__':
    main()
    

'''
Testing stats functions
'''

import sys


class Stats:
    
    def __init__(self): 
        n = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else get_numeric_series()
        print("Stats Class initialised for series: {}".format(n))

    def mean(self):
        pass

def get_numeric_series():
    nums = []
    inp = get_number()
    while (inp != ""):
        nums.append(inp)
        inp = get_number()
    return nums

def get_number():
    try:
        return int(input("Please enter a number:"))
    except (TypeError, ValueError) as e:
        print("Not a Number. Please enter a number.")
        get_number()

def main():
    s = Stats()


if __name__ == '__main__':
    main()

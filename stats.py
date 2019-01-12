'''
Testing stats functions
'''

import sys
from helper import *


class Stats:
    
    def __init__(self): 
        n = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else get_numeric_series()
        print("Stats Class initialised for series: {}".format(n))

    def mean(self):
        pass

def main():
    s = Stats()


if __name__ == '__main__':
    main()

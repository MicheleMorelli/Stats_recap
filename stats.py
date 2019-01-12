"""Playing with some basic stats functions to refresh them!"""

from helper import *
import re
import sys

class Stats:
    
    def __init__(self,*args): 
        """Stats class constructor
        Takes a series of numeric values from the std input and puts them in
        a list n
        """
        if (len(args)):
            self.n = args
        elif (len(sys.argv) > 1):
            self.n = [int(x) for x in sys.argv[1:]]
        else:
            self.n = get_numeric_series()
        print("Stats Class initialised")


    def func_mean(self):
        """Calculates the mean avg of the n list of numbers
        Returns:
            mean (float): the mean value
        """
        return sum(self.n) / len(self.n)
   

    def func_variance(self):
        """Calculates the variance of the n list of numbers
        Returns:
            variance (float): the variance value
        """
        return sum(map(lambda x: (x - self.func_mean())**2, self.n)) \
                / len(self.n)


    def print_values(self):
        """
        Prints the values of all the stats functions for the numeric list n
        """
        print("Basic Statistical Functions for numeric series {}"\
                .format(self.n))
        for attr in dir(self):
            if (not re.match(r'^func_*', attr )): continue
            func_name = re.sub(r'^func_',"", attr).upper()
            print("{}: {:.2f}".format(func_name,getattr(self, attr)()))

        
def main():
    s = Stats(1,2,3,4,5,6)
    s.print_values()


if __name__ == '__main__':
    main()

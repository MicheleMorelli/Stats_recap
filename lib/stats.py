"""Playing with some basic stats functions to refresh them!"""

import re, sys, math

import symbols
from helper import *

class Stats:
    # UTF-compatible math symbols as a reminder for myself:-)
    symbol = symbols.create_dictionary()
    
    def __init__(self,*args): 
        """Stats class constructor
        Takes a series of numeric values from the std input and puts them in
        a list n
        """
        if (len(args)):
            self.n = args
        elif (len(sys.argv) > 1):
            self.n = [float(x) for x in sys.argv[1:]]
        else:
            self.n = get_numeric_series()
        print("Stats Class initialised!")


    def func_mean(self):
        """Calculates the arithmetic mean of the n list of numbers
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
    

    def func_standard_deviation(self):
        """Calculates the standard_deviation of the n list of numbers
        Returns:
            standard_deviation (float): the std. deviation value
        """
        return math.sqrt(self.func_variance())


    def print_values(self):
        """
        Prints the values of all the stats functions for the numeric list n
        """
        div = "\n" + ("*" * 60) + "\n"
        print( div + "Basic Statistical Functions for numeric series {}"\
                .format(self.n).upper() + div)
        for attr in dir(self):
            if (not re.match(r'^func_*', attr )): continue
            func_name = re.sub(r'^func_',"", attr)
            sym = Stats.symbol[func_name] 
            func_name = re.sub(r'_', " ",func_name) # for printing
            print("{} (symbol: {}): {:.2f}"\
                    .format(func_name.capitalize(), \
                    sym,\
                    getattr(self, attr)()
                    )
                    )
        print()

        
def main():
    s = Stats()
    s.print_values()


if __name__ == '__main__':
    main()

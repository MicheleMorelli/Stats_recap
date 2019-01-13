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
       # print("Stats Class initialised!")


    def func_mean(self):
        """Calculates the arithmetic mean of the n list of numbers
        Returns:
            mean (float): the mean value
        """
        return sum(self.n) / len(self.n)
    
    
    def func_median(self):
        """Calculates the median of the n list of numbers
        Returns:
            median (float): the median value of the series
        """
        series = sorted(self.n)
        if (len(series) == 1):
            return series[0]
        elif (len(series) % 2):
            return series[(len(series) - 1) // 2]
        else:
            mid = len(series) // 2 
            return Stats(*series[mid - 1:mid + 1]).func_mean()


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
    
    
    def func_large(self):
        """
        Returns:
            large (float): the largest value in the dataset
        """
        return max(self.n)


    def func_small(self):
        """
        Returns:0
            small(float): the smallest value in the dataset
        """
        return min(self.n)


    def func_range(self):
        """
        Returns:
            range (float): the range between min and max
        """
        return self.func_large() - self.func_small()


    def func_mode(self):
        """
        Returns:
            mode (float): the single elements that recurs the most in the 
            dataset
        """
        d = {}
        for i in self.n:
            d[i] = d.get(i, 0) + 1
        maxi = 0
        for i in d:
            if (d[i] > maxi):
                maxi = d[i]
        mode_lst = list(filter(lambda x: d[x] == maxi, d.keys()))
        return mode_lst[0] if len(mode_lst) == 1 else "N/A"

    
    def func_summation(self):
        """
        Returns:
            summation (float): the summation of all the values in the dataset
        """
        return sum((self.n))


    def func_double_summation(self):
        """
        Returns:
            d_summation (float): the double summation of all the values in 
                the dataset
        """
        return self.func_summation() * len(self.n)

    
    def func_kurtosis(self):
        """
        Returns:
            kurtosis (float): the peakedness of the dataset's  distribution
        """
        return "TODO"


    def func_skewness(self):
        """
        Returns:
            skewness (float): the amount of asymmetry of distribution
            of the dataset
        """
        total_summation = 0
        for i in self.n:
            partial_sum = i - self.func_mean()
            partial_sum /= self.func_standard_deviation()
            partial_sum **= 3
            total_summation += partial_sum
        total_summation /= len(self.n)
        return total_summation



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
            value = getattr(self, attr)()
            value = "{:.2f}".format(value) if isinstance(value,float)\
                    else str(value)

            print("{} (symbol: {}): {}"\
                    .format(func_name.capitalize(), \
                    sym,\
                    value
                    )
                    )
        print()

        
def main():
    s = Stats()
    s.print_values()


if __name__ == '__main__':
    main()

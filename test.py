from stats import *
import numpy

"""
Using numpy as an initial benchmark for testing
"""

def test_mean():
    s = Stats(*range(1,10))
    assert s.func_mean() == numpy.mean(list(range(1,10)))  

def test_mean2():
    s = Stats(*range(1,1010))
    assert s.func_mean() == numpy.mean(list(range(1,1010)))  

def test_variance():
    s = Stats(*range(1,1010))
    assert s.func_variance() == numpy.var(list(range(1,1010)))  

def test_variance2():
    s = Stats(*range(1,100))
    assert s.func_variance() == numpy.var(list(range(1,100)))  

def test_std():
    s = Stats(*range(1,1010))
    assert s.func_standard_deviation() == numpy.std(list(range(1,1010)))  

def test_std2():
    s = Stats(*range(1,100))
    assert s.func_standard_deviation() == numpy.std(list(range(1,100)))  

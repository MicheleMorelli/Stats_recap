import sys
import os
sys.path.append(os.path.join(sys.path[0],'..','lib'))
from stats import *
import numpy as np

"""
Using numpy as an initial benchmark for testing
"""

def test_mean():
    s = Stats(*range(1,10))
    assert s.func_mean() == np.mean(list(range(1,10)))  


def test_mean2():
    s = Stats(*range(1,1010))
    assert s.func_mean() == np.mean(list(range(1,1010)))  

def test_median():
    s = Stats(*range(1,10))
    assert s.func_median() == np.median(list(range(1,10)))  


def test_median2():
    s = Stats(*range(1,1010))
    assert s.func_median() == np.median(list(range(1,1010)))  

def test_variance():
    s = Stats(*range(1,1010))
    assert s.func_variance() == np.var(list(range(1,1010)))  


def test_variance2():
    s = Stats(*range(1,100))
    assert s.func_variance() == np.var(list(range(1,100)))  


def test_std():
    s = Stats(*range(1,1010))
    assert s.func_standard_deviation() == np.std(list(range(1,1010)))  


def test_std2():
    s = Stats(*range(1,100))
    assert s.func_standard_deviation() == np.std(list(range(1,100)))  


def test_large():
    s = Stats(*range(1,100))
    assert s.func_large() == max(list(range(1,100)))


def test_small():
    s = Stats(*range(1,100))
    assert s.func_small() == min(list(range(1,100)))


def test_range():
    s = Stats(*range(1,100))
    assert s.func_range() == np.ptp(list(range(1,100)))


def test_mode():
    s = Stats(1,2,34,4,2,3,21,1,23,32,2,31,2,2432,234,2)
    assert s.func_mode() == 2

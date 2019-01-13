# Basic Statistical Functions #
### by Michele Morelli ###
.\
├── lib\
│   ├── helper.py\
│   ├── stats.py ---> (This is the main class!)\
│   └── symbols.py ---> (A small dictionary of Symbols)\
├── LICENCE.txt\
├── README.md\
└── test\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── test.py ---> (all the pytests are here)\

The new term is approaching, and I found myself refreshing some statistics for the upcoming modules.

I thought it would be a good idea to write down a couple of simple Python methods to help me refresh the basics (and the symbols!).

Just to make sure that everything is working as it should, I used numpy's methods to double-check my functions  in the pytests.

Currently it shows the following functions:
- Arithmetic mean
- Median
- Variance
- Standard Deviation
- Summation
- Double Summation
- Min
- Max
- Range
- Mode

To run it:

    $python3 lib/stats.py [optional: put a list of number as arguments]

So for example:

    $python3 lib/stats.py 23 32 43 2342 342 34 234 234 2342 34 34

For the tests I used pytest:

    $pytest test/test.py

Enjoy!

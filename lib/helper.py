"""Helper methods for the Stats class"""


def get_numeric_series():
    """Creates a list of numbers (float)
    Returns:
        [nums]: a list of numbers
    """
    nums = []
    inp = get_number()
    while (inp):
        nums.append(inp)
        inp = get_number()
    return nums

def get_number():
    """Reads a number from the standard input and returns it
    Returns:
        num (float): an float
        num (nil): if "" is passed via the input
    Raises:
        TypeError, ValueError: if anything other than a num or "" is entered 
        as input
    """
    num = input("Please enter a number:")
    if not num: return 
    try:
        return float(num)
    except (TypeError,ValueError) as e:
        print("Not a Number. Please enter a number.")
        get_number()

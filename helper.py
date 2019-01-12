"""Helper methods for the Stats class"""


def get_numeric_series():
    """Creates a list of ints a list of ints
    Returns:
        [nums]: a list of integers
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
        num (int): an integer
        num (nil): if "" is passed via the input
    Raises:
        ValueError: if anything other than a num or "" is entered as input
    """
    num = input("Please enter a number:")
    return if !num 
    try:
        return int(num)
    except (ValueError) as e:
        print("Not a Number. Please enter a number.")
        get_number()

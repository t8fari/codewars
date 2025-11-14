# You're a square!


def is_square(n):
    """
    Given an integral number, determine if it's a square number
    """
    return n > -1 and not n**.5 % 1
    # if n < 0:
    #     return False
    # return int(str(n**.5)[-1]) == 0

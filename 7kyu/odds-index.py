# Odds-Index


def odd_ball(arr):
    """
    You are given an array with several "even" words, one "odd" word, and some numbers mixed in.

    Determine if any of the numbers in the array is the index of the "odd" word. If so, return true, otherwise false.
    """
    return arr.index("odd") in arr
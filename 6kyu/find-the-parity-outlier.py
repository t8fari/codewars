# Find the Parity Outlier


def find_outlier(integers):
    """
    You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
    Examples

    [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

    [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
    """
    mod2 = [x%2 for x in integers]
    common = 1 if mod2.count(1) > 1 else 0
    for x in integers:
        if x%2 != common:
            return x

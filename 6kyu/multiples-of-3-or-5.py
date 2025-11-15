# Multiples of 3 or 5


def solution(num):
    """
    Return the sum of all the multiples of 3 or 5 below the number passed in
    If the number is negative, return 0
    If a number is a multiple of both 3 and 5, count in once
    """
    return sum(i for i in range(num) if not i%3 or not i%5)

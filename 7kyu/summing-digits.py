# Summing a number's digits


def sum_digits(number):
    """
    Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

    For example: (Input --> Output)

    10 --> 1
    99 --> 18
    -32 --> 5

    Let's assume that all numbers in the input will be integer values.
    """
    return sum(map(int, str(abs(number))))
    # return sum(map(int, list(filter(lambda i: i.isdigit(), str(number)))))
#     nums = [int(i) for i in str(number) if i.isdigit()]
#     return sum(nums)

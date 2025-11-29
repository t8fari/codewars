# Number of trailing zeros of N!


def zeros(n):
    # how many numbers in range(n) have at least one 5 as a factor ==> 100/5 = 20
    # how many of those numbers have at least two 5s (i.e. 25)as a factor ==> 20/5 = 4
    # and so on.... until you have less than 5 numbers
    # count = 20+4 = 24
    count = 0
    while n:
        count += n//5
        n = n//5
    return count


def zeros(n):
    count = 0
    while n:
        n = n // 5
        count += n
    return count


def zeros(n):
    i = 5
    zeros = 0
    while n >= i:
        zeros += n // i
        i *= 5
    return zeros
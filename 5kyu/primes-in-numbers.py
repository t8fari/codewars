# Primes in numbers


def prime_factors(n):
    """
    Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

    "(p1**n1)(p2**n2)...(pk**nk)"

    with the p(i) in increasing order and n(i) empty if n(i) is 1.

    Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
    """
    i = 2
    decomp = ''
    while n != 1:
        count = 0
        while not n%i:
            n = n / i
            count += 1
        if count > 1:
            decomp += f"({i}**{count})"
        elif count == 1:
            decomp += f"({i})"
        i += 1
    return decomp

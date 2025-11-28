# Primes in numbers


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True


def prime_factors(n):
    """
    Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

    "(p1**n1)(p2**n2)...(pk**nk)"

    with the p(i) in increasing order and n(i) empty if n(i) is 1.

    Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
    """
    if is_prime(n):
        return f"({n})"
    
    p_factors = [x for x in range(int(n**.5)+1) if is_prime(x)]
    decomp = []
    g = n
    while not is_prime(g):
        for f in p_factors:
            if not g%f:
                decomp.append(f)
                g = g//f
                break
        if is_prime(g):
            decomp.append(g)
    return ''.join(f"({f}**{decomp.count(f)})" if decomp.count(f)>1 else f"({f})" for f in sorted(set(decomp)))



# print(factors(8))
# print(factors(86240))
# print(prime_factors(86240))
# print(prime_factors(120))
# print(prime_factors(7775460))
# print(factors(120)[1:-1])
# print(is_prime(7919))
print(prime_factors(25))
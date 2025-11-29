# Integers: Recreation One


def list_squared(m, n):
    """
    1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246.

    Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681.

    The sum of these squares is 84100 which is 290 * 290.
    Task

    Find all integers between m and n (m and n are integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

    We will return an array of subarrays or of tuples (in C an array of Pair) or a string.

    The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.
    Example:

    m =  1, n = 250 --> [[1, 1], [42, 2500], [246, 84100]]
    m = 42, n = 250 --> [[42, 2500], [246, 84100]]
    """
    ans = []
    for i in range(m, n+1):
        divisors = [x for x in range(1, int(i**0.5)+1) if not i%x]
        divisors += [i//y for y in divisors if i//y not in divisors]
        sum_squared_divisors = sum(x**2 for x in divisors)
        if not (sum_squared_divisors**.5) % 1:
            ans.append([i, sum_squared_divisors])
    return ans

# divisors = set([x for x in range(1, int(i**0.5)+1) if not i%x])
# divisors.update([i//y for y in divisors])
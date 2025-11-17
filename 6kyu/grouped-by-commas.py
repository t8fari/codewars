# Grouped by commas


def group_by_commas(n):
    """
    Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

    Assume: 0 <= n <= 2147483647
    Examples

    1  ->           "1"
    10  ->          "10"
    100  ->         "100"
    1000  ->       "1,000"
    10000  ->      "10,000"
    100000  ->     "100,000"
    1000000  ->   "1,000,000"
    35235235  ->  "35,235,235"
    """
    n_rev = str(n)[::-1]
    cols = [n_rev[i:i+3] for i in range(0, len(n_rev), 3)]
    
    return ','.join(cols)[::-1]

    # return f"{n:,}"

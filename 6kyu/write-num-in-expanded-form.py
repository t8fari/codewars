# Write number in expanded form


def expanded_form(num):
    """
    You will be given a number and you will need to return it as a string in Expanded Form. For example:

    12 --> "10 + 2"
    45 --> "40 + 5"
    70304 --> "70000 + 300 + 4"

    NOTE: All numbers will be whole numbers greater than 0.
    """
    n = len(str(num))-1
    cols = [int(c)*10**(n-i) for i, c in enumerate(str(num))]
    return " + ".join(str(x) for x in cols if x)

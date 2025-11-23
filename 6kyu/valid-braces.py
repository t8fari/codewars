# Valid Braces


def valid_braces(string):
    """
    Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.
    Examples
    "(){}[]"   =>  True
    "([{}])"   =>  True
    "(}"       =>  False
    "[(])"     =>  False
    "[({})](]" =>  False
    """
    s = string
    valid = ['{}', '()', '[]']
    for _ in range(len(s)//2):
        for brace in valid:
            s = s.replace(brace, '')
    return not s

def valid_braces(string):
    valid = ['{}', '()', '[]']
    while any(b in string for b in valid):
        for v in valid:
            string = string.replace(v, '')
    return not string

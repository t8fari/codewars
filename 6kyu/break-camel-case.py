# Break camelCase

def solution(s):
    """
    Complete the solution so that the function will break up camel casing, using a space between words.
    Example

    "camelCasing"  =>  "camel Casing"
    "identifier"   =>  "identifier"
    ""             =>  ""
    """
    return ''.join(char if char.islower() else " "+char for char in s)

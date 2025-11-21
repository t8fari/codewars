# Find the missing letter


def find_missing_letter(chars):
    """
    Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

    You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
    The array will always contain letters in only one case.

    Example:

    ['a','b','c','d','f'] -> 'e'
    ['O','Q','R','S'] -> 'P'
    """
    for i in range(ord(min(chars)), ord(max(chars))):
        if chr(i) not in chars:
            return chr(i)

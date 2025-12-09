# Sentence Calculator


def letters_to_numbers(s):
    """
    Calculate the total score (sum of the individual character scores) of a sentence given the following score rules for each allowed group of characters:

    Lower case [a-z]: 'a'=1, 'b'=2, 'c'=3, ..., 'z'=26
    Upper case [A-Z]: 'A'=2, 'B'=4, 'C'=6, ..., 'Z'=52
    Digits [0-9] their numeric value: '0'=0, '1'=1, '2'=2, ..., '9'=9
    Other characters: 0 value

    Note: input will always be a string
    """
    total = 0
    for c in s:
        if c.isalpha():
            num_val = ord(c.lower())-96
            d = 1 if c.islower() else 2
            total += num_val*d
        elif c.isdigit():
            total += int(c)
    return total
# Vowel Recognition


def vowel_recognition(s):
    """
    Given a string "baceb" you can split it into substrings: b, ba, bac, bace, baceb, a, ac, ace, aceb, c, ce, ceb, e, eb, b. The number of vowels in each of these substrings is 0, 1, 1, 2, 2, 1, 1, 2, 2, 0, 1, 1, 1, 1, 0; if you sum up these number, you get 16 - the expected output.

    Note: your solution should have linear time complexity.
    """
    # each vowel will appear c*pos times
    # c is how many times it begins a substring
    # pos is the position of the vowel in `s`
    
    # how many times each vowel in `s` begins a substring
    counts = [len(s)-i for i in range(len(s)) if s[i].lower() in 'aeiou']
    # the position of each vowel in `s`
    vowel_pos = [i for i, j in enumerate(s,1) if j.lower() in 'aeiou']

    return sum((i*j) for i, j in zip(counts,vowel_pos))


def vowel_recognition(s):
    return sum((i + 1) * (len(s) - i) for i, c in enumerate(s) if c in 'AEIOUaeiou')
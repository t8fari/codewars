# Highest Scoring Word


import string

def high(x):
    """
    Given a string of words, you need to find the highest scoring word.

    Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

    For example, the score of abad is 8 (1 + 2 + 1 + 4).

    You need to return the highest scoring word as a string.

    If two words score the same, return the word that appears earliest in the original string.

    All letters will be lowercase and all inputs will be valid.
    """
    alpha = '_' + string.ascii_lowercase
    words = x.split()
    scores = [sum(alpha.index(c) for c in word) for word in words]
    ind_of_max_score = scores.index(max(scores))
    
    return words[ind_of_max_score]

def high(x):
    return max(x.split(), key=lambda x: sum(ord(c)-96 for c in x))

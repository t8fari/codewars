# Countdown - Longest Word


def longest_word(letters):
    """
    Given an uppercase 9 letter string, letters, find the longest word that can be made with some or all of the letters. The preloaded array words (or $words in Ruby) contains a bunch of uppercase words that you will have to loop through. Only return the longest word; if there is more than one, return the words of the same lengths in alphabetical order. If there are no words that can be made from the letters given, return None/nil/null.
    Examples

    letters = "ZZZZZZZZZ"
    longest word = None

    letters = "POVMERKIA", 
    longest word = ["VAMPIRE"]

    letters = "DVAVPALEM"
    longest word = ["PALMED", "VALVED", "VAMPED"]
    """
    words = []  # words is preloaded in the kata
    res = [word for word in words if all(letters.count(c)>=word.count(c) for c in word)]
    if not res: return None
    max_len = len(max(res, key=len))
    return [x for x in res if len(x)==max_len]
    
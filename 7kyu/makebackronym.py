# makeBackronym


#preloaded variable: "dictionary"
dictionary = {}

def make_backronym(acronym):
    """
    Complete the function to create backronyms. Transform the given string (without spaces) to a backronym, using the preloaded dictionary and return a string of words, separated with a single space (but no trailing spaces).

    The keys of the preloaded dictionary are uppercase letters A-Z and the values are predetermined words, for example:

    dictionary["P"] == "perfect"

    Examples

    "dgm" ==> "disturbing gregarious mustache"

    "lkj" ==> "literal klingon joke"
    """
    return ' '.join(dictionary[c] for c in acronym.upper())
    # return ' '.join(map(lambda c: dictionary[c], acronym.upper()))
    # return ' '.join(map(dictionary.get, acronym.upper()))

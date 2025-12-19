# Reverse words


def reverse_words(text):
    """
    Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
    Examples

    "This is an example!" ==> "sihT si na !elpmaxe"
    "double  spaces"      ==> "elbuod  secaps"
    """
    return ' '.join(map(lambda c: c[::-1], text.split(' ')))
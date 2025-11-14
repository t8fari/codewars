# Get the Middle Character


def get_middle(s):
    """
    You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.
    If the string's length is odd, return the middle character.
    If the string's length is even, return the middle 2 characters.
    Examples:
    "test" --> "es"
    "testing" --> "t"
    "middle" --> "dd"
    "A" --> "A"
    """
    x = len(s)
    if x % 2:
        return s[x//2]
    return f"{s[(x//2)-1]}{s[x//2]}"

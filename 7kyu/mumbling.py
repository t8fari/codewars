# Mumbling


def accum(string):
    """
    This time no story, no theory. The examples below show you how to write function accum:
    Examples:
    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"
    The parameter of accum is a string which includes only letters from a..z and A..Z.
    """
    return '-'.join((string[i]*(i+1)).title() for i in range(len(string)))
    # return '-'.join((c*(i+1)).title() for i, c in enumerate(string))

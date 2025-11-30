# Strip Comments


def strip_comments(string, markers):
    """
    Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

    Example:

    Given an input string of:

    apples, pears # and bananas
    grapes
    bananas !apples

    The output expected would be:

    apples, pears
    grapes
    bananas
    """
    ss = string.split('\n')
    for i in range(len(ss)):
        s = ss[i]
        for m in markers:
            index = s.find(m)
            if index >= 0:
                s = s[:index].rstrip()
        ss[i] = s
    return '\n'.join(ss)


def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

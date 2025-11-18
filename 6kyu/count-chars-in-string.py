# Count characters in your string


def count(s):
    """
    The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

    What if the string is empty? Then the result should be empty object literal, {}.
    """
    ans = {}
    for k in set(s):
        ans[k] = s.count(k)
    return ans


def count(s):
    return {k: s.count(k) for k in set(s)}

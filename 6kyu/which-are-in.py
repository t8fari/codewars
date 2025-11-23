# Which are in?


def in_array(array1, array2):
    """
    Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
    Example 1:

    a1 = ["arp", "live", "strong"]

    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

    returns ["arp", "live", "strong"]
    Example 2:

    a1 = ["tarp", "mice", "bull"]

    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

    returns []
    """
    ans = []
    for word in sorted(set(array1)):
        if any(word in x for x in array2):
            ans.append(word)
    return ans

def in_array(array1, array2):
    return [word1 for word1 in sorted(set(array1)) if any(word1 in word2 for word2 in array2)]
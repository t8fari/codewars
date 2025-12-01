# Find the unique string


def find_uniq(arr):
    """
    There is an array of strings. All strings contains similar letters except one. Try to find it!

    find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
    find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

    Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

    It's guaranteed that array contains more than 2 strings.
    """
    # sort the array so that the unique string will be at one of the ends
    words = sorted(arr, key=lambda x: x.lower())
    unique1 = set(words[0].lower())   # used `set` to enable comparison

    # since the unique string will be at one of the ends,
    # we'll just compare the second element in arr to them
    if set(words[1].lower().strip()) == unique1:
        return words[-1]
    else:
        return words[0]


print(find_uniq(['q','e','q','q']))


def find_uniq(arr):
    low = [''.join(sorted(set(i.lower().replace(' ', '')))) for i in arr]
    return arr[low.index(min(set(low), key=low.count))]

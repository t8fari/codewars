# Find the missing term in an Arithmetic Progression


def find_missing(arr):
    """
    An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

    You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.
    Example

    find_missing([1, 3, 5, 9, 11]) == 7
    """
    a, l, n = arr[0], arr[-1], len(arr)+1
    return ((n/2)*(a+l)) - sum(arr)


def find_missing(arr):
    ds = [arr[i]-arr[i-1] for i in range(1, 5)]
    d = max(ds, key=ds.count)
    a = arr[0]
    for n in range(2,len(arr)+1):
        N = a+((n-1)*d)
        if N != arr[n-1]:
            return N

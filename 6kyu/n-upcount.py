# n-upcount

arr = [5, 6, -6, 3, 1]
def n_upcount(n):
    """
    count the number of times the partial sum goes from <= n to > n
    """
    count = 0
    partial_sum = 0
    temp = arr[0]
    for x in arr:
        partial_sum += x
        # if temp <= n and partial_sum > n:
        if temp <= n < partial_sum:
            count += 1
        temp = partial_sum
    return count

print(n_upcount(6))
arr = [1,12,-1]
print(n_upcount(20))


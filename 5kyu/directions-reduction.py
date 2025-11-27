# Directions Reduction


def dir_reduc(arr):
    opp = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    ans = []
    for d in arr:
        if ans and ans[-1] == opp[d]:
            ans.pop(-1)
        else:
            ans.append(d)
    return ans

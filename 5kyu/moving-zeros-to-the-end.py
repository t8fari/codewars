# Moving zeros to the end


def move_zeros(lst):
    """
    Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
    """
    return sorted(lst, key= bool, reverse=True)
    # return [i for i in lst if i] + [0]*lst.count(0)

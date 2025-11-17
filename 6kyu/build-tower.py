# Tower Builder


def tower_builder(n_floors):
    """
    Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

    For example, a tower with 3 floors looks like this:

    [
    "  *  ",
    " *** ", 
    "*****"
    ]

    And a tower with 6 floors looks like this:

    [
    "     *     ", 
    "    ***    ", 
    "   *****   ", 
    "  *******  ", 
    " ********* ", 
    "***********"
    ]
    """
    return [('*'*i).center(n_floors*2-1) for i in range(1, n_floors*2, 2)]

    # tower = []
    # for i in range(1, n_floors*2, n):
    #     tower.append(('*'*i).center(n_floors*2-1))
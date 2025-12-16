# Only One


def only_one(*bools):
    """
    Write function only_one which return True if ONLY ONE of the boolean flag is True, otherwise return False. If there are no boolean flag, return False

    only_one() == False
    only_one(True, False, False) == True
    only_one(True, False, False, True) == False
    only_one(False, False, False, False) == False  
    """
    return bools.count(True)==1
    # return sum(bools)==1
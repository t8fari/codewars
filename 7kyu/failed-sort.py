# Failed Sort - Bug Fixing #4


def sort_array(value):
    return "".join(sorted(value,key=lambda a: int(a)))
    # return "".join(sorted(value))
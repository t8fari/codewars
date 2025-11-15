# Who likes it?


def likes(names):
    """
    You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

    Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

    []                                -->  "no one likes this"
    ["Peter"]                         -->  "Peter likes this"
    ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
    """
    lenn = len(names)
    if lenn == 0:
        return "no one likes this"
    elif lenn == 1:
        return f"{names[0]} likes this"
    elif lenn == 2:
        return f"{' and '.join(names)} like this"
    elif lenn == 3:
        return f"{names[0]}, {' and '.join(names[1:])} like this"
    else:
        return f"{', '.join(names[:2])} and {lenn-2} others like this"

# clever solution i found
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

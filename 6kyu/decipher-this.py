# Decipher this!


def decipher_this(text):
    """
    You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

    For each word:

    the second and the last letter is switched (e.g. Hello becomes Holle)
    the first letter is replaced by its character code (e.g. H becomes 72)

    there are no special characters used, only letters and spaces
    words are separated by a single space
    there are no leading or trailing spaces

    Examples

    '72olle 103doo 100ya' --> 'Hello good day'
    '82yade 115te 103o'   --> 'Ready set go'
    """
    res = []
    for word in text.split():
        num_part = ''.join(i for i in word if i.isdigit())
        str_part = word[len(num_part):]
        s = chr(int(num_part))
        if not str_part:
            res.append(s)
            continue
        elif len(str_part) == 1:
            s += str_part
        else:
            s += str_part[-1] + str_part[1:-1] + str_part[0]
        res.append(s)
    return ' '.join(res)

# i = sum(map(str.isdigit, word))
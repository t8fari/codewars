# Reverse every other word in the string


def reverse_alternate(st):
    """
    Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata. 
    """
    words = st.split()
    return ' '.join(words[i] if not i%2 else words[i][::-1] for i in range(len(words)))
    # return ' '.join(j if not i%2 else j[::-1] for i, j in enumerate(st.split()))

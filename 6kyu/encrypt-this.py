# Encrypt this!


def encrypt_this(text):
    """
    You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

    Your message is a string containing space separated words.
    You need to encrypt each word in the message using the following rules:
        The first letter must be converted to its ASCII code.
        The second letter must be switched with the last letter
    Keepin' it simple: There are no special characters in the input.

    Examples:

    encrypt_this("Hello") == "72olle"
    encrypt_this("good") == "103doo"
    encrypt_this("hello world") == "104olle 119drlo"
    """
    res = []
    for word in text.split():
        # converting the first letter to its ASCII code
        s = str(ord(word[0]))
        # if word has only 1 letter, add s to res and continue to the next word
        if len(word) == 1:
            res.append(s)
            continue
        # if word has 2 letters, add the second letter to s
        elif len(word) == 2:
            s += word[1]
        # if word has more than 2 letters, swap the 2nd and last letters
        else:
            sec, last = word[-1], word[1]
            s += word[-1] + word[2:-1] + word[1]
        res.append(s)
    return ' '.join(res)
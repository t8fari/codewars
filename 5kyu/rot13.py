# Rot13


from string import ascii_lowercase

def rot13(message):
    """
    ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

    Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
    """
    ans = ''
    for c in message:
        if c.isalpha():
            c_pos = ascii_lowercase.index(c.lower())
            rep_char = ascii_lowercase[min(c_pos-13, c_pos+13)]
            if c.isupper():
                ans += rep_char.upper()
            else:
                ans += rep_char.lower()
        else:
            ans += c
    return ans
    
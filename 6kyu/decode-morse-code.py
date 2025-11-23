# Decode the Morse code

MORSE_CODE = {}

def decode_morse(morse_code):
    """
    Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

    For example:

    decode_morse('.... . -.--   .--- ..- -.. .')
    #should return "HEY JUDE"
    """
    words = morse_code.split('   ')
    ans = ''
    for word in words:
        for char in word.split():
            ans += MORSE_CODE[char]
        ans += ' '
    return ans.strip()
            
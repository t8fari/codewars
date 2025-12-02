# Simple Encryption #1 - Alternating Split

"""
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"

Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
"""

def decrypt(text, n):
    if n<0 or not text:
        return text
    for _ in range(n):
        i = [i for i in range((len(text)//2), len(text))]
        j = [i for i in range(len(text)//2)]
        s = ''
        while i:
            s += text[i.pop(0)]
            if j:
                s += text[j.pop(0)]
        text = s
    return text


def encrypt(text, n):
    if not text or n<0:
        return text
    for _ in range(n):
        odd = ''.join(text[i] for i in range(len(text)) if i%2)
        even = ''.join(text[i] for i in range(len(text)) if not i%2)
        text = odd + even
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text

# print(encrypt('012345', 2))
# print(encrypt('Purchases', 2))
# for i in range(1, 22):
#     print(i, ':', encrypt('This is a ', i))

    # print(i, ':', encrypt('inventor', i))

# x = encrypt('This is a test!', 5)
# print(x)
# print(decrypt(x, 5))
# print(decrypt("ucaePrhs", 1))
print(decrypt("hsi  etTi sats!",1))
# print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))
# print(encrypt('Purchase', 1))
# print(encrypt('Purchase', 2))
# print(decrypt(encrypt('012345',2), 2))
# print(decrypt('01234', 1))
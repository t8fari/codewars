
def base(num, n=10):
    if num == 0:
        return '0'
    res = ''
    while num:
        res = str(num%n) + res
        num = num//n
    return res


def is_palindrome(n):
    if len(n) <= 1:
        return True
    return n[0]==n[-1] and is_palindrome(n[1:-1])


print(is_palindrome('111'))
print(is_palindrome('2002'))
print(is_palindrome('10201'))
print(is_palindrome('10'))

# print(base(0))
# print(base(1))
# print(base(55,3))
# print(base(100, 3))
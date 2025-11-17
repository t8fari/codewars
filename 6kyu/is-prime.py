# Is a number prime?


def is_prime(num):
    """
    Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num**.5)+1):
        if not num % i:
            return False
    return True

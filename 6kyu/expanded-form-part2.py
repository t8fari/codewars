# Write number in expanded form - Part 2


def expanded_form(num):
    """
    You will be given a number and you will need to return it as a string in expanded form :
    For example:

    807.304 --> "800 + 7 + 3/10 + 4/1000"
    1.24  --> "1 + 2/10 + 4/100"
    7.304 --> "7 + 3/10 + 4/1000"
    0.04  --> "4/100"
    """
    num = str(num)
    point = num.index('.')
    n = len(num[:point])-1
    whole = [str(int(c)*10**(n-i)) for i, c in enumerate(num[:point]) if int(c)]
    decimal = [f"{x}/{10**(j+1)}" for j, x in enumerate(num[point+1:]) if int(x)]
    return " + ".join(whole + decimal)


def expanded_form(num):
    integer, fraction = str(num).split('.')
    n = len(integer)-1
    whole = [str(int(c)*10**(n-i)) for i, c in enumerate(integer) if int(c)]
    decimal = [f"{x}/{10**(j+1)}" for j, x in enumerate(fraction) if int(x)]
    return " + ".join(whole + decimal)


sentence = "What letter of the alphabet is the one which comes eight letters before the letter which comes five letters after the fourth appearance of the first letter to occur four times in this sentence?".lower().replace(' ', '')
count = {}

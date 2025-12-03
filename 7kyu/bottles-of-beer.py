# 99 Bottles of Beer


def sing():
    lines = []
    for i in range(99, -1, -1):
        s1 = 's' if i!=1 else ''
        s2 = 's' if i-1!=1 else ''
        start_num = i if i>0 else 'No more'
        end_num = i-1 if i>1 else 'no more'
        takedown = "Take one down and pass it around" if i else "Go to the store and buy some more"
        
        lines.append(f"{start_num} bottle{s1} of beer on the wall, {str(start_num).lower()} bottle{s1} of beer.")
        if i==0: end_num = 99
        lines.append(f"{takedown}, {end_num} bottle{s2} of beer on the wall.")
    return lines

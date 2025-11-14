# Complementary DNA


def DNA_strand(dna):
    """
    In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all.
    Example: (input --> output)
    "ATTGC" --> "TAACG"
    "GTAT" --> "CATA"
    """
    complements = {'A': 'T',
                   'T': 'A',
                   'C': 'G',
                   'G': 'C'}
    return ''.join(complements[s] for s in dna)

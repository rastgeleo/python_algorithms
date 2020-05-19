def str_comb(n, letters):
    """ combination of given letters recursively.
    input
        n: the length of result combinations
        e.g 3 -> aaa, 4 -> aaaa
        letters: string letters to be used for the combination
        e.g 'abc'
    """
    if n == 1:
        return letters
    return [digit + letter for digit in str_comb(1, letters) for letter in str_comb(n-1, letters)]

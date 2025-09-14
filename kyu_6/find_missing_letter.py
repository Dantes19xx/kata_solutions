def find_missing_letter(chars):
    """['a','b','c','d','f'] -> 'e'
    ['O','Q','R','S'] -> 'P'
    """

    ord_arr = list(map(ord, chars))

    for i in range(1, len(ord_arr)):
        if ord_arr[i] - ord_arr[i-1] != 1:
            return chr(ord_arr[i] - 1)

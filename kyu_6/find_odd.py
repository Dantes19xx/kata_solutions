def find_it(seq: list[int]) -> int:
    """Given an array of integers, find the one that appears 
    an odd number of times
    There will always be only one integer that appears an odd 
    number of times.

    :seq: Array of digits
    :return: a number that occurs an odd number of times
    """

    for i in set(seq):
        if seq.count(i) % 2 == 1:
            return i

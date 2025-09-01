def is_isogram(string: str) -> bool:
    """ An isogram is a word that has no repeating letters,
    consecutive or non-consecutive. Implement a function 
    that determines whether  a string that contains only 
    letters is an isogram. Assume the empty string is 
    an isogram. Ignore letter case.
    
    :string: The word that will be checked for isogram validation.
    :return: Isogram validation result
    """

    return len(string) == len({x.lower() for x in string})

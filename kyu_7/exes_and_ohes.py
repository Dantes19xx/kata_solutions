def xo(s: str) -> bool:
    """Function check 'x's and 'o's chars count equal.
    
    :s: String with any chars.
    :return: True, if count(x) == count(o). Else false
    """

    return s.lower().count("x") == s.lower().count("o")

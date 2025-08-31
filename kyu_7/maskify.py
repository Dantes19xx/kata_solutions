def maskify(cc: str) -> str:
    """Put mask on string, if lenght more than 3.
    Each char will be replaced with '#' excluding 4 last.

    :cc: Public string
    :return: Masked string
    """
    
    if len(cc) < 4:
        return cc
    
    return ("#" * len(cc[:-4])) + cc[-4:]

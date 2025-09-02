def accum(st: str) -> str:
    """This time no story, no theory.
    The examples below show you how to write function accum:

    Examples:
    accum("abcd") -> 'A-Bb-Ccc-Dddd'
    accum("RqaEzty") -> 'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'
    accum("cwAt") -> 'C-Ww-Aaa-Tttt'
    """
    
    return "-".join([(st[i]*(i+1)).capitalize() for i in range(len(st))])

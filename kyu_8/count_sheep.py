def count_sheep(n):
    """Given a non-negative integer, 3 for example, return a string with a murmur:
    "1 sheep...2 sheep...3 sheep...".
    Input will always be valid, i.e. no negative integers.
    """
    
    if not n:
        return ""

    return "".join([f"{x+1} sheep..." for x in range(n)]).rstrip()


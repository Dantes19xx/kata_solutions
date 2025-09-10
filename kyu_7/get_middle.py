def get_middle(s):
    """
    If the string's length is odd, return the middle character.
    If the string's length is even, return the middle 2 characters.
    Examples:
    "test" --> "es"
    "testing" --> "t"
    "middle" --> "dd"
    "A" --> "A
    """

    n = len(s)

    if n == 1:
        return s[0]

    if n % 2 == 0:
        return f"{s[(n//2)-1]}{s[n//2]}"
    else:
        return s[n//2]
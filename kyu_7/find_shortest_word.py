def find_short(s):
    """Simple, given a string of words, return the length of the
    shortest word(s).
    String will never be empty and you do not need to account
    for different data types.
    """
    
    word_to_len_digit: list[int] = [len(i) for i in s.split()]
    
    return min(word_to_len_digit)

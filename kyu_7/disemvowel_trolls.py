def disemvowel(string_: str) -> str:
    """Removing all vowels from string, excluded 'y' && 'Y'.
    :string_: String with vowels.
    :return: String without vowels.
    """

    result_str: str = ""

    for i in string_:
        current_char = i.lower()
        if current_char not in ["a", "e", "i", "o", "u"]:
            result_str += i
    return result_str

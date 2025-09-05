def double_char(s):
    """Examples (Input -> Output):
    * 'String'      -> 'SSttrriinngg'
    * 'Hello World' -> 'HHeelllloo  WWoorrlldd'
    * '1234!_ '     -> '11223344!!__ '
    """
    
    return "".join([i * 2 for i in s])

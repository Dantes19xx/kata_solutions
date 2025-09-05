def filter_list(l):
    """filter_list([1,2,'a','b']) == [1,2]
    filter_list([1,'a','b',0,15]) == [1,0,15]
    filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
    """

    'return a new list with the strings filtered out'

    return [x for x in l if isinstance(x, int)]

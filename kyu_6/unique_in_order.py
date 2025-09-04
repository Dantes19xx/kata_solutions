def unique_in_order(sequence):
    """
    Implement the function unique_in_order which takes 
    as argument a sequence and returns a list of items without 
    any elements with the same value next to each other and 
    preserving the original order of elements.

    For example:
    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
    unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
    """
    
    n = len(sequence)
    res_arr = []
    counter = 0


    if len(sequence) == 1:
        return list(sequence[0])

    while counter < n:
        for i in range(counter + 1, n):
            if sequence[counter] != sequence[i]:
                res_arr.append(sequence[counter])
                break
        if counter + 1 == n:          
            if not res_arr or sequence[counter] != res_arr[-1]:
                res_arr.append(sequence[counter])
                counter = n
        else:
            counter = i
    
    return res_arr

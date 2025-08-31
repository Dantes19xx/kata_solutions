def move_zeros(lst: list[int]) -> list[int]:
    """Moving zeroes to the end of list,
    but preserving the order of the other elements.
    
    :lst: Raw list.
    :return: List, with zeroes in the end of list,
    but preserving the order of the other elements.
    """

    n = len(lst)
    for i in range(n):
        if lst[i] != 0:
            continue
        
        zero_idx = i        
        for j in range(i + 1, n):
            if lst[j] != 0:
                lst[zero_idx], lst[j] = lst[j], lst[zero_idx]
                zero_idx = j + 1
            
    return lst

def summation(num: int) -> int:
    """Write a program that finds the summation of every number 
    from 1 to num (both inclusive). The number will always 
    be a positive integer greater than 0. Your function only 
    needs to return the result, what is shown between parentheses 
    in the example below is how you reach that result and it's 
    not part of it, see the sample tests.

    :num:
    :return: summation result.
    """
    
    if num == 1:
        return 1
    
    return num + summation(num - 1)

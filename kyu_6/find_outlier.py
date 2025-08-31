def find_outlier(integers: list[int]) -> int:
    """The array is either entirely comprised 
    of odd integers or entirely comprised of even integers 
    except for a single integer N. Write a method that takes
    the array as an argument and returns this 'outlier' N.
    
    :integers: Raw list of ints.
    :return: Outlier
    """
    
    odd = [i for i in integers if i % 2 == 1]
    even = [i for i in integers if i % 2 == 0]

    return odd[0] if len(odd) == 1 else even[0]

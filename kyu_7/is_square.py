from math import sqrt

def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    
    sqrt_res = str(sqrt(n)).split(".")
    
    return True if len(sqrt_res[1]) == 1 and sqrt_res[1].startswith("0") else False



is_square(26)
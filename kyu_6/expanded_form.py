def expanded_form(num):
    """You will be given a number and you will need 
    to return it as a string in Expanded Form. 
    For example:
    12 --> "10 + 2"
    45 --> "40 + 5"
    70304 --> "70000 + 300 + 4"
    All numbers will be whole numbers greater than 0.
    """
   
    digit_components = []
    divider = 10
    operation_num = int(num)
  
    for _ in range(len(str(num))):
        digit = operation_num % divider
        if digit != 0:
            digit_components.insert(0, str(digit))
        divider *= 10
        operation_num -= digit

    return " + ".join(digit_components)   

expanded_form(11)
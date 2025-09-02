from math import floor


def litres(time: int) -> int:
    """Nathan loves cycling.
    Because Nathan knows it is important to stay hydrated, 
    he drinks 0.5 litres of water per hour of cycling.
    You get given the time in hours and you need to return 
    the number of litres Nathan will drink, rounded down.
    
    :time: How many times Nathan drinks 0.5L of water per hour.
    :return: Drinked litres qty per.
    """
    return floor(time * 0.5)

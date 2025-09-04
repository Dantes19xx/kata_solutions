def quarter_of(month):
    """Given a month as an integer from 1 to 12,
    return to which quarter of the year it belongs as an integer number.
    
    For example: month 2 (February), is part of the first quarter;
    month 6 (June), is part of the second quarter; and month 11
    (November), is part of the fourth quarter.
    """
    
    if 1 <= month <= 3:
        return 1

    elif 4 <= month <= 6:
        return 2
    
    elif 7 <= month <= 9:
        return 3
    
    else:
        return 4
    
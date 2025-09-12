def format_duration(seconds):
    """
    Your task in order to complete this Kata is to write a function which 
    formats a duration, given as a number of seconds, in a human-friendly way.

    The function must accept a non-negative integer. If it is zero, it just returns "now". 
    Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

    It is much easier to understand with an example:

    * For seconds = 62, your function should return 
    "1 minute and 2 seconds"
    * For seconds = 3662, your function should return
    For the purpose of this Kata, a year is 365 days and a day is 24 hours.
    "1 hour, 1 minute and 2 seconds"""
    
    if not seconds:
        return "now"
    
    minutes = seconds // 60
    seconds = seconds % 60
    
    hours = minutes // 60
    minutes = minutes % 60

    days = hours // 24
    hours = hours % 24

    years = days // 365
    days = days % 365

    calculated_time_arr = []

    calculated_time_arr.append(f"{years} year" if years == 1 else f"{years} years" if years else "")
    calculated_time_arr.append(f"{days} day" if days == 1 else f"{days} days" if days else "")
    calculated_time_arr.append(f"{hours} hour" if hours == 1 else f"{hours} hours" if hours else "")
    calculated_time_arr.append(f"{minutes} minute" if minutes == 1 else f"{minutes} minutes" if minutes else "")
    calculated_time_arr.append(f"{seconds} second" if seconds == 1 else f"{seconds} seconds" if seconds else "")

    calculated_time_arr = [i for i in calculated_time_arr if i]

    human_readable = ", ".join(calculated_time_arr[:len(calculated_time_arr)-1])

    if not human_readable:
        return calculated_time_arr[0]
    
    else:
        return f"{human_readable} and {calculated_time_arr[-1]}"

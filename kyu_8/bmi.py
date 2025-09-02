def bmi(weight: int, height: float) -> str:
    """BMI calculation function
    (bmi = weight / height2).

    :weight:
    :height:
    :return" Calculated BMI.
    """
    
    bmi: float = weight / (height*height)

    if bmi <= 18.5:
        return "Underweight"
    
    elif bmi <= 25.0:
        return "Normal"
    
    elif bmi <= 30.0:
        return "Overweight"
    
    else:
        return "Obese"

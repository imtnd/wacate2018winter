def determineValue(age, isStudent):
    value = 1200
    if (age <= 19 and isStudent == True):
        value = 1000 
    return value

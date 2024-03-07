def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    if 1<=temp<=10:
        return "Very Cold"
    if 10<temp<21:
        return "Cold"
    if 20<temp<31:
        return "Normal"
    if 30<temp<41:
        return "Hot"
    if temp>40:
        return "Very hot"
    else:
        return "Freezing"
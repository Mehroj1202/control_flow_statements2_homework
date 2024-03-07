def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    first_number=n//100000
    second_number=n//10000%10
    third_number=n//1000%10
    fourth_number=n//100%10
    fifth_number=n%10
    x=0
    if x<first_number:
        x=first_number
    if x<second_number:
        x=second_number
    if x<third_number:
        x=third_number
    if x<fourth_number:
        x=fourth_number
    if x<fifth_number:
        x=fifth_number
    return x
print(main(90685))
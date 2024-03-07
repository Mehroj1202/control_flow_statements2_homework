def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    x=a
    if a==b:
        return 0
    if x<a:
        x=a
    if x<b:
        x=b
    return x
print(main(8,9))
def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    x=a
    y=b
    if x>a:
        x=a
    if x>b:
        x=b
    if x>c:
        x=c
    if y<a:
        y=a
    if y<b:
        y=b
    if y<c:
        y=c
    return a+b+c-x-y
print(main(4,5,7))
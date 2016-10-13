import math

def angles(a, b, c):
    try:
        aa = round(math.acos((b**2 +c**2 - a**2)/(2*b*c))*180/math.pi)
        bb = round(math.acos((c**2 +a**2 - b**2)/(2*c*a))*180/math.pi)
        cc = round(math.acos((a**2 +b**2 - c**2)/(2*a*b))*180/math.pi)
    except ValueError:
        aa = 0
        bb = 0
        cc = 0

    if 0 in [aa,bb,cc]:
        aa = 0
        bb = 0
        cc = 0

    return sorted([aa, bb, cc])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"
    assert angles(10,20,30) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

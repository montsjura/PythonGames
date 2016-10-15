import fractions as f

def divide_pie(groups):
    nbRobots = sum(map(abs,groups))
    remainingCharge = f.Fraction(nbRobots,nbRobots)

    for group in groups:
        if group > 0:
            remainingCharge -= f.Fraction(group,nbRobots)
        else:
            remainingCharge -= f.Fraction(1,nbRobots)*remainingCharge*abs(group)

    return (remainingCharge.numerator,remainingCharge.denominator)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    #assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    #assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    #assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    #assert tuple(divide_pie((10,))) == (0, 1), "All together"
    assert tuple(divide_pie((6, -4, 6, 24, 23, 65))) == (0, 1), "All together"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

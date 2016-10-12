import math

# Formula found and explained here
# http://www.lucamoroni.it/the-dice-roll-sum-problem/
def comb(n, k):
        return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def probability(dices, sides, target):
    # Case not possible
    if target > dices * sides:
        return 0

    # Find the Kmax
    kmax = math.floor((target - dices) / sides)

    # Find the amount of the event
    sum = 0

    for k in range(kmax+1):
        sum += ((-1)**k)*comb(dices,k)*comb(target-sides*k-1,target-sides*k-dices)

    print(round(sum/(sides**dices), 4))
    return round(sum/(sides**dices), 4)


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

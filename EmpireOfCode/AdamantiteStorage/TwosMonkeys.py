def two_monkeys(asmile, bsmile):
    if asmile and bsmile:
        return True
    if not(asmile) and not(bsmile):
        return True
    return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert two_monkeys(True, True) == True, "First"
    assert two_monkeys(False, False) == True, "Second"
    assert two_monkeys(True, False) == False, "Third"
    assert two_monkeys(False, True) == False, "Forth"

    print("All set? Click \"Check\" to review your code and earn rewards!")

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    conjunction = {(0, 0): 0, (1, 0): 0, (0, 1): 0, (1, 1): 1}
    disjunction = {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 1}
    implication = {(0, 0): 1, (1, 0): 0, (0, 1): 1, (1, 1): 1}
    exclusive = {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 0}
    equivalence = {(0, 0): 1, (1, 0): 0, (0, 1): 0, (1, 1): 1}
    operations = {"conjunction": conjunction, "disjunction": disjunction, "implication": implication,
                  "exclusive": exclusive, "equivalence": equivalence}

    operation = operations[operation]

    return operation[(x, y)]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

    print("All done? Earn rewards by using the 'Check' button!")

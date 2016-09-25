def check_line(line):
    sequence = {"X": "Z", "Z": "X"}
    quality = True
    for i in range(len(line) - 1):
        if line[i + 1] != sequence.get(line[i]):
            quality = False
            break

    return quality


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_line(["X", "Z", "X"]) == True
    assert check_line(["X", "Z", "X", "X"]) == False
    assert check_line(["X", "Z"]) == True
    assert check_line(["Z", "X"]) == True
    assert check_line(["Z", "X", "Z", "X", "Z", "Z", "X"]) == False

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

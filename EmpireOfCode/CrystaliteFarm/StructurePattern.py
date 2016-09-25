def check_structure(pattern, structure, pattern_level=2):
    isdigit = lambda x: x.isdigit()
    isalpha = lambda x: x.isalpha()
    isalphalower = lambda x: x.isalpha() and x.islower()
    isalphaupper = lambda x: x.isalpha() and x.isupper()
    isspace = lambda x: x == ' '

    decode = {2:[isdigit,isalpha], 3:[isdigit,isalphalower,isalphaupper], 4:[isdigit,isalphalower,isalphaupper,isspace]}

    dl = str_base(pattern, pattern_level)

    if len(structure) < len(dl):
        return False

    if len(structure) > len(dl):
        for i in range(len(structure) - len(dl)):
            dl = '0' + dl

    print("Pattern : %s" % dl)
    print("Structure : %s" % structure)

    for i in range(len(structure)):
        if not decode.get(pattern_level)[int(dl[i])](structure[i]):
            return False

    return True

def digit_to_char(digit):
    if digit < 10: return chr(ord('0') + digit)
    else: return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number,base)
    else:
        (d,m) = divmod(number,base)
        if d:
            return str_base(d,base) + digit_to_char(m)
        else:
            return digit_to_char(m)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert check_structure(42, "12a0b3e4"), "42 is the answer"
    assert not check_structure(101, "ab23b4zz"), "one hundred plus one"
    assert check_structure(0, "478103487120470129"), "Any number"
    assert check_structure(127, "Checkio"), "Uppercase"
    assert not check_structure(7, "Hello"), "Only full match"
    assert not check_structure(8, "a"), "Too short command"
    assert check_structure(5, "H2O"), "Water"
    assert not check_structure(42, "C2H5OH"), "Yep, this is not the Answer"

    # Rank 2
    assert check_structure(1823, 'CheckiO', 3), "up and down"
    assert not check_structure(1826, 'CheckiO', 3), "wrong up and down"
    assert check_structure(66431, '9z1b2c4d6a7Z', 3), "Various"

    # Rank 3
    assert not check_structure(39294315, 'Kill Them ALL', 4), "Don't kill"
    assert not check_structure(29, 'aXz', 4), "A Z"
    assert check_structure(39294442, 'Feed Them ALL', 4), "Feed them"
    assert check_structure(2385166685525, 'C3PO and 300 spartans', 4), "C3PO"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
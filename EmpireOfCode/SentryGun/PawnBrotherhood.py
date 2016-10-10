def safe_pawns(pawns):
    total = 0


    for pawn in pawns:
        defenders = []

        if int(pawn[1]) > 1:
            if pawn[0] > 'a':
                defenders.append(chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1))
            if pawn[0] < 'h':
                defenders.append(chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1))

        for defender in defenders:
            if defender in pawns:
                total += 1
                break

    return total



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

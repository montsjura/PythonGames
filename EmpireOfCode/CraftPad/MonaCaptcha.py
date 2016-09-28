FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")

# Transform digits into binary
FONTS = {"010110010010010":1,"111001011100111":2,"111001010001111":3,"101101111001001":4, "111100110001110":5, "011100111101011":6, "111001010100100":7, "111101111101111":8, "011101111001110":9, "110101101101011":0}


def recognize(image):
    lines = []

    # Transform the matrix to handle strings
    for line in image:
        lines.append(''.join(str(e) for e in line))


    length = len(lines[0])
    indexDigit = 0
    result = ''

    while length - indexDigit*4 - 1 > 0:
        # Build the string corresponding to the current digit
        digit = ''
        for line in lines:
            digit += line[1+indexDigit*4:4+indexDigit*4]

        # Search the digit (xor gives a binary with one single 1 to match)
        for key in FONTS.keys():
            diff = int(key, base=2)^int(digit, base=2)

            if str(bin(diff)).count('1') <= 1:
                result += str(FONTS.get(key))
                break

        indexDigit += 1

    return int(result)



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"

    print("Earn cool rewards by using the 'Check' button!")

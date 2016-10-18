def recall_password(cipher_grille, ciphered_password):
    clearPwd = ""
    clockwise = ciphered_password[0][0].islower()

    for k in range(4):
        # Decode the password
        for i in range (len(cipher_grille)):
            for j in range(len(cipher_grille)):
                if cipher_grille[i][j] == "X":
                    clearPwd += ciphered_password[i][j]

        # Rotate the cipher
        cipher_grille = rotate(cipher_grille, clockwise)
    print(clearPwd)
    return clearPwd

def rotate(matrix, clockwise):
    # Transpose the matrix
    length = len(matrix)
    # for i in range(length): print(matrix[i])
    matrix = list(zip(*matrix))


    rotatedMatrix = [['' for x in range(length)] for y in range(length)]
    # Invert the columns to get clockwise rotation
    if clockwise:
        for i in range(length):
            for j in range(length):
                rotatedMatrix[i][j] = matrix[i][length - 1 - j]
    # Invert the rows to get counterclockwise rotation
    else:
        for i in range(len(matrix)):
            rotatedMatrix[i] = matrix[length - 1 - i]

    # print()
    # print()
    # print()
    # for i in range(length): print(rotatedMatrix[i])

    return rotatedMatrix





if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

    # Rank 2
    assert recall_password(
        ('.X...X.',
         'X.....X',
         '.......',
         '...X...',
         '.......',
         'X.....X',
         '.X...X.'),
        ('loremip',
         'sumdolo',
         'rsitame',
         'tconsec',
         'teturad',
         'ipiscin',
         'gelitqu')) == "oisonineqoisonineqoisonineqoisonineq", "R2"

    # Rank 3
    assert recall_password(
        ('.X...',
         '.X...',
         '..X..',
         '.X...',
         '.X...'),
        ('QWERT',
         'ASDFG',
         'ZXCVB',
         'YUIOP',
         'GHJKL')) == "WSCUHCYUOPRFCOKASFGC", "R3"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

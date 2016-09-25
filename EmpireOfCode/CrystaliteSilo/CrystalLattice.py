def golf(cube):
    sequence = {'X': 'Z', 'Z': 'X'}
    print(cube)

    for k in range(2):
        for i in range(len(cube)):
            for j in range(len(cube[i]) - 1):
                # Check horizontally
                if cube[i][j + 1] != sequence.get(cube[i][j]):
                    return False

        # Transpose the matrix
        cube = list(zip(*cube))


    return True
if __name__ == "__main__":
    assert golf([[["X", "Z"],
                  ["Z", "X"]],
                 [["Z", "X"],
                  ["X", "Z"]]]) == True, "1st example"
    assert golf([[["X", "Z"],
                  ["Z", "X"]],
               [["X", "Z"],
                  ["Z", "X"]]]) == False, "2nd example"
    print("All done? Earn rewards by using the 'Check' button!")

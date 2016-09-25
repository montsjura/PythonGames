def check_grid(grid):
    sequence = {'X': 'Z', 'Z': 'X'}

    for k in range(2):
        for i in range(len(grid)):
            for j in range(len(grid[i]) - 1):
                # Check horizontally
                if grid[i][j + 1] != sequence.get(grid[i][j]):
                    print("(%i,%i) : %s is different from %s --> return False" % (
                    i, j, grid[i][j + 1], sequence.get(grid[i][j])))
                    return False

        # Transpose the matrix
        grid = list(zip(*grid))

    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_grid([["X", "Z"], ["Z", "X"]]), "2x2 Good"
    assert check_grid([["X", "Z", "X"],
                       ["Z", "X", "Z"],
                       ["X", "Z", "X"]]), "3x3 Good"
    assert check_grid([["X", "Z", "X", "Z"],
                       ["Z", "X", "Z", "X"]]), "2x4 Good"
    assert not check_grid([["X", "X"],
                           ["X", "X"]]), "2x2 Bad"
    assert not check_grid([["X", "Z", "X"],
                           ["Z", "Z", "Z"],
                           ["X", "Z", "X"]]), "3x3 Bad"
    assert not check_grid([["X", "Z", "X", "Z"],
                           ["X", "Z", "X", "Z"]]), "2x4 Bad"

    print("Use 'Check' to earn sweet rewards!")

def count_neighbours(grid, row, col):
    nbEnemy = 0

    # Count at below
    if row-1 >= 0:
        nbEnemy += grid[row - 1][col]
        if col-1 >=0:
            nbEnemy += grid[row-1][col-1]
        if col+1<len(grid[0]):
            nbEnemy += grid[row-1][col+1]

    # Count at center
    if col-1 >= 0:
        nbEnemy += grid[row][col-1]
    if col+1 < len(grid[0]):
        nbEnemy += grid[row][col+1]

    # Count at bottom
    if row+1 < len(grid):
        nbEnemy += grid[row + 1][col]
        if col - 1 >= 0:
            nbEnemy += grid[row+1][col-1]
        if col + 1 < len(grid[0]):
            nbEnemy += grid[row+1][col+1]


    return nbEnemy




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
    assert count_neighbours(((1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),
                             (1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),
                             (1, 1, 1, 0, 1),
                             (0, 1, 0, 1, 0)), 5, 0) == 3
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
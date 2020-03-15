'''solve the given Sudoku puzzle recursively
Rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
'''
# https://youtu.be/G_UYXzGuqvM
grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]
grid1 = [
    [0,0,0,0,0,0,0,0,0],
    [3,1,0,4,0,5,0,8,2],
    [6,0,0,0,0,0,0,0,5],
    [0,0,6,3,5,1,2,0,0],
    [0,2,3,0,0,0,7,1,0],
    [0,8,0,0,0,0,0,5,0],
    [0,6,0,1,0,2,0,7,0],
    [0,0,4,5,0,3,8,0,0],
    [0,0,8,0,7,0,5,0,0],
]

# define the puzzle row (y) and each row contains the elements (x)
# define function possible() to test if a given number (n) is possible to be in a given position
# define function solve() and try all possible numbers recursively

import numpy as np      # for formatting display only
# takes a position in the grid and position (y, x)
# test if number n can be put in the position
# first test the column and row (y, x) already contain the number, if yes, return false
# then test the square in position (y, x) in top left corner contains n, if yes, return false
def possible(grid, y, x, n):
    for i in range(1, 9):      # check column, rule #1
        if grid[y][i] == n:
            return False
    for j in range(1, 9):      # check row, rule #2
        if grid[j][x] == n:
            return False

    # check for square, rule #3
    x0 = (x // 3) * 3       # brings the number to top left corner of the square
    y0 = (y // 3) * 3
    for k in range(0, 3):
        for l in range(0, 3):   # check the square with n on top left
            if grid[y0 + k][x0 + l] == n:
                return False
    return True
    # print(possible(4,4,3)) should be False
    # print(possible(4,4,5)) should return True

def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:     # find an empty position
                for n in range(1, 10):  # try to find a number that can be put in here
                    if possible(grid, y, x, n):
                        grid[y][x] = n      # put k in there if possible returns True
                        solve(grid)         # calls solve() again to find next empty space
                        grid[y][x] = 0      # didn't work
                return                      # deadend, go back up and try another number
    print(np.matrix(grid))                  # tried everything, no more empty space = done
    input("More?")      # this pauses before displaying the next solution



#print(possible(4,4,3))
#print(possible(4,4,5))
print(np.matrix(grid1))
solve(grid)

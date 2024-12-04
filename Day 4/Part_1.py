import numpy as np
import re

# Intuition for this problem, either:
# 1. One pass through text file getting square:
# 2. Multiple passes for each direction:
# Back/forth: Row-wise, Column-wise, Diagonal-wise(left/right, right/left)

def reader(file):
    """Helper function, reads a file and returns a numpy matrix of lines."""
    with open(file) as f:
        lines = [line.strip() for line in f]
    matrix = [list(line) for line in lines]
    return np.array(matrix)

def get_rows(matrix):
    """Returns the rows of the matrix as lists."""
    return [list(row) for row in matrix]

def get_columns(matrix):
    """Returns the columns of the matrix as lists."""
    return [list(col) for col in matrix.T]

def get_diagonals(matrix):
    """Returns the diagonals of the matrix as lists."""
    l2r_diags = []
    r2l_diags = []
    # left to right diagonals
    for offset in range(-matrix.shape[0] + 1, matrix.shape[1]):
        l2r_diags.append(list(np.diagonal(matrix, offset=offset)))
    # right to left diagonals
    for offset in range(-matrix.shape[0] + 1, matrix.shape[1]):
        r2l_diags.append(list(np.diagonal(np.fliplr(matrix), offset=offset)))
    return l2r_diags, r2l_diags

def get_all(matrix):
    """Returns all rows, columns, and diagonals of the matrix."""
    diags = get_diagonals(matrix)
    return [get_rows(matrix), get_columns(matrix), diags[0], diags[1]]

def finder(data):
    """Finds occurrences of the pattern 'XMAS' in the data."""
    pattern = r"XMAS"
    normal = "".join(data)
    reverse = "".join(data[::-1])
    return re.findall(pattern, normal) + re.findall(pattern, reverse)

if __name__ == '__main__':
    # Read the input file and convert it to a numpy matrix
    data = reader(r'Day 4\input.txt')
    # Get all rows, columns, and diagonals of the matrix
    poss = get_all(data)
    cnt = 0
    # Iterate through all directions and count occurrences of the pattern
    for direction in poss:
        for line in direction:
            cnt += len(finder(line))
    # Print the total count of occurrences
    print(cnt)
import numpy as np

# Intuition: Find 'A's and check the corners
# Easier than previous part?

def reader(file):
    """Helper function, reads a file and returns a numpy matrix of lines."""
    with open(file) as f:
        lines = [line.strip() for line in f]
    matrix = [list(line) for line in lines]
    return np.array(matrix)

def check_corner(i, j):
    """Check if the corners around the 'A' at (i, j) match the required pattern."""
    if (data[i-1, j-1] == 'M' and data[i+1, j+1] == "S" or data[i-1, j-1] == 'S' and data[i+1, j+1] == "M") and \
       (data[i-1, j+1] == 'M' and data[i+1, j-1] == "S" or data[i-1, j+1] == 'S' and data[i+1, j-1] == "M"):
        return True

if __name__ == '__main__':
    # Read the input data from the file
    data = reader(r'Day 4\input.txt')
    cnt = 0
    # Iterate through the matrix to find 'A's
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            # Check if the current element is 'A' and not on the border
            if data[i, j] == 'A' and 0 < i < data.shape[0] - 1 and 0 < j < data.shape[1] - 1:
                # Check if the corners around 'A' match the required pattern
                if check_corner(i, j):
                    cnt += 1
    print(cnt)
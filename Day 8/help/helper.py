help = [(0, 11), (3, 2), (5, 6), (7, 5), (9, 4), (11, 3), (7, 0), (1, 3), (0, 1), (4, 9), (5, 11), (0, 6), (6, 3), (8, 2), (10, 1), (2, 10), (5, 1), (2, 4), (11, 10), (1, 3), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0), (10, 10), (11, 11)]
from collections import defaultdict
def reader(file):
    with open(file) as f:
        matrix = [list(line.strip()) for line in f]
    return matrix

def create_dict(matrix):
    dict = defaultdict(list)
    n,m = len(matrix), len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '.':
                dict[matrix[i][j]].append((i,j))
    return dict,n,m

if '__main__' == __name__:
    mat = reader(r'Day 8\example_ans.txt')
    print(mat)
    tmp = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != '.' and (i,j) not in help:
                tmp.append((i,j))
    print(tmp)
    print(len(tmp))
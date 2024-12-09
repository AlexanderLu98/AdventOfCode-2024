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

def find_anti_nodes(antennas,n,m):
    anti_nodes = []
    for key in antennas:
        for i in range(len(antennas[key])):
            for j in range(i+1, len(antennas[key])):
                x1, y1 = antennas[key][i]
                x2, y2 = antennas[key][j]
                x_dist = x1 - x2
                y_dist = y1 - y2
                #create antinodes
                anti_1 = (x1 + x_dist, y1 + y_dist)
                anti_2 = (x2 - x_dist, y2 - y_dist)
                if anti_1[0] >= 0 and anti_1[0] < m and anti_1[1] >= 0 and anti_1[1] < n:
                    anti_nodes.append(anti_1)
                if anti_2[0] >= 0 and anti_2[0] < m and anti_2[1] >= 0 and anti_2[1] < n:
                    anti_nodes.append(anti_2)
    return anti_nodes


if __name__ == '__main__':
    matrix = reader(r'Day 8\input.txt')
    antennas,n,m = create_dict(matrix)
    anti_nodes = find_anti_nodes(antennas,n,m)
    # all_antennas = [item for sublist in antennas.values() for item in sublist]
    # valid = [anti_nodes[i] for i in range(len(anti_nodes)) if anti_nodes[i] not in all_antennas]
    # invalid = [anti_nodes[i] for i in range(len(anti_nodes)) if anti_nodes[i] in all_antennas]
    # print(antennas)
    # print(invalid)
    print(len(set(anti_nodes)))

    #too low, 329
    #too high 361
    #manual binary search lol
    #correct: 336
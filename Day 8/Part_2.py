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
                #resonant anti nodes:
                #first
                while x1 >= 0 and x1 < m and y1 >= 0 and y1 < n:
                    anti_nodes.append((x1, y1))
                    x1 += x_dist
                    y1 += y_dist

                #second
                while x2  >= 0 and x2  < m and y2  >= 0 and y2  < n:
                    anti_nodes.append((x2, y2))
                    x2 -= x_dist
                    y2 -= y_dist
    return anti_nodes


if __name__ == '__main__':
    matrix = reader(r'Day 8\input.txt')
    antennas,n,m = create_dict(matrix)
    anti_nodes = find_anti_nodes(antennas,n,m)
    print(anti_nodes)
    print(len(set(anti_nodes)))

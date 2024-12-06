def reader(file):
    with open(file) as f:
        return [line.strip() for line in f]

def find_guard_pos_and_dir(map_data):
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    for r, row in enumerate(map_data):
        for c, char in enumerate(row):
            if char in dirs:
                return (r, c), dirs[char], char
    return None, None, None

def turn_right(dir):
    if dir == (-1, 0):  # Up
        return (0, 1)  # Right
    elif dir == (0, 1):  # Right
        return (1, 0)  # Down
    elif dir == (1, 0):  # Down
        return (0, -1)  # Left
    elif dir == (0, -1):  # Left
        return (-1, 0)  # Up

def simulate_guard(map_data):
    pos, dir, initial_char = find_guard_pos_and_dir(map_data)
    if pos is None:
        return 0

    rows, cols = len(map_data), len(map_data[0])
    visited = set()
    visited.add(pos)
    loop = []
    while True:
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break
        
        if map_data[next_pos[0]][next_pos[1]] == '#':
            loop.append(pos)
            dir = turn_right(dir)
        else:
            pos = next_pos
            visited.add(pos)

    return len(visited)

def simulate_guard_sec(map_data,limit):
    pos, dir, initial_char = find_guard_pos_and_dir(map_data)
    if pos is None:
        return 0

    rows, cols = len(map_data), len(map_data[0])
    visited = set()
    visited.add(pos)
    loop = []
    while True:
        if len(visited) > limit:
            return False
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break
        
        if map_data[next_pos[0]][next_pos[1]] == '#':
            loop.append(pos)
            dir = turn_right(dir)
        else:
            pos = next_pos
            visited.add(pos)

    return True


if __name__ == '__main__':
    map_data = reader(r'Day 6\example.txt')
    path = simulate_guard(map_data)
    for i in range(len(map_data[0])):
        for j in range(len(map_data[1])):
            new_map = [list(row) for row in map_data]
            new_map[i][j] = '#'
            new_map = [''.join(row) for row in new_map]
            if simulate_guard_sec(new_map,path):
                print(i, j)
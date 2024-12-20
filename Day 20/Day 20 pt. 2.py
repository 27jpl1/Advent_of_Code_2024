import sys
from collections import deque

race = open("Race", "r")
sys.setrecursionlimit(10000)
start = ()
end = ()
grid = []
for i, line in enumerate(race):
    row = []
    for j, char in enumerate(line.strip()):
        if char == "S":
            start = (i, j)
        elif char == "E":
            end = (i, j)
        row.append(char)
    grid.append(row)

dist_to_end = {}
seen = set()
path = []


def count_bfs(grid, row, col):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    seen.add((row, col))
    path.append((row, col))
    if grid[row][col] == "E":
        dist_to_end[(row, col)] = 0
        return 0
    for dir in directions:
        if grid[row + dir[0]][col + dir[1]] != "#" and (row + dir[0], col + dir[1]) not in seen:
            dist_to_end[(row, col)] = 1 + count_bfs(grid, row + dir[0], col + dir[1])
            return dist_to_end[(row, col)]


count_bfs(grid, start[0], start[1])
total = 0
for i in range(0, len(path)):
    for j in range(i + 1, len(path)):
        manhat_dist = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
        if manhat_dist <= 20:
            if (dist_to_end[path[i]] - dist_to_end[path[j]]) - manhat_dist >= 100:
                total += 1

print(total)

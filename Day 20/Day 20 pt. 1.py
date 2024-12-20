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


def count_bfs(grid, row, col):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    seen.add((row, col))
    if grid[row][col] == "E":
        dist_to_end[(row, col)] = 0
        return 0
    for dir in directions:
        if grid[row + dir[0]][col + dir[1]] != "#" and (row + dir[0], col + dir[1]) not in seen:
            dist_to_end[(row, col)] = 1 + count_bfs(grid, row + dir[0], col + dir[1])
            return dist_to_end[(row, col)]


count_bfs(grid, start[0], start[1])
queue = deque()
queue.append(start)
checked = set()
total = 0
while queue:
    row, col = queue.popleft()
    checked.add((row, col))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dir in directions:
        up = dir[0]
        left = dir[1]
        if grid[row + up][col + left] == "#" and (row + up, col + left) not in checked:
            checked.add((row + up, col + left))
            for new_dir in directions:
                new_row = row + up + new_dir[0]
                new_col = col + left + new_dir[1]
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]):
                    if grid[new_row][new_col] != "#" and (new_row, new_col) not in checked:
                        if (dist_to_end[(row, col)] - dist_to_end[(new_row, new_col)]) - 2 >= 100:
                            total += 1
        if grid[row + up][col + left] == "." and (row + up, col + left) not in checked:
            queue.append((row + up, col + left))

print(total)

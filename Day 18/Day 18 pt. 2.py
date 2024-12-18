from collections import deque

falling = open("Falling Bytes", "r")

memory = []
for i in range(0, 71):
    memory.append(["."] * 71)


def bfs(grid):
    queue = deque()
    queue.append((0, 0))
    seen = {(0, 0)}
    parents = {}
    while queue:
        row, col = queue.popleft()
        if (row, col) == (70, 70):
            return True
        else:
            if row - 1 >= 0 and (row - 1, col) not in seen and grid[row - 1][col] == ".":
                queue.append((row - 1, col))
                seen.add((row - 1, col))
                parents[(row - 1, col)] = (row, col)
            if col - 1 >= 0 and (row, col - 1) not in seen and grid[row][col - 1] == ".":
                queue.append((row, col - 1))
                seen.add((row, col - 1))
                parents[(row, col - 1)] = (row, col)
            if row + 1 < len(grid) and (row + 1, col) not in seen and grid[row + 1][col] == ".":
                queue.append((row + 1, col))
                seen.add((row + 1, col))
                parents[(row + 1, col)] = (row, col)
            if col + 1 < len(grid[row]) and (row, col + 1) not in seen and grid[row][col + 1] == ".":
                queue.append((row, col + 1))
                seen.add((row, col + 1))
                parents[(row, col + 1)] = (row, col)
    return False


for i, line in enumerate(falling):
    line = line.strip().split(",")
    x, y = map(int, line)
    memory[y][x] = "#"
    if not bfs(memory):
        print(x, y)
        break

from collections import deque

top_map = open("Topographic Map", "r")

tmap = []
for line in top_map:
    row = []
    for char in line.strip():
        row.append(int(char))
    tmap.append(row)


def follow_trail(row, col):
    trails_found = 0
    visited = {(row, col)}
    queue = deque()
    queue.append((row, col))
    while len(queue) > 0:
        row, col = queue.pop()
        curr_val = tmap[row][col]
        if curr_val == 9:
            trails_found += 1
        else:
            if row - 1 >= 0 and tmap[row - 1][col] == curr_val + 1:
                visited.add((row - 1, col))
                queue.append((row - 1, col))
            if row + 1 < len(tmap) and tmap[row + 1][col] == curr_val + 1:
                visited.add((row + 1, col))
                queue.append((row + 1, col))
            if col - 1 >= 0 and tmap[row][col - 1] == curr_val + 1:
                visited.add((row, col - 1))
                queue.append((row, col - 1))
            if col + 1 < len(tmap[row]) and tmap[row][col + 1] == curr_val + 1:
                visited.add((row, col + 1))
                queue.append((row, col + 1))
    return trails_found


total = 0
for i in range(0, len(tmap)):
    for j in range(0, len(tmap[i])):
        if tmap[i][j] == 0:  # Start of a trailhead
            total += follow_trail(i, j)

print(total)

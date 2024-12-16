from heapq import heappop, heappush
from collections import deque

race_map = open("Race Map", "r")
r_map = []
start = ()
end = ()
for i, line in enumerate(race_map):
    row = []
    for j, char in enumerate(line.strip()):
        if char == "E":
            end = (i, j)
        if char == "S":
            start = (0, i, j, "E")
        row.append(char)
    r_map.append(row)

seen = set()
s_score, s_row, s_col, s_dir = start
heap = [(s_score, s_row, s_col, s_dir, 0, 0, 0, 0)]
best_score = {}
parents = {}
final_state = ()
while len(heap) > 0:
    score, row, col, dir, old_score, old_row, old_col, old_dir = heappop(heap)
    if (row, col) == end:
        parents[row, col, dir] = [(old_row, old_col, old_dir)]
        final_state = (row, col, dir)
        break
    if (row, col, dir) in seen:
        if score < best_score[row, col, dir]:
            print("Something is wrong")
        elif score == best_score[row, col, dir]:
            parents[row, col, dir].append((old_row, old_col, old_dir))
    else:
        seen.add((row, col, dir))
        best_score[(row, col, dir)] = score
        parents[(row, col, dir)] = [(old_row, old_col, old_dir)]
        if dir == "E":
            if r_map[row][col + 1] != "#":
                heappush(heap, (score + 1, row, col + 1, "E", score, row, col, dir))
            heappush(heap, (score + 1000, row, col, "N", score, row, col, dir))
            heappush(heap, (score + 1000, row, col, "S", score, row, col, dir))
        if dir == "S":
            if r_map[row + 1][col] != "#":
                heappush(heap, (score + 1, row + 1, col, "S", score, row, col, dir))
            heappush(heap, (score + 1000, row, col, "W", score, row, col, dir))
            heappush(heap, (score + 1000, row, col, "E", score, row, col, dir))
        if dir == "W":
            if r_map[row][col - 1] != "#":
                heappush(heap, (score + 1, row, col - 1, "W", score, row, col, dir))
            heappush(heap, (score + 1000, row, col, "N", score, row, col, dir))
            heappush(heap, (score + 1000, row, col, "S", score, row, col, dir))
        if dir == "N":
            if r_map[row - 1][col] != "#":
                heappush(heap, (score + 1, row - 1, col, "N", score, row, col, dir))
            heappush(heap, (score + 1000, row, col, "W", score, row, col, dir))
            heappush(heap, (score + 1000, row, col, "E", score, row, col, dir))


total = 0
seen_state = set()
queue = deque()
queue.append(final_state)
while len(queue) > 0:
    state = queue.popleft()
    row, col, dir = state
    if (0, row, col, dir) == start:
        break
    if (row, col) not in seen_state:
        total += 1
    seen_state.add((row, col))
    for parent in parents[state]:
        queue.append(parent)
print(total)

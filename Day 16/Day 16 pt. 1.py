from heapq import heappop, heappush


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
heap = [start]
while len(heap) > 0:
    curr_place = heappop(heap)
    score, row, col, dir = curr_place
    if (row, col) == end:
        print(score)
        break
    if (row, col, dir) in seen:
        pass
    else:
        seen.add((row, col, dir))
        if dir == "E":
            if r_map[row][col + 1] != "#":
                heappush(heap, (score + 1, row, col + 1, "E"))
            heappush(heap, (score + 1000, row, col, "N"))
            heappush(heap, (score + 1000, row, col, "S"))
        if dir == "S":
            if r_map[row + 1][col] != "#":
                heappush(heap, (score + 1, row + 1, col, "S"))
            heappush(heap, (score + 1000, row, col, "W"))
            heappush(heap, (score + 1000, row, col, "E"))
        if dir == "W":
            if r_map[row][col - 1] != "#":
                heappush(heap, (score + 1, row, col - 1, "W"))
            heappush(heap, (score + 1000, row, col, "N"))
            heappush(heap, (score + 1000, row, col, "S"))
        if dir == "N":
            if r_map[row - 1][col] != "#":
                heappush(heap, (score + 1, row - 1, col, "N"))
            heappush(heap, (score + 1000, row, col, "W"))
            heappush(heap, (score + 1000, row, col, "E"))

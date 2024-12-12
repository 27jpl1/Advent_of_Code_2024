from collections import deque

garden = open("Garden", "r")

plots = []
for line in garden:
    split_row = []
    for char in line.strip():
        split_row.append(char)
    plots.append(split_row)

visited = set()


def find_region(row, col):
    queue = deque()
    queue.append((row, col))
    label = plots[row][col]
    area = 1
    perimeter = 0
    while len(queue) > 0:
        added_perimeter = 4
        l, k = queue.popleft()
        if l + 1 < len(plots) and plots[l + 1][k] == label:
            added_perimeter -= 1
            if (l + 1, k) not in visited:
                visited.add((l + 1, k))
                queue.append((l + 1, k))
                area += 1
        if k + 1 < len(plots[l]) and plots[l][k + 1] == label:
            added_perimeter -= 1
            if (l, k + 1) not in visited:
                visited.add((l, k + 1))
                queue.append((l, k + 1))
                area += 1
        if l - 1 >= 0 and plots[l - 1][k] == label:
            added_perimeter -= 1
            if (l - 1, k) not in visited:
                visited.add((l - 1, k))
                queue.append((l - 1, k))
                area += 1
        if k - 1 >= 0 and plots[l][k - 1] == label:
            added_perimeter -= 1
            if (l, k - 1) not in visited:
                visited.add((l, k - 1))
                queue.append((l, k - 1))
                area += 1
        perimeter += added_perimeter
    return area * perimeter


total = 0
for i in range(0, len(plots)):
    for j in range(0, len(plots[i])):
        if (i, j) not in visited:
            visited.add((i, j))
            total += find_region(i, j)
print(total)


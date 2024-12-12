from collections import deque

garden = open("Garden", "r")

plots = []
for line in garden:
    split_row = []
    for char in line.strip():
        split_row.append(char)
    plots.append(split_row)

visited = set()


def find_area(row, col):
    region = set()
    queue = deque()
    queue.append((row, col))
    label = plots[row][col]
    area = 1
    while len(queue) > 0:
        l, k = queue.popleft()
        region.add((l, k))
        if l + 1 < len(plots) and (l + 1, k) not in visited and plots[l + 1][k] == label:
            visited.add((l + 1, k))
            queue.append((l + 1, k))
            area += 1
        if k + 1 < len(plots[l]) and (l, k + 1) not in visited and plots[l][k + 1] == label:
            visited.add((l, k + 1))
            queue.append((l, k + 1))
            area += 1
        if l - 1 >= 0 and (l - 1, k) not in visited and plots[l - 1][k] == label:
            visited.add((l - 1, k))
            queue.append((l - 1, k))
            area += 1
        if k - 1 >= 0 and (l, k - 1) not in visited and plots[l][k - 1] == label:
            visited.add((l, k - 1))
            queue.append((l, k - 1))
            area += 1
    return area, region


# Based off of finding corners. The # of corners = # of sides
# If a set of adjacent direction no plots there is a corner
# if a set of adjacent direction has plots and the diagonal between those direction has no plot then there is a corner
def find_perimeter(region):
    sides = 0
    for plot in region:
        row, col = plot
        is_plot_up = row - 1 >= 0 and (row - 1, col) in region
        is_plot_down = row + 1 < len(plots) and (row + 1, col) in region
        is_plot_left = col - 1 >= 0 and (row, col - 1) in region
        is_plot_right = col + 1 < len(plots[row]) and (row, col + 1) in region
        is_plot_up_left = row - 1 >= 0 and col - 1 >= 0 and (row - 1, col - 1) in region
        is_plot_up_right = row - 1 >= 0 and col + 1 < len(plots[row]) and (row - 1, col + 1) in region
        is_plot_down_left = row + 1 < len(plots) and col - 1 >= 0 and (row + 1, col - 1) in region
        is_plot_down_right = row + 1 < len(plots) and col < len(plots[row]) and (row + 1, col + 1) in region
        if not is_plot_up and not is_plot_left:
            sides += 1
        if not is_plot_up and not is_plot_right:
            sides += 1
        if not is_plot_down and not is_plot_right:
            sides += 1
        if not is_plot_down and not is_plot_left:
            sides += 1
        if is_plot_up and is_plot_left and not is_plot_up_left:
            sides += 1
        if is_plot_up and is_plot_right and not is_plot_up_right:
            sides += 1
        if is_plot_down and is_plot_left and not is_plot_down_left:
            sides += 1
        if is_plot_down and is_plot_right and not is_plot_down_right:
            sides += 1
    return sides


total = 0
for i in range(0, len(plots)):
    for j in range(0, len(plots[i])):
        if (i, j) not in visited:
            visited.add((i, j))
            area, region = find_area(i, j)
            sides = find_perimeter(region)
            total += area * sides
print(total)


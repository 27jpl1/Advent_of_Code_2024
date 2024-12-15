warehouse = open("Map", "r")

grid = []
finished_grid = False
robot = ()
moves = []
for i, line in enumerate(warehouse):
    line = line.strip()
    row = []
    if line == "":
        finished_grid = True
    if not finished_grid:
        for j, char in enumerate(line):
            if char == "@":
                robot = (i, j)
            row.append(char)
        grid.append(row)
    else:
        for char in line:
            moves.append(char)

for move in moves:
    row, col = robot
    if move == "^":
        if grid[row - 1][col] != "#":  #The spot above is not a wall or edge
            if grid[row - 1][col] == "O":
                blank_found = False
                wall_found = False
                num_up = 1
                while not blank_found and not wall_found:
                    num_up += 1
                    if grid[row - num_up][col] == ".":
                        blank_found = True
                    if grid[row - num_up][col] == "#":
                        wall_found = True
                if not wall_found:
                    while num_up > 0:
                        grid[row - num_up][col] = "O"
                        num_up -= 1
                    robot = (row - 1, col)
                    grid[row][col] = "."
                    grid[row - 1][col] = "@"
            else:  #Must be an open space
                robot = (row - 1, col)
                grid[row][col] = "."
                grid[row - 1][col] = "@"
    elif move == ">":
        if grid[row][col + 1] != "#":  #The spot above is not a wall or edge
            if grid[row][col + 1] == "O":
                blank_found = False
                wall_found = False
                num_right = 1
                while not blank_found and not wall_found:
                    num_right += 1
                    if grid[row][col + num_right] == ".":
                        blank_found = True
                    if grid[row][col + num_right] == "#":
                        wall_found = True
                if not wall_found:
                    while num_right > 0:
                        grid[row][col + num_right] = "O"
                        num_right -= 1
                    robot = (row, col + 1)
                    grid[row][col] = "."
                    grid[row][col + 1] = "@"
            else:  #Must be an open space
                robot = (row, col + 1)
                grid[row][col] = "."
                grid[row][col + 1] = "@"
    elif move == "<":
        if grid[row][col - 1] != "#":  # The spot above is not a wall or edge
            if grid[row][col - 1] == "O":
                blank_found = False
                wall_found = False
                num_left = 1
                while not blank_found and not wall_found:
                    num_left += 1
                    if grid[row][col - num_left] == ".":
                        blank_found = True
                    if grid[row][col - num_left] == "#":
                        wall_found = True
                if not wall_found:
                    while num_left > 0:
                        grid[row][col - num_left] = "O"
                        num_left -= 1
                    robot = (row, col - 1)
                    grid[row][col] = "."
                    grid[row][col - 1] = "@"
            else:  # Must be an open space
                robot = (row, col - 1)
                grid[row][col] = "."
                grid[row][col - 1] = "@"
    elif move == "v":
        if grid[row + 1][col] != "#":  #The spot above is not a wall or edge
            if grid[row + 1][col] == "O":
                blank_found = False
                wall_found = False
                num_down = 1
                while not blank_found and not wall_found:
                    num_down += 1
                    if grid[row + num_down][col] == ".":
                        blank_found = True
                    if grid[row + num_down][col] == "#":
                        wall_found = True
                if not wall_found:
                    while num_down > 0:
                        grid[row + num_down][col] = "O"
                        num_down -= 1
                    robot = (row + 1, col)
                    grid[row][col] = "."
                    grid[row + 1][col] = "@"
            else:  #Must be an open space
                robot = (row + 1, col)
                grid[row][col] = "."
                grid[row + 1][col] = "@"

total = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == "O":
            total += 100 * i + j
print(total)

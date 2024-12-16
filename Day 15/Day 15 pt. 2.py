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
            if char == "#":
                row.append("#")
                row.append("#")
            elif char == "O":
                row.append("[")
                row.append("]")
            elif char == ".":
                row.append(".")
                row.append(".")
            elif char == "@":
                row.append("@")
                row.append(".")
        grid.append(row)
    else:
        for char in line:
            moves.append(char)

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == "@":
            robot = (i, j)

for move in moves:
    row, col = robot
    if move == "^":
        if grid[row - 1][col] == "#":
            pass
        elif grid[row - 1][col] == "[":
            if grid[row - 2][col] == "#" or grid[row - 2][col + 1] == "#":
                pass
            elif grid[row - 2][col] == "[" or grid[row - 2][col] == "]" or grid[row - 2][col + 1] == "[":
                full_row_available = False
                cant_move = False
                top_boxes = []
                boxes = [(row - 1, col), (row - 1, col + 1)]
                if grid[row - 2][col] == "[":
                    top_boxes.append((row - 2, col))
                    top_boxes.append((row - 2, col + 1))
                    boxes.append((row - 2, col))
                    boxes.append((row - 2, col + 1))
                if grid[row - 2][col] == "]":
                    top_boxes.append((row - 2, col - 1))
                    top_boxes.append((row - 2, col))
                    boxes.append((row - 2, col - 1))
                    boxes.append((row - 2, col))
                if grid[row - 2][col + 1] == "[":
                    top_boxes.append((row - 2, col + 1))
                    top_boxes.append((row - 2, col + 2))
                    boxes.append((row - 2, col + 1))
                    boxes.append((row - 2, col + 2))
                while not full_row_available and not cant_move:
                    new_top_boxes = []
                    num_spaces = 0
                    for box in top_boxes:
                        box_row, box_col = box
                        if grid[box_row - 1][box_col] == "#":
                            cant_move = True
                        elif grid[box_row - 1][box_col] == ".":
                            num_spaces += 1
                        elif grid[box_row - 1][box_col] == "]" and (box_row - 1, box_col) not in new_top_boxes:
                            new_top_boxes.append((box_row - 1, box_col))
                            boxes.append((box_row - 1, box_col))
                            if (box_row - 1, box_col - 1) not in new_top_boxes:
                                new_top_boxes.append((box_row - 1, box_col - 1))
                                boxes.append((box_row - 1, box_col - 1))
                        elif grid[box_row - 1][box_col] == "[" and (box_row - 1, box_col) not in new_top_boxes:
                            new_top_boxes.append((box_row - 1, box_col))
                            boxes.append((box_row - 1, box_col))
                            if (box_row - 1, box_col + 1) not in new_top_boxes:
                                new_top_boxes.append((box_row - 1, box_col + 1))
                                boxes.append((box_row - 1, box_col + 1))
                    if num_spaces == len(top_boxes):
                        full_row_available = True
                    else:
                        top_boxes = new_top_boxes
                if full_row_available and not cant_move:
                    boxes.reverse()
                    for box in boxes:
                        box_row, box_col = box
                        grid[box_row - 1][box_col] = grid[box_row][box_col]
                        grid[box_row][box_col] = "."
                    robot = (row - 1, col)
                    grid[row][col] = "."
                    grid[row - 1][col] = "@"
            else:
                grid[row - 2][col] = "["
                grid[row - 2][col + 1] = "]"
                grid[row - 1][col + 1] = "."
                robot = (row - 1, col)
                grid[row][col] = "."
                grid[row - 1][col] = "@"
        elif grid[row - 1][col] == "]":
            if grid[row - 2][col] == "#" or grid[row - 2][col - 1] == "#":
                pass
            elif grid[row - 2][col] == "[" or grid[row - 2][col] == "]" or grid[row - 2][col - 1] == "]":
                full_row_available = False
                cant_move = False
                top_boxes = []
                boxes = [(row - 1, col), (row - 1, col - 1)]
                if grid[row - 2][col] == "[":
                    top_boxes.append((row - 2, col))
                    top_boxes.append((row - 2, col + 1))
                    boxes.append((row - 2, col))
                    boxes.append((row - 2, col + 1))
                if grid[row - 2][col] == "]":
                    top_boxes.append((row - 2, col - 1))
                    top_boxes.append((row - 2, col))
                    boxes.append((row - 2, col - 1))
                    boxes.append((row - 2, col))
                if grid[row - 2][col - 1] == "]":
                    top_boxes.append((row - 2, col - 1))
                    top_boxes.append((row - 2, col - 2))
                    boxes.append((row - 2, col - 1))
                    boxes.append((row - 2, col - 2))
                while not full_row_available and not cant_move:
                    new_top_boxes = []
                    num_spaces = 0
                    for box in top_boxes:
                        box_row, box_col = box
                        if grid[box_row - 1][box_col] == "#":
                            cant_move = True
                        elif grid[box_row - 1][box_col] == ".":
                            num_spaces += 1
                        elif grid[box_row - 1][box_col] == "]" and (box_row - 1, box_col) not in new_top_boxes:
                            new_top_boxes.append((box_row - 1, box_col))
                            boxes.append((box_row - 1, box_col))
                            if (box_row - 1, box_col - 1) not in new_top_boxes:
                                new_top_boxes.append((box_row - 1, box_col - 1))
                                boxes.append((box_row - 1, box_col - 1))
                        elif grid[box_row - 1][box_col] == "[" and (box_row - 1, box_col) not in new_top_boxes:
                            new_top_boxes.append((box_row - 1, box_col))
                            boxes.append((box_row - 1, box_col))
                            if (box_row - 1, box_col + 1) not in new_top_boxes:
                                new_top_boxes.append((box_row - 1, box_col + 1))
                                boxes.append((box_row - 1, box_col + 1))
                    if num_spaces == len(top_boxes):
                        full_row_available = True
                    else:
                        top_boxes = new_top_boxes
                if full_row_available and not cant_move:
                    boxes.reverse()
                    for box in boxes:
                        box_row, box_col = box
                        grid[box_row - 1][box_col] = grid[box_row][box_col]
                        grid[box_row][box_col] = "."
                    robot = (row - 1, col)
                    grid[row][col] = "."
                    grid[row - 1][col] = "@"
            else:
                grid[row - 2][col] = "]"
                grid[row - 2][col - 1] = "["
                grid[row - 1][col - 1] = "."
                robot = (row - 1, col)
                grid[row][col] = "."
                grid[row - 1][col] = "@"
        else:
            robot = (row - 1, col)
            grid[row][col] = "."
            grid[row - 1][col] = "@"
    elif move == ">":
        if grid[row][col + 1] != "#":
            if grid[row][col + 1] == "[":
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
                        grid[row][col + num_right] = grid[row][col + num_right - 1]
                        num_right -= 1
                    robot = (row, col + 1)
                    grid[row][col] = "."
                    grid[row][col + 1] = "@"
            else:  #Must be an open space
                robot = (row, col + 1)
                grid[row][col] = "."
                grid[row][col + 1] = "@"
    elif move == "<":
        if grid[row][col - 1] != "#":
            if grid[row][col - 1] == "]":
                blank_found = False
                wall_found = False
                num_right = 1
                while not blank_found and not wall_found:
                    num_right += 1
                    if grid[row][col - num_right] == ".":
                        blank_found = True
                    if grid[row][col - num_right] == "#":
                        wall_found = True
                if not wall_found:
                    while num_right > 0:
                        grid[row][col - num_right] = grid[row][col - num_right + 1]
                        num_right -= 1
                    robot = (row, col - 1)
                    grid[row][col] = "."
                    grid[row][col - 1] = "@"
            else:  # Must be an open space
                robot = (row, col - 1)
                grid[row][col] = "."
                grid[row][col - 1] = "@"
    elif move == "v":
        if grid[row + 1][col] == "#":
            pass
        elif grid[row + 1][col] == "[":
            if grid[row + 2][col] == "#" or grid[row + 2][col + 1] == "#":
                pass
            elif grid[row + 2][col] == "[" or grid[row + 2][col] == "]" or grid[row + 2][col + 1] == "[":
                full_row_available = False
                cant_move = False
                top_boxes = []
                boxes = [(row + 1, col), (row + 1, col + 1)]
                if grid[row + 2][col] == "[":
                    top_boxes.append((row + 2, col))
                    top_boxes.append((row + 2, col + 1))
                    boxes.append((row + 2, col))
                    boxes.append((row + 2, col + 1))
                if grid[row + 2][col] == "]":
                    top_boxes.append((row + 2, col - 1))
                    top_boxes.append((row + 2, col))
                    boxes.append((row + 2, col - 1))
                    boxes.append((row + 2, col))
                if grid[row + 2][col + 1] == "[":
                    top_boxes.append((row + 2, col + 1))
                    top_boxes.append((row + 2, col + 2))
                    boxes.append((row + 2, col + 1))
                    boxes.append((row + 2, col + 2))
                while not full_row_available and not cant_move:
                    new_top_boxes = []
                    num_spaces = 0
                    for box in top_boxes:
                        box_row, box_col = box
                        if grid[box_row + 1][box_col] == "#":
                            cant_move = True
                        elif grid[box_row + 1][box_col] == ".":
                            num_spaces += 1
                        elif grid[box_row + 1][box_col] == "]" and (box_row + 1, box_col) not in new_top_boxes:
                            new_top_boxes.append((box_row + 1, box_col))
                            boxes.append((box_row + 1, box_col))
                            if (box_row + 1, box_col + 1) not in new_top_boxes:
                                new_top_boxes.append((box_row + 1, box_col - 1))
                                boxes.append((box_row + 1, box_col - 1))
                        elif grid[box_row + 1][box_col] == "[" and (box_row + 1, box_col) not in new_top_boxes:
                            new_top_boxes.append((box_row + 1, box_col))
                            boxes.append((box_row + 1, box_col))
                            if (box_row + 1, box_col + 1) not in new_top_boxes:
                                new_top_boxes.append((box_row + 1, box_col + 1))
                                boxes.append((box_row + 1, box_col + 1))
                    if num_spaces == len(top_boxes):
                        full_row_available = True
                    else:
                        top_boxes = new_top_boxes
                if full_row_available and not cant_move:
                    boxes.reverse()
                    for box in boxes:
                        box_row, box_col = box
                        grid[box_row + 1][box_col] = grid[box_row][box_col]
                        grid[box_row][box_col] = "."
                    robot = (row + 1, col)
                    grid[row][col] = "."
                    grid[row + 1][col] = "@"
            else:
                grid[row + 2][col] = "["
                grid[row + 2][col + 1] = "]"
                grid[row + 1][col + 1] = "."
                robot = (row + 1, col)
                grid[row][col] = "."
                grid[row + 1][col] = "@"
        elif grid[row + 1][col] == "]":
            if grid[row + 2][col] == "#" or grid[row + 2][col - 1] == "#":
                pass
            elif grid[row + 2][col] == "[" or grid[row + 2][col] == "]" or grid[row + 2][col - 1] == "]":
                full_row_available = False
                cant_move = False
                top_boxes = []
                boxes = [(row + 1, col), (row + 1, col - 1)]
                if grid[row + 2][col] == "[":
                    top_boxes.append((row + 2, col))
                    top_boxes.append((row + 2, col + 1))
                    boxes.append((row + 2, col))
                    boxes.append((row + 2, col + 1))
                if grid[row + 2][col] == "]":
                    top_boxes.append((row + 2, col - 1))
                    top_boxes.append((row + 2, col))
                    boxes.append((row + 2, col - 1))
                    boxes.append((row + 2, col))
                if grid[row + 2][col - 1] == "]":
                    top_boxes.append((row + 2, col - 1))
                    top_boxes.append((row + 2, col - 2))
                    boxes.append((row + 2, col - 1))
                    boxes.append((row + 2, col - 2))
                while not full_row_available and not cant_move:
                    new_top_boxes = []
                    num_spaces = 0
                    for box in top_boxes:
                        box_row, box_col = box
                        if grid[box_row + 1][box_col] == "#":
                            cant_move = True
                        elif grid[box_row + 1][box_col] == ".":
                            num_spaces += 1
                        elif grid[box_row + 1][box_col] == "]" and (box_row + 1, box_col) not in new_top_boxes:
                            new_top_boxes.append((box_row + 1, box_col))
                            boxes.append((box_row + 1, box_col))
                            if (box_row + 1, box_col - 1) not in new_top_boxes:
                                new_top_boxes.append((box_row + 1, box_col - 1))
                                boxes.append((box_row + 1, box_col - 1))
                        elif grid[box_row + 1][box_col] == "[" and (box_row + 1, box_col) not in new_top_boxes:
                            new_top_boxes.append((box_row + 1, box_col))
                            boxes.append((box_row + 1, box_col))
                            if (box_row + 1, box_col + 1) not in new_top_boxes:
                                new_top_boxes.append((box_row + 1, box_col + 1))
                                boxes.append((box_row + 1, box_col + 1))
                    if num_spaces == len(top_boxes):
                        full_row_available = True
                    else:
                        top_boxes = new_top_boxes
                if full_row_available and not cant_move:
                    boxes.reverse()
                    for box in boxes:
                        box_row, box_col = box
                        grid[box_row + 1][box_col] = grid[box_row][box_col]
                        grid[box_row][box_col] = "."
                    robot = (row + 1, col)
                    grid[row][col] = "."
                    grid[row + 1][col] = "@"
            else:
                grid[row + 2][col] = "]"
                grid[row + 2][col - 1] = "["
                grid[row + 1][col - 1] = "."
                robot = (row + 1, col)
                grid[row][col] = "."
                grid[row + 1][col] = "@"
        else:
            robot = (row + 1, col)
            grid[row][col] = "."
            grid[row + 1][col] = "@"


total = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == "[":
            total += 100 * i + j

print(total)

import itertools
import sys
from collections import deque
from itertools import product

file = open("Codes", "r")

codes = []
for line in file:
    codes.append(line.strip())

num_pad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
dir_pad = [[None, "^", "A"], ["<", "v", ">"]]


def solve(code, keypad):
    pos = {}
    for row in range(len(keypad)):
        for col in range(len(keypad[row])):
            if keypad[row][col] is not None:
                pos[keypad[row][col]] = (row, col)
    sequences = {}
    for start in pos:
        for end in pos:
            if start == end:
                sequences[(start, end)] = ["A"]
            else:
                possibilities = []
                queue = deque()
                queue.append((pos[start], ""))
                optimal_len = sys.maxsize
                break_loop = False
                while queue and not break_loop:
                    (row, col), moves = queue.popleft()
                    for new_row, new_col, new_move in [(row - 1, col, "^"), (row + 1, col, "v"), (row, col - 1, "<"), (row, col + 1, ">")]:
                        if 0 <= new_row < len(keypad) and 0 <= new_col < len(keypad[new_row]):
                            if keypad[new_row][new_col] is not None:
                                if keypad[new_row][new_col] == end:
                                    if optimal_len < len(moves) + 1:
                                        break_loop = True
                                    else:
                                        optimal_len = len(moves) + 1
                                        possibilities.append(moves + new_move + "A")
                                else:
                                    queue.append(((new_row, new_col), moves + new_move))
                sequences[(start, end)] = possibilities
    options = [sequences[x, y] for x, y in zip("A" + code, code)]
    return ["".join(x) for x in product(*options)]


total = 0
for code in codes:
    robot_1 = solve(code, num_pad)
    next_robot = robot_1
    for _ in range(2):
        possible_next = []
        for possibility in next_robot:
            possible_next += (solve(possibility, dir_pad))
        min_len = min(map(len, possible_next))
        next_robot = [possibility for possibility in possible_next if len(possibility) == min_len]
    total += len(next_robot[0]) * int(code[:-1])
print(total)


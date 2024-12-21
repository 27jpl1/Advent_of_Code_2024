import sys
from collections import deque
from itertools import product
from functools import cache

file = open("Codes", "r")

codes = []
for line in file:
    codes.append(line.strip())


def compute_sequences(keypad):
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
                    for new_row, new_col, new_move in [(row - 1, col, "^"), (row + 1, col, "v"), (row, col - 1, "<"),
                                                       (row, col + 1, ">")]:
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
    return sequences


def solve(code, sequences):
    options = [sequences[x, y] for x, y in zip("A" + code, code)]
    return ["".join(x) for x in product(*options)]


num_pad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
dir_pad = [[None, "^", "A"], ["<", "v", ">"]]
num_sequences = compute_sequences(num_pad)
dir_sequences = compute_sequences(dir_pad)
dir_lengths = {key: len(value[0]) for key, value in dir_sequences.items()}


@cache
def compute_length(sequence, depth=25):
    if depth == 1:
        return sum(dir_lengths[(x, y)] for x, y in zip("A" + sequence, sequence))
    length = 0
    for x, y in zip("A" + sequence, sequence):
        length += min(compute_length(subsequence, depth - 1) for subsequence in dir_sequences[(x,y)])
    return length


total = 0
for code in codes:
    inputs = solve(code, num_sequences)
    length = min(map(compute_length, inputs))
    total += length * int(code[:-1])
print(total)


from functools import cache

init_arrange = open("Stones", "r")

stones = []
for line in init_arrange:
    line = line.strip().split()
    for char in line:
        stones.append(char)


@cache
def blink(stone, steps):
    if steps == 0:
        return 1
    elif stone == "0":
        return blink("1", steps - 1)
    elif len(stone) % 2 == 0:
        middle = len(stone) // 2
        first_stone = stone[:middle]
        second_stone = stone[middle:]
        while second_stone[0] == "0" and len(second_stone) > 1:
            second_stone = second_stone[1:]
        return blink(first_stone, steps - 1) + blink(second_stone, steps - 1)
    else:
        val = int(stone)
        return blink(str(val * 2024), steps - 1)


num_blinks = 75
total = 0
for stone in stones:
    total += blink(stone, num_blinks)
print(total)

init_arrange = open("Stones", "r")

stones = []
for line in init_arrange:
    line = line.strip().split()
    for char in line:
        stones.append(char)


def blink(stone_arrangement):
    new_arrangement = []
    for stone in stone_arrangement:
        if stone == "0":
            new_arrangement.append("1")
        elif len(stone) % 2 == 0:
            middle = len(stone) // 2
            first_stone = stone[0:middle]
            second_stone = stone[middle:]
            new_arrangement.append(first_stone)
            while second_stone[0] == "0" and len(second_stone) > 1:
                second_stone = second_stone[1:]
            new_arrangement.append(second_stone)
        else:
            val = int(stone)
            new_val = str(val * 2024)
            new_arrangement.append(new_val)
    return new_arrangement


num_blinks = 25
for i in range(0, num_blinks):
    new_stone = blink(stones)
    stones = new_stone

print(len(stones))


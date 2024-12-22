file = open("Secret Numbers", "r")

numbers = []
for line in file:
    numbers.append(int(line.strip()))


def run_day(secret_number):
    secret_number ^= (secret_number * 64)
    secret_number %= 16777216
    secret_number ^= secret_number // 32
    secret_number %= 16777216
    secret_number ^= secret_number * 2048
    secret_number %= 16777216
    return secret_number


def make_change(change):
    change[0] += 1
    if change[0] == 10:
        change[0] = -9
        change[1] += 1
    if change[1] == 10:
        change[1] = -9
        change[2] += 1
    if change[2] == 10:
        change[2] = -9
        change[3] += 1
    return change


max_total = 0
number = 0
changes = [-9, -9, -9, -9]
while changes != [-9, -9, -9, 10]:
    print(changes)
    total = 0
    for number in numbers:
        num = number
        num_changes = []
        found = False
        i = 0
        while i < 2000 and not found:
            old_num = number
            number = run_day(number)
            if len(num_changes) == 4:
                temp = num_changes.pop(0)
                val = number % 10 - old_num % 10
                num_changes.append(val)
                if num_changes == changes:
                    total += number % 10
                    found = True
            else:
                val = number % 10 - old_num % 10
                num_changes.append(val)
            i += 1
    if max_total < total:
        max_total = total
    make_change(changes)
    print(max_total)

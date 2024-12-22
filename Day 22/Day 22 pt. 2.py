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


bananas = {}
for number in numbers:
    seen = set()
    num = number
    num_changes = tuple()
    found = False
    i = 0
    while i < 2000 and not found:
        old_num = number
        number = run_day(number)
        if len(num_changes) == 4:
            val = number % 10 - old_num % 10
            num_changes = (num_changes[1], num_changes[2], num_changes[3], val)
            if num_changes in seen:
                pass
            else:
                seen.add(num_changes)
                if num_changes in bananas.keys():
                    bananas[num_changes] += number % 10
                else:
                    bananas[num_changes] = number % 10
        else:
            if len(num_changes) == 0:
                val = number % 10 - old_num % 10
                num_changes = (val,)
            elif len(num_changes) == 1:
                val = number % 10 - old_num % 10
                num_changes = (num_changes[0], val)
            elif len(num_changes) == 2:
                val = number % 10 - old_num % 10
                num_changes = (num_changes[0], num_changes[1], val)
            elif len(num_changes) == 3:
                val = number % 10 - old_num % 10
                num_changes = (num_changes[0], num_changes[1], num_changes[2], val)
        i += 1

max_total = 0
for banana in bananas.keys():
    if bananas[banana] > max_total:
        max_total = bananas[banana]
print(max_total)

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


total = 0
for number in numbers:
    for i in range(0, 2000):
        number = run_day(number)
    total += number
print(total)

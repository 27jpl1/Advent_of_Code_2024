from functools import cache

file = open("Towels", "r")

towels = []
makes = []
got_towels = False
for line in file:
    line = line.strip()
    if not got_towels:
        towels = line.split(",")
        got_towels = True
    elif line == "":
        pass
    else:
        makes.append(line)

for i in range(0, len(towels)):
    towels[i] = towels[i].strip()


@cache
def make_towel(make):
    if len(make) == 0:
        return 1
    num_makes = 0
    for towel in towels:
        length = len(towel)
        if towel == make[:length]:
            num_makes += make_towel(make[length:])
    return num_makes


total = 0
for make in makes:
    total += make_towel(make)
print(total)

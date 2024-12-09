from unittest.mock import sentinel

file = open("Antennas", "r")

map = []
for line in file:
    map.append(line.strip())

antennas = {}
i = 0
while i < len(map):
    j = 0
    while j < len(map[i]):
        char = map[i][j]
        if char!= ".":
            if char in antennas.keys():
                antennas[char].append((i, j))
            else:
                antennas[char] = [(i, j)]
        j += 1
    i += 1

antinodes = set()
keys = antennas.keys()
for key in keys:  #Adding all the towers
    if len(antennas[key]) > 1:
        for tower in antennas[key]:
            antinodes.add(tower)
for key in keys:
    for k in range(0, len(antennas[key])):
        first_antenna = antennas[key][k]
        for l in range(k + 1, len(antennas[key])):
            second_antenna = antennas[key][l]
            if first_antenna[1] < second_antenna[1]:  # First antenna is to the top left of the second antenna
                x_distance = abs(first_antenna[1] - second_antenna[1])
                y_distance = abs(first_antenna[0] - second_antenna[0])
                new_y_distance = y_distance
                new_x_distance = x_distance
                while first_antenna[0] - new_y_distance >= 0 and first_antenna[1] - new_x_distance >= 0:
                    if (first_antenna[0] - new_y_distance, first_antenna[1] - new_x_distance) in antinodes:
                        pass
                    else:
                        antinodes.add((first_antenna[0] - new_y_distance, first_antenna[1] - new_x_distance))
                    new_x_distance += x_distance
                    new_y_distance += y_distance
                new_y_distance = y_distance
                new_x_distance = x_distance
                while second_antenna[0] + new_y_distance < len(map) and second_antenna[1] + new_x_distance < len(map[0]):
                    if (second_antenna[0] + new_y_distance, second_antenna[1] + new_x_distance) in antinodes:
                        pass
                    else:
                        antinodes.add((second_antenna[0] + new_y_distance, second_antenna[1] + new_x_distance))
                    new_x_distance += x_distance
                    new_y_distance += y_distance
            else:  # First antenna is to the top right of the second antenna
                x_distance = abs(first_antenna[1] - second_antenna[1])
                y_distance = abs(first_antenna[0] - second_antenna[0])
                new_y_distance = y_distance
                new_x_distance = x_distance
                while first_antenna[0] - new_y_distance >= 0 and first_antenna[1] + new_x_distance < len(map[0]):
                    if (first_antenna[0] - new_y_distance, first_antenna[1] + new_x_distance) in antinodes:
                        pass
                    else:
                        antinodes.add((first_antenna[0] - new_y_distance, first_antenna[1] + new_x_distance))
                    new_x_distance += x_distance
                    new_y_distance += y_distance
                new_y_distance = y_distance
                new_x_distance = x_distance
                while second_antenna[0] + new_y_distance < len(map) and second_antenna[1] - new_x_distance >= 0:
                    if (second_antenna[0] + new_y_distance, second_antenna[1] - new_x_distance) in antinodes:
                        pass
                    else:
                        antinodes.add((second_antenna[0] + new_y_distance, second_antenna[1] - new_x_distance))
                    new_x_distance += x_distance
                    new_y_distance += y_distance
print(len(antinodes))

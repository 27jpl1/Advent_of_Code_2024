file = open("Connections", "r")

vertices = set()
connections = {}
for line in file:
    line = line.strip()
    vert1 = line[0:2]
    vert2 = line[3:5]
    if vert1 not in vertices:
        vertices.add(vert1)
    if vert2 not in vertices:
        vertices.add(vert2)
    if vert1 in connections.keys():
        connections[vert1].append(vert2)
    else:
        connections[vert1] = [vert2]
    if vert2 in connections.keys():
        connections[vert2].append(vert1)
    else:
        connections[vert2] = [vert1]

sets = set()
for vertice in vertices:
    for connection in connections[vertice]:
        for second_connection in connections[connection]:
            if vertice in connections[second_connection]:
                computers = (vertice, connection, second_connection)
                sets.add(tuple(sorted(computers)))

total = 0
for computer_set in sets:
    works = False
    for computer in computer_set:
        if computer[0] == "t":
            works = True
    if works:
        total += 1
print(total)


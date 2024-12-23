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

k_3 = set()
for vertice in vertices:
    for connection in connections[vertice]:
        for second_connection in connections[connection]:
            if vertice in connections[second_connection]:
                computers = (vertice, connection, second_connection)
                k_3.add(tuple(sorted(computers)))

k_n = k_3
while len(k_n) > 1:
    new_k_n = set()
    for graph in k_n:
        for key in connections.keys():
            can_add = True
            for computer in graph:
                if computer not in connections[key]:
                    can_add = False
            if can_add:
                new_k_n.add(tuple(sorted(graph + (key,))))
    k_n = new_k_n
print(k_n)


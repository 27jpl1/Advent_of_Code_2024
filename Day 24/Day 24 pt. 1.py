from collections import deque

file = open("Gates", "r")

done_gates = False
gates = {}
queue = deque()
for line in file:
    if line.strip() == "":
        done_gates = True
    else:
        line = line.strip().split()
        if done_gates:
            queue.append(line)
        else:
            gates[line[0][:3]] = int(line[1])

while queue:
    curr_gate = queue.popleft()
    if curr_gate[0] in gates.keys() and curr_gate[2] in gates.keys():
        if curr_gate[1] == "AND":
            gates[curr_gate[4]] = (gates[curr_gate[0]] and gates[curr_gate[2]])
        if curr_gate[1] == "OR":
            gates[curr_gate[4]] = (gates[curr_gate[0]] or gates[curr_gate[2]])
        if curr_gate[1] == "XOR":
            gates[curr_gate[4]] = (gates[curr_gate[0]] ^ gates[curr_gate[2]])
    else:
        queue.append(curr_gate)


z_keys = []
for key in gates.keys():
    if "z" in key:
        z_keys.append(key)

total = 0
z_keys = sorted(z_keys)
for i, key in enumerate(z_keys):
    total += (gates[key] * 2**i)

print(total)

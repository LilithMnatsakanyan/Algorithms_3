graph = {
    '0': ['2', '6', '3'],
    '1': ['4'],
    '2': ['6'],
    '3': ['1', '4'],
    '4': ['5', '8'],
    '5': [],
    '6': ['7', '11'],
    '7': ['4', '12'],
    '8': [],
    '9': ['2', '10'],
    '10': ['6'],
    '11': ['12'],
    '12': ['8'],
    '13': [],
}

indegrees = {} # i-i mej qani hat e mtnum
for node in graph:
    indegrees[node] = 0

for node in graph:
    for neighbor in graph[node]:
        indegrees[neighbor] += 1
print(indegrees)
queue = []
for node in indegrees:
    if indegrees[node] == 0:
        queue.append(node)

final_order = []

while len(queue) > 0:
    current = queue.pop(0)
    final_order.append(current)

    for neighbor in graph[current]:
        indegrees[neighbor] -= 1
        if indegrees[neighbor] == 0:
            queue.append(neighbor)

if len(final_order) != len(graph):
    print("There is a circular dependency.")
else:
    print("Topological Order:", final_order)

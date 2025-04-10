graph = {
    "A": [("B", 3), ("C", 6)],
    "B": [("C", 4), ("D", 4), ("E", 11)],
    "C": [("D", 8), ("G", 11)],
    "D": [("E", -4), ("F", 5), ("G", 2)],
    "E": [("H", 9)],
    "F": [("H", 1)],
    "G": [("H", 2)],
    "H": [],
}

vertices = list(graph.keys())
num_vertices = len(vertices)
in_degree = {v: 0 for v in vertices}
for u in graph:
    for v, weight in graph[u]:
        in_degree[v] += 1

queue = [v for v in in_degree if in_degree[v] == 0]
topo_order = []

while queue:
    u = queue.pop(0)
    topo_order.append(u)

    for v, weight in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

dist = {v: -float('inf') for v in vertices}
dist["A"] = 0

for u in topo_order:
    if dist[u] != -float('inf'):
        for v, weight in graph[u]:
            if dist[v] < dist[u] + weight:
                dist[v] = dist[u] + weight

print("Longest path distances from the source 'A':")
for vertex in dist:
    print(f"From 'A' to {vertex}: {dist[vertex]}")


# ------------------using shortest pathfinding------------------

graph = {
    "A": [("B", 3), ("C", 6)],
    "B": [("C", 4), ("D", 4), ("E", 11)],
    "C": [("D", 8), ("G", 11)],
    "D": [("E", -4), ("F", 5), ("G", 2)],
    "E": [("H", 9)],
    "F": [("H", 1)],
    "G": [("H", 2)],
    "H": [],
}

neg_graph = {}
for u, edges in graph.items():
    neg_graph[u] = []
    for v, w in edges:
        neg_graph[u].append((v, -w))  # -weight

print("Graph with negated weights:")
print(neg_graph)

vertices = list(graph.keys())
num_vertices = len(vertices)
in_degree = {v: 0 for v in vertices}
for u in neg_graph:
    for v, weight in neg_graph[u]:
        in_degree[v] += 1

queue = [v for v in in_degree if in_degree[v] == 0]
topo_order = []

while queue:
    u = queue.pop(0)
    topo_order.append(u)

    for v, weight in neg_graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

dist = {v: float('inf') for v in vertices}
dist["A"] = 0

for u in topo_order:
    if dist[u] != float('inf'):
        for v, weight in neg_graph[u]:
            if dist[v] > dist[u] + weight:  #
                dist[v] = dist[u] + weight

longest_path_distances = {}
for v in vertices:
    if dist[v] != float('inf'):
        longest_path_distances[v] = -dist[v]
    else:
        longest_path_distances[v] = None  

print("Longest path distances from the source 'A':")
for vertex in longest_path_distances:
    print(f"From 'A' to {vertex}: {longest_path_distances[vertex]}")

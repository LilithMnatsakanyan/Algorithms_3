import numpy as np
def topological(graph):
    nodes = list(graph.keys())
    in_degree = np.zeros(len(nodes), dtype=int)

    for node in graph:
        for neighbor in graph[node]:
            in_degree[nodes.index(neighbor)] += 1

    queue = []
    for i in range(len(nodes)):
        if in_degree[i] == 0:
            queue.append(nodes[i])

    ordering = []

    while queue:
        node = queue.pop(0)
        ordering.append(node)

        for neighbor in graph[node]:
            in_degree[nodes.index(neighbor)] -= 1
            if in_degree[nodes.index(neighbor)] == 0:
                queue.append(neighbor)

    if len(ordering) != len(graph):
        return None

    return ordering


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

print(topological(graph))


# -----------------------------------------------------------------------------------------------------------
# import numpy as np
#
#
# def topological(graph):
#     # Number of nodes in the graph
#     num_nodes = len(graph)
#
#     # Initialize in-degree array with zeros
#     in_degree = np.zeros(num_nodes, dtype=int)
#
#     # Calculate in-degrees
#     for node in range(num_nodes):
#         for neighbor in graph[node]:
#             in_degree[neighbor] += 1
#
#     # Initialize the queue for nodes with zero in-degree
#     queue = []
#     for node in range(num_nodes):
#         if in_degree[node] == 0:
#             queue.append(node)
#
#     ordering = []
#
#     while queue:
#         node = queue.pop(0)
#         ordering.append(node)
#
#         for neighbor in graph[node]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
#
#     if len(ordering) != num_nodes:
#         return None  # Graph contains a cycle
#
#     return ordering
#
#
# # Graph represented by a list of lists (adjacency list)
# graph = [
#     [2, 6, 3],  # Node 0 -> [2, 6, 3]
#     [4],  # Node 1 -> [4]
#     [6],  # Node 2 -> [6]
#     [1, 4],  # Node 3 -> [1, 4]
#     [5, 8],  # Node 4 -> [5, 8]
#     [],  # Node 5 -> []
#     [7, 11],  # Node 6 -> [7, 11]
#     [4, 12],  # Node 7 -> [4, 12]
#     [],  # Node 8 -> []
#     [2, 10],  # Node 9 -> [2, 10]
#     [6],  # Node 10 -> [6]
#     [12],  # Node 11 -> [12]
#     [8],  # Node 12 -> [8]
#     []  # Node 13 -> []
# ]
#
# print(topological(graph))

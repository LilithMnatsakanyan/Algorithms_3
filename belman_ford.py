def find_source_target(matrix_way):
    source, target = None, None

    for i, j, _ in matrix_way:
        if i not in [x[1] for x in matrix_way]:
            source = i
        if j not in [x[0] for x in matrix_way]:
            target = j

    return source, target

def find_shortest_path(matrix_way, source, target):
    vertices_set = set()
    for uvw in matrix_way: # uvw = [u, v, weight]
        vertices_set.add(uvw[0])
        vertices_set.add(uvw[1])
    num_vertices = len(vertices_set)

    INF = float('inf')
    distance = [INF] * num_vertices
    previous = [None] * num_vertices
    distance[source] = 0

    # Bellman-Ford algorithm
    for _ in range(num_vertices - 1):
        for u, v, weight in matrix_way:
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                previous[v] = u

    shortest_path = []
    current = target
    while current is not None:
        shortest_path.append(current)
        current = previous[current]
    shortest_path.reverse()

    total_length = distance[target]

    print(f"Shortest path from {source} to {target}:")
    for i in range(len(shortest_path) - 1):
        print(f"{shortest_path[i]}-{shortest_path[i + 1]} (length: { distance[shortest_path[i + 1]]- (distance[shortest_path[i]]) }) ", end=" ")
        '''To find the vertex and its closest neighbor, take the first initial element and attach it
        to the closest neighbor using the already formed list, also indicating the path length or weight'''

    print(f"Total length: {total_length}")

# Graph
matrix_way =  [[1,2, 2], [1,3, 5], [1,4, 3],[1,5, 4], [2,6, 5], [2,7, 6], [3,6, 1], [3,8, 6],[3,9, 9], [4,7, 8], [4,8, 7], [5,8, 5], [5,9, 7],
              [5,10, 6], [6,11, 9], [6,13, 10], [7,11, 6], [7,12, 8], [8,11, 9],
              [8,12, 8], [8,13, 9], [9,13, 9], [10,12, 7], [10,13, 10], [11,14, 6], [11,15, 12], [11,16, 6], [11,17, 7],
              [12,15, 9], [12,17, 9], [12,18, 10], [13,16, 8], [13,17, 9], [14,19, 9], [14,21, 7], [15,19, 5], [15,20, 3],[16,19, 6],
              [16,21, 4], [16,22, 5], [17,20, 3], [17,21, 2], [18,20, 3], [18,22, 6], [19,0, 5], [20, 0, 9],
              [21,0, 3], [22,0, 4]]

source, target = find_source_target(matrix_way)
find_shortest_path(matrix_way, source, target)


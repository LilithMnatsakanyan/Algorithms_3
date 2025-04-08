import numpy as np
def find_start_end(matrix):
    start, end = None, None

    for i, j, _ in matrix:
        if i not in [x[1] for x in matrix]:
            start = i
        if j not in [x[0] for x in matrix]:
            end = j

    return start, end

def func(distance_matrix, start, end):

    infinity = float('inf')
    distance = [infinity] * nodes_count
    visited = [None] * nodes_count
    distance[start] = 0

    for _ in range(nodes_count - 1):
        for i in range(nodes_count):
            for j in range(nodes_count):
                if distance_matrix[i][j] != 0  and distance[i] + distance_matrix[i][j] < distance[j]:
                    distance[j] = distance[i] + distance_matrix[i][j]
                    visited[j] = i

    path = []
    k = end
    while k is not None:
        path.append(k)
        k = visited[k]
    path.reverse()

    return path, distance[end]

# example
matrix =  [[1,2, 2], [1,3, 5], [1,4, 3],[1,5, 4], [2,6, 5], [2,7, 6], [3,6, 1], [3,8, 6],[3,9, 9], [4,7, 8], [4,8, 7], [5,8, 5], [5,9, 7],
              [5,10, 6], [6,11, 9], [6,13, 10], [7,11, 6], [7,12, 8], [8,11, 9],
              [8,12, 8], [8,13, 9], [9,13, 9], [10,12, 7], [10,13, 10], [11,14, 6], [11,15, 12], [11,16, 6], [11,17, 7],
              [12,15, 9], [12,17, 9], [12,18, 10], [13,16, 8], [13,17, 9], [14,19, 9], [14,21, 7], [15,19, 5], [15,20, 3],[16,19, 6],
              [16,21, 4], [16,22, 5], [17,20, 3], [17,21, 2], [18,20, 3], [18,22, 6], [19,0, 5], [20, 0, 9],
              [21,0, 3], [22,0, 4]]

nodes = set()
for i in matrix:
    nodes.add(i[0])
    nodes.add(i[1])
nodes_count = len(nodes)
distance_matrix = np.zeros((nodes_count, nodes_count), dtype=int)
for i in matrix:
    distance_matrix[i[0]][i[1]] = i[2]

# Main code
start, end = find_start_end(matrix)
shortest_path, distance = func(distance_matrix, start, end)

print("The shortest path of:", start, "--->", end, ":")
print(shortest_path, "Shortest distance:", distance)
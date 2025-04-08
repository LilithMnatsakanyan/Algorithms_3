# # Global or class scopevariables
# n = number of nodes in the graph
# g = adjacency list representing graph
# visited = [false, ….., falsel # sizen function dfs(at):
# if visited [at]: return visited [at]= true
# neighbours = graph[at]
# for next in neighbours:
# dfs(next)
# # Start DFS at node zero
# start_node = 0
# dfs(start_node)

graph = {
    '0': ['9', '1'],
    '1': ['0', '8'],
    '9': ['0', '8'],
    '8': ['7'],
    '7': ['8', '3', '6', '11', '10'],
    '3': ['7', '2', '4', '5'],
    '6': ['7', '5'],
    '11': ['7', '10'],
    '10': ['7', '11'],
    '2': ['3'],
    '4': ['3'],
    '5': ['3', '6'],
    '12': []

}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


dfs(graph, '0')


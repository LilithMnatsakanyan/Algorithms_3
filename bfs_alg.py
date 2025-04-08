# from collections import deque


graph = {
    '0' : ['9' , '7', '11'],
    '9' : ['10', '8', '0'],
    '7' : ['11', '6', '3', '0'],
    '11' : ['7', '0'],
    '10' : ['1', '9'],
    '8' : ['1', '12', '9'],
    '6' : ['5', '7'],
    '3' : ['2', '4', '7'],
    '1' : ['10', '8'],
    '12' : ['2', '8'],
    '5' : ['6'],
    '2' : ['12', '3'],
    '4' : ['3']

}

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     print("Queue: ", end = "")
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node, end=" ")
#             visited.add(node)
#             queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
#
# bfs(graph, '0')
#
# print("\n ")

def bfs(graph, start):
    visited = set()
    queue = [start]
    print("Queue: ", end='')
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print( node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

bfs(graph, '0')
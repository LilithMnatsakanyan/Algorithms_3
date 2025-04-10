n = 7
g = {
    0: [1],
    1: [2, 4, 6],
    2: [3],
    3: [2, 4, 5],
    4: [5],
    5: [4],
    6: [0, 2]
}
# n =8
# g = {
#     0: [1],
#     1: [2],
#     2: [0],
#     3: [4, 7],
#     4: [5],
#     5: [0, 6],
#     6: [0, 2, 4],
#     7: [3, 5]
#
# }
count = 0
components = [-1] * n
visited = [False] * n

for i in range(n):
    if not visited[i]:
        count += 1
        stack = [i]
        while stack:
            at = stack.pop()
            if not visited[at]:
                visited[at] = True
                components[at] = count
                for next_node in g[at]:
                    if not visited[next_node]:
                        stack.append(next_node)

print("Number of connected components:", count)
print("Components array:", components)
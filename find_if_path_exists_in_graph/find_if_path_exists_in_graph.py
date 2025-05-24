from collections import defaultdict, deque

# dfs
# class Solution(object):
#     def validPath(self, n, edges, source, destination):
#         """
#         :type n: int
#         :type edges: List[List[int]]
#         :type source: int
#         :type destination: int
#         :rtype: bool
#         """
#         graph = defaultdict(list)
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
#
#         visited = set()
#         def dfs(node):
#             if node == destination:
#                 return True
#             visited.add(node)
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     if dfs(neighbor):
#                         return True
#             return False
#         return dfs(source)

# -----------------------------------------------------------------------------------------
# bfs
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        queue = deque([source])
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False

# example 1 from leetcode
n1 = 3
edges1 = [[0, 1], [1, 2], [2, 0]]
source1, dest1 = 0, 2
# Graph is a triangle, so 0→2 is reachable
print(Solution().validPath(n1, edges1, source1, dest1))  # True

# example 2 from leetcode
n2 = 6
edges2 = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source2, dest2 = 0, 5
# Nodes {0,1,2} are disconnected from {3,4,5}, so 0→5 is not reachable
print(Solution().validPath(n2, edges2, source2, dest2))  # False

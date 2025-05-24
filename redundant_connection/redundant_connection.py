class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [i for i in range(len(edges) + 1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootY] = rootX
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]

# example from leetcode
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(Solution().findRedundantConnection(edges)) # output [1,4]

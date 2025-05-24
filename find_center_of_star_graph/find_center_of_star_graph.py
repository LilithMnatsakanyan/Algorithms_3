class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]


# example from leetcode
edges = [[1,2], [2,3]]
print(Solution().findCenter(edges)) # output 2

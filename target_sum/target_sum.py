class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        def dfs(index, current_sum):
            key = (index, current_sum)
            if key in memo:
                return memo[key]
            if index == len(nums):
                return 1 if current_sum == target else 0
            add = dfs(index + 1, current_sum + nums[index])
            subtract = dfs(index + 1, current_sum - nums[index])
            memo[key] = add + subtract
            return memo[key]
        return dfs(0, 0)


# example from leetcode
nums = [1, 1, 1, 1, 1]
target = 3
print(Solution().findTargetSumWays(nums, target)) # output 5


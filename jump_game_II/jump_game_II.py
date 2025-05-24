class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break
        return jumps

# example from leetcode
example = [2, 3, 1, 1, 4]
# you can jump from index 0 -> 1 (nums[0]=2 allows jump length up to 2),
# then from index 1 -> 4. Total jumps = 2.
print(Solution().jump(example))  # output 2

#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        k = 0
        set_nums = set(nums)
        for i in set_nums:
            if nums.count(i) > 1:
                for j in range(nums.count(i)-1, 0, -1):
                    k += j
        return k
# @lc code=end


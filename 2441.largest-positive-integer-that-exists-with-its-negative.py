#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        while r - l > 0:
            if nums[r] == -nums[l]:
                return nums[r]
            if nums[r] > - nums[l]:
                r -= 1
            else: l += 1
        return -1    
# @lc code=end


#
# @lc app=leetcode id=2733 lang=python3
#
# [2733] Neither Minimum nor Maximum
#

# @lc code=start
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if len(nums) > 2: return nums[1]
        return -1
# @lc code=end


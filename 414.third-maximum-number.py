#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums=sorted(nums)
        if len(nums) > 2: return nums[-3]
        else: return nums[-1]
# @lc code=end


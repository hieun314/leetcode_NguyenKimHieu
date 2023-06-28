#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = set(nums)
        for i in temp:
            if nums.count(i) == 1:
                return i
# @lc code=end


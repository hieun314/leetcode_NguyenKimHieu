#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_list = {}
        for i, num in enumerate(nums):
            if num in num_list:
                return True
            else:
                num_list[num] = i
        return False
# @lc code=end


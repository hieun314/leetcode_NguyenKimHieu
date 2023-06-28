#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = {}
        for i, num in enumerate(nums):
            compensation = target - num
            if compensation in num_list:
                return [num_list[compensation], i]
            num_list[num] = i
        return None       
# @lc code=end


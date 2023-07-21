#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = nums[0]
        min1 = nums[0]
        output = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                min1, max1 = max1, min1
            max1 = max(nums[i], max1*nums[i])
            min1 = min(nums[i], min1*nums[i])
            output = max(max1, output)
        return output   
# @lc code=end


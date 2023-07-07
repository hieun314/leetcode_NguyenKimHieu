#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_num = 0
        output = len(nums)+1
        j = 0
        for i in range(len(nums)):
            sum_num += nums[i]
            while sum_num >= target:
                output = min(output, i - j + 1)
                sum_num -= nums[j]
                j += 1
        return output if output != len(nums)+1 else 0     
# @lc code=end


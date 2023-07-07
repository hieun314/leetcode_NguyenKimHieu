#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        right = [nums[-1]]
        output = []
        for i in range(-2, -len(nums), -1):
            right.append(nums[i]*right[-i-2])
        output.append(right[-1])
        for j in range(1, len(nums)-1):
            left.append(nums[j]*left[j-1])
            output.append(left[j-1]*right[-j - 1])
        output.append(left[-1])
        return output   
# @lc code=end


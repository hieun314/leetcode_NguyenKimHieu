#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tmp = [False] * len(nums)
        tmp[0] = True
        for i in range(len(tmp)):
            if tmp[i] == True:
                if nums[i] + i >= len(nums) - 1: return True
                tmp[i:nums[i]+i],tmp[nums[i]+i] = [True]*(nums[i]), True
        return tmp[-1]
# @lc code=end


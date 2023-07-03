#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if nums[0] == 0:
            nums.pop(0)
        i = -1
        for i in range(len(nums)):
            if (i + 1) != nums[i]:
                if i + 1 not in nums: 
                    return i + 1
        return i + 2   
# @lc code=end


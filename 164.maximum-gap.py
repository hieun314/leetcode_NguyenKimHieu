#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        output = 0
        nums.sort()
        for i in range(1,len(nums)):
            output = max(output,nums[i]-nums[i-1])
        return output   
# @lc code=end


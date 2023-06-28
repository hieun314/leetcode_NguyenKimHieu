#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        k=0
        output=[]
        for i in range(len(nums)):
            k = nums[i]+k
            output.append(k)
        return output
# @lc code=end


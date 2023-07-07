#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        newsum = sum(nums[0:k])
        maxsum = newsum
        for i in range(k,len(nums)):
           newsum -= nums[i-k]
           newsum += nums[i]
           maxsum = max(maxsum, newsum)
        return maxsum/k  
# @lc code=end


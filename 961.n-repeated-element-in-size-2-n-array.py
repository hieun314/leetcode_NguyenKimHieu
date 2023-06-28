#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        if nums.count(nums[len(nums)//2]) == len(nums)//2: return nums[len(nums)//2]
        return nums[len(nums)//2-1]
# @lc code=end


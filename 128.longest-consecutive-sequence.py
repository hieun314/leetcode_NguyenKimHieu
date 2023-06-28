#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        k = 1
        nums = list(set(nums))
        nums.sort()
        if len(nums) <= 1: return len(nums)
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                k += 1
            else:
                longest=max(longest,k)
                k = 1
        longest=max(longest,k)
        return longest
# @lc code=end


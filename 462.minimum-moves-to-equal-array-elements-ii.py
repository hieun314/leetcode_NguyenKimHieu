#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#

# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        k = 0
        nums.sort()
        k = nums[len(nums)//2]
        output = 0
        for i in nums:
            output += abs(i-k)
        return output
# @lc code=end


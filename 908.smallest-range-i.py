#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(nums)-min(nums)-2*k if max(nums)-min(nums)-2*k > 0 else 0        
# @lc code=end


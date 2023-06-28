#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0
        l = 0
        r = len(height)-1
        while r - l > 0:
            s = max(s, (r-l)*min(height[l],height[r]))
            if height[l] > height[r]:r-= 1
            else:l+=1
        return s            
# @lc code=end


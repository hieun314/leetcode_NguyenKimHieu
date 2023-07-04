#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        max1 = 0
        max2 = 0
        l = 0
        r = len(height)-1
        while r - l > 0:
            if height[r] >= height[l]:
                max1 = max(max1,height[l])
                s += max1 - height[l]
                l += 1
            else:
                max2 = max(max2,height[r])
                s += max2-height[r]
                r -= 1
        return s    
# @lc code=end


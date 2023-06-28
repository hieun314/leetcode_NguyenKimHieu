#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return n
        step1 = 1
        step2 = 1
        for i in range(2, n+1):
            count = step1 + step2
            step2 = step1
            step1 = count            
        return count      
# @lc code=end


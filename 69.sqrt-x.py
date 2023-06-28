#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        for i in range(x):
            if i*i == x:
                return i
                break
            elif i*i < x and x < (i+1)*(i+1):
                return i
                break
        return 1

# @lc code=end


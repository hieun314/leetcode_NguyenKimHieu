#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0: x,sign = -x,-1
        x = str(x)
        x = x[::-1]
        x = int(x) * sign
        if x < -2**31 or x > 2**31 -1: return 0
        return x
# @lc code=end


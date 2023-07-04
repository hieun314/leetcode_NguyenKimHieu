#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend//divisor > 2**31 -1: return 2**31-1
        elif dividend//divisor < -2**31: return -2**31
        elif dividend//divisor >= 0 or dividend%divisor == 0: return dividend//divisor
        return dividend//divisor + 1     
# @lc code=end


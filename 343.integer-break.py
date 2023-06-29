#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n-1
        total = n//3
        tmp = n%3
        if tmp == 1: return 3**(total-1)*4
        elif tmp == 2: return 3**total*2
        return 3**total
# @lc code=end


#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        while n > 1 :
            if n%2 == 0:
                n //= 2
            else: return False
        return True
# @lc code=end


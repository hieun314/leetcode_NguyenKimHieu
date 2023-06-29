#
# @lc app=leetcode id=2544 lang=python3
#
# [2544] Alternating Digit Sum
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = 0
        k = 1
        n = int(str(n)[::-1])
        while n != 0:
            if k == 1:
                s += n%10
                k = 0
            else:
                s -= n%10
                k = 1
            n //= 10
        return s 
# @lc code=end


#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9: return n
        i = 1
        while True:
            n -= 9*10**(i-1)*(i)
            if n <= 9*10**i*(i+1):
                return int(str(10**i+(n-1)//(i+1))[(n+i)%(i+1)])
            i += 1        
# @lc code=end


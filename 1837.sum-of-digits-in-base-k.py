#
# @lc app=leetcode id=1837 lang=python3
#
# [1837] Sum of Digits in Base K
#

# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total =""
        while n != 0:
            total += str(n%k)
            n = n//k
        for i in total:
            n+=int(i)
        return n  
# @lc code=end


#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 0
        while n != 0:
            if n%2==1: k+=1
            n=n//2
        return k
# @lc code=end


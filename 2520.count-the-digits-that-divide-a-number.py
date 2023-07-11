#
# @lc app=leetcode id=2520 lang=python3
#
# [2520] Count the Digits That Divide a Number
#

# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:
        tmp = num
        a = 0
        while tmp != 0:
            if num%(tmp%10) == 0:
                a += 1
            tmp //= 10
        return a        
# @lc code=end


#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        n = 1
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                n += i + num//i
        return num == n
# @lc code=end


#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        str1 = ""
        sign = 0
        if num < 0:
            sign = 1
            num = -num
        if num == 0: str1 += "0"
        while num != 0:
            str1 = str(num%7) + str1
            num //= 7
        if sign == 1: str1 = "-" + str1
        return str1  
# @lc code=end


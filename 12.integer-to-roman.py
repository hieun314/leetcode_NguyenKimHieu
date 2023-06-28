#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        str=""
        s = ["I", "V", "X", "L", "C", "D", "M"]
        k = [1, 5, 10, 50, 100, 500, 1000]
        i = 1
        while num != 0 and i <= 7:
            total = num//k[-i]
            if total == 4:
                str += s[-i] + s[-i+1]
            elif total == 9:
                str += s[-i] + s[-i+2]
            elif total >= 5:
                str += s[-i+1]
                str += (total-5)*s[-i]
            elif total < 5:
                str+= total*s[-i]
            num -= total*k[-i]
            i += 2
        return str
# @lc code=end


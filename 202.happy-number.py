#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        note = []
        while n>0:
            temp = 0
            while n>0:
                temp += (n%10)**2
                n//=10
            if temp in note:
                return False
            else:
                note.append(temp)
            if temp == 1: return True
            n = temp
        return False
# @lc code=end


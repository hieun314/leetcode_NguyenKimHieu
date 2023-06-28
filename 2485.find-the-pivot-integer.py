#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        i = 1
        s1 = i
        s2 = n
        while i != n:
            if s1 <= s2:
                i +=1
                s1 += i
            elif s2 < s1:
                n-=1
                s2 += n
        if s1 == s2: return n
        return -1
# @lc code=end


#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        tmp1 = ""
        tmp2 = ""
        for i in range(len(s)):
            if s[i] != goal[i]:
                tmp1 += s[i]
                tmp2 += goal[i]
        if len(tmp1) == 2:
            return tmp1 == tmp2[::-1]
        if len(tmp1) == 0:
            return len(set(s)) < len(s)
        return False  
# @lc code=end


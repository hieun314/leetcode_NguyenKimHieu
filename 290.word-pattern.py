#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_pattern = {}
        list_s = {}
        s = s.split(" ")
        if len(s) != len(pattern): return False
        for i in range(len(pattern)):
            if pattern[i] not in list_pattern:
                if s[i] not in list_s:
                    list_s[s[i]] = pattern[i]
                    list_pattern[pattern[i]] = s[i]
                else: return False
            elif list_pattern[pattern[i]] != s[i]: return False
        return True    
# @lc code=end


#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False
        set_arr=set(t)
        for char in set_arr:
            if t.count(char) != s.count(char): return False
        return True
# @lc code=end


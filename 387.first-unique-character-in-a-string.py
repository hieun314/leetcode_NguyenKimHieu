#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for char in s:
            if s.count(char) == 1:
                return s.index(char)
                break
        return -1
# @lc code=end


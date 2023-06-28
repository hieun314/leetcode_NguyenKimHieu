#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = 0
        for i in range(1, len(s) + 1):
            if s[-i] != " ":
                k += 1
            if s[-i] == " " and k > 0:
                    break
        return k
# @lc code=end


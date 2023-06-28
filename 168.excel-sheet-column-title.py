#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        str = ""
        while columnNumber > 0:
            columnNumber -= 1
            total = columnNumber%26
            str = chr(ord('A') + total) + str
            columnNumber //= 26
        return str
# @lc code=end


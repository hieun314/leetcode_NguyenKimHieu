#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        i = 0
        for i in range(len(haystack)):        
            if haystack[i:k+i] == needle:
                return i
        return -1
# @lc code=end


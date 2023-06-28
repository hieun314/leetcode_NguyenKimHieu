#
# @lc app=leetcode id=1967 lang=python3
#
# [1967] Number of Strings That Appear as Substrings in Word
#

# @lc code=start
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        k = 0
        for char in patterns:
            if char in word:
                k+=1
        return k
            
# @lc code=end


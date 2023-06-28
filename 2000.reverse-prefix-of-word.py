#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            i = word.index(ch)
            word = word.replace(word[:i+1],word[i::-1])
        return word

# @lc code=end


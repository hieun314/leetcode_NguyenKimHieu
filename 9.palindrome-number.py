#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        char = str(x)
        char = char[::-1]
        y = int(char)
        if x == y: return True
        else: return False
# @lc code=end


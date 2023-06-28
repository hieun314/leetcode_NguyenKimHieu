#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace("_","")        
        s = s.replace(" ","")
        s = re.sub(r"[^\w\s]", "", s)
        if s==s[::-1]: return True
        return False
# @lc code=end


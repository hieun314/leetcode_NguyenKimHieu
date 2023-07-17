#
# @lc app=leetcode id=1556 lang=python3
#
# [1556] Thousand Separator
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        strs = ""
        n = str(n)
        while True:
            strs = n[-3:] + strs
            n = n[:-3]
            if len(n) == 0: break
            strs = "." + strs
        return strs        
# @lc code=end


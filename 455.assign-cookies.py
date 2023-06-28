#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 1
        j = 1
        k = 0
        g.sort()
        s.sort()
        while i <= len(g) and j <= len(s):
            if g[-i] <= s[-j]:
                k +=1
                i,j=i+1,j+1
            else: i+=1
        return k
# @lc code=end


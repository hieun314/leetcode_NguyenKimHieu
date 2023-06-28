#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while r-l >= 0:
            mid=(r+l)//2
            if mid**2 < num and (mid + 1)**2 > num: return False
            elif mid**2 < num: l = mid + 1
            elif mid**2 > num: r = mid - 1
            else: return True
# @lc code=end


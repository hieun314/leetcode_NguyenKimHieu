#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        return int(num[0]+num[3]) + int(num[1] + num[2])        
# @lc code=end


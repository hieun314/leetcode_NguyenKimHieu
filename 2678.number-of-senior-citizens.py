#
# @lc app=leetcode id=2678 lang=python3
#
# [2678] Number of Senior Citizens
#

# @lc code=start
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        k = 0
        for char in details:
            n = int(char[-4:-2])
            if n > 60: k += 1
        return k
# @lc code=end


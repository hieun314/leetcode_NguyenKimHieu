#
# @lc app=leetcode id=1551 lang=python3
#
# [1551] Minimum Operations to Make Array Equal
#

# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        n -= 1
        k = 0
        while n > 0:
            k += n
            n -= 2
        return k
# @lc code=end


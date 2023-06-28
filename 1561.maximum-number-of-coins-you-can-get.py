#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        k = 0
        i = 0
        j = len(piles) - 2
        piles.sort()
        while j - i > 0:
            k += piles[j]
            j -= 2
            i += 1
        return k
# @lc code=end


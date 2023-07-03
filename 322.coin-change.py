#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0: return 0
        tmp = [amount+1] * (amount+1)
        tmp[0] = 0
        for i in range(len(tmp)):
            if tmp[i] < amount + 1:
                for coin in coins:
                    if i + coin < amount + 1:
                        tmp[i+coin] = min(tmp[i+coin],tmp[i]+1)
        if tmp[amount] == amount+1: return -1
        else: return tmp[amount]
# @lc code=end


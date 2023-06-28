#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        min = prices[0]
        output = 0
        while i < len(prices):
            if prices[i] > min:
                output = max(output, prices[i]-min)
            elif prices[i] <= min: min = prices[i] 
            i+=1
        return output
# @lc code=end


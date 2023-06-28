#
# @lc app=leetcode id=1725 lang=python3
#
# [1725] Number Of Rectangles That Can Form The Largest Square
#

# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        x = max((min(rec) for rec in rectangles))
        return  len([rec for rec in rectangles if int(rec[0])>=x and int(rec[1])>=x])
# @lc code=end


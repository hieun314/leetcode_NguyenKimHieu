#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        k = 0
        if len(flowerbed)==1 and flowerbed[0] == 0 : n-=1
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i+=1
                k=0
            elif flowerbed[i] == 0: 
                i+=1
                k+=1
            if k == 2 and i == 2: 
                n-=1
                k=0
                i-=1                
            if k == 3:
                k=0
                n-=1
                i-=1
        if k == 2: n-=1
        return True if n <= 0 else False
# @lc code=end


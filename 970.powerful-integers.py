#
# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
#

# @lc code=start
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        i = 0
        j = 0
        temp = []
        if bound < 2: return temp
        elif x == 1 and y == 1: temp.append(2) 
        elif x == 1 or y == 1:
            while max(x,y)**i+1<bound:
                temp.append(max(x,y)**i+1)
                i+=1
        else:
            while x**i <= bound:
                j = 0
                while x**i + y**j <= bound:
                    temp.append(x**i + y**j)
                    j+=1
                i+=1
        temp=list(set(temp))
        temp.sort()
        return temp
# @lc code=end


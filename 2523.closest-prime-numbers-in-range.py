#
# @lc app=leetcode id=2523 lang=python3
#
# [2523] Closest Prime Numbers in Range
#

# @lc code=start
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        nums = [True] * (right + 2)
        if right + 1 > 0: nums[0] = False
        if right + 1 > 1: nums[1] = False
        for i in range(2, right + 1):
            if nums[i] == True:
                for j in range(i*i, right + 1, i):
                    nums[j] = False
        output = [-1,-1]
        if True in nums[left:right+1]: 
            s = nums[left:right+1].index(True) + left
            x = right - left
            for e in range(left , right+1):
                if nums[e] == True and e > s:
                    if x > e - s:
                        x = e - s
                        output = [s,e]
                    elif x == e - s:
                        if output == [-1,-1]: output = [s,e]
                    s = e
        return output      
# @lc code=end


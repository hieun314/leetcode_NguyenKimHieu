#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        output=[0]*n
        i = 0
        j = len(output)-1
        k = 1
        while i <= j - 1:
            output[i]=k
            output[j]=-k
            i +=1
            j -=1
            k+=1
        return output
# @lc code=end


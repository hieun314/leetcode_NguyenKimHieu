#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums=[]
        nums.append([1])
        for i in range(0, rowIndex):
            next = [1]
            for j in range(i):
                next.append(nums[i][j]+nums[i][j+1])
            next.append(1)
            nums.append(next)
        return nums[rowIndex]
                
        
# @lc code=end


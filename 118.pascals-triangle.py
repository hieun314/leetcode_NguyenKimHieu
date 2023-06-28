#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums=[]
        nums.append([1])
        for i in range(0, numRows-1):
            next = [1]
            for j in range(i):
                next.append(nums[i][j]+nums[i][j+1])
            next.append(1)
            nums.append(next)
        return nums

# @lc code=end


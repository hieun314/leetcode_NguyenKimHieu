#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count += 4
                    if j in range(1,len(grid[i])):
                        if grid[i][j-1] == 1: count -= 2
                    if i in range(1,len(grid)):
                        if grid[i-1][j] == 1: count -= 2
        return count        
# @lc code=end


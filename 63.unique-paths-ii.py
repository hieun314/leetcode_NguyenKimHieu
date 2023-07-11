#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1: return 0
        obstacleGrid[0][0] = -1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0 and obstacleGrid[i-1][j] != 1:
                    obstacleGrid[i][j] += obstacleGrid[i-1][j]
                if j > 0 and obstacleGrid[i][j-1] != 1:
                    obstacleGrid[i][j] += obstacleGrid[i][j-1]
        return -obstacleGrid[-1][-1]    
# @lc code=end


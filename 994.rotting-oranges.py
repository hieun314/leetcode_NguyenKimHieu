#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        k = 2
        while True:
            change = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == k:
                        if i > 0:
                            if grid[i-1][j] == 1:
                                grid[i-1][j] = k + 1
                                change = 1
                        if i < m - 1:
                            if grid[i+1][j] == 1:
                                grid[i+1][j] = k + 1
                                change = 1
                        if j > 0:
                            if grid[i][j-1] == 1:
                                grid[i][j-1] = k + 1
                                change = 1
                        if j < n - 1:
                            if grid[i][j+1] == 1:
                                grid[i][j+1] = k + 1
                                change = 1
            if change == 0:
                for i in range(m):
                    if 1 in grid[i]: return -1
                return k - 2
            k += 1       
# @lc code=end


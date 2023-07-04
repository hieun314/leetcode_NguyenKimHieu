#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [[0] * n for _ in range(m)]
        count[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    count[i][j] += count[i-1][j]
                if j > 0:
                    count[i][j] += count[i][j-1]
        return count[m-1][n-1]   
# @lc code=end


#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tmp = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            k = 0
            for j in range(n):
                if matrix[i][j] == 0:
                    k += 1
                if matrix[i][j] == 0 and j not in tmp:
                    tmp.append(j)
            if k > 0:
                matrix[i] = [0]*n
        for j in tmp:
            for i in range(m):
                matrix[i][j] = 0   
# @lc code=end


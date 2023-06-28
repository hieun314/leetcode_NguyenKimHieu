#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        i = 0
        j = 0
        k = 1
        n = len(matrix[0])
        m = len(matrix)
        while len(output) < n * m:
            output.append(matrix[i][j])
            matrix[i][j]=101
            if k == 1:
                if j < n - 1:
                    j += 1
                    if matrix[i][j] == 101: k,j = 2,j-1
                else: k = 2
            if k == 2:
                if i < m - 1: 
                    i += 1
                    if matrix[i][j] == 101: k,i = 3,i-1
                else: k = 3
            if k == 3:
                if j > 0:
                    j -= 1
                    if matrix[i][j] == 101: k,j = 4,j+1
                else: k = 4
            if k == 4:
                if i > 0:
                    i -= 1
                    if matrix[i][j] == 101: k,i,j = 1,i+1,j+1
                else: k = 1
        return output
# @lc code=end


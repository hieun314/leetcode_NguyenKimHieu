#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        for i in zip(*matrix[::-1]): temp.append(i)
        for j in range(len(matrix)):
            matrix[j]=temp[j]
# @lc code=end


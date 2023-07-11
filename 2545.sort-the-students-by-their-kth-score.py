#
# @lc app=leetcode id=2545 lang=python3
#
# [2545] Sort the Students by Their Kth Score
#

# @lc code=start
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        output = []
        list_num = {}
        for i in range(len(score)):
            list_num[i] = score[i][k]
        list_num = sorted(list_num.items(), key = lambda x: x[1], reverse = True)
        for i in range(len(score)):
            output.append(score[list_num[i][0]])
        return output    
# @lc code=end


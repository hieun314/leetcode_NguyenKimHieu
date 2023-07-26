#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        list_k = {1:[0,1], 2:[1,0], 3:[0,-1], 4:[-1,0]}
        start = [0,0]
        k = 1
        for _ in range(4):
            for char in instructions:
                if char == "G":
                    start[0] += list_k[k][0]
                    start[1] += list_k[k][1]
                elif char == "R":
                    if k != 4: k += 1
                    else: k = 1
                elif char == "L":
                    if k != 1: k -= 1
                    else: k = 4
        return start == [0,0]      
# @lc code=end


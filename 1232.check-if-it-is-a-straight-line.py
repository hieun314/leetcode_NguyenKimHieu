#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2: return True
        v1   = [a1 - a2 for a1, a2 in zip(coordinates[0], coordinates[1])]
        for i in range(2,len(coordinates)):
            v2 = [a1 - a2 for a1, a2 in zip(coordinates[0], coordinates[i])]
            if v2[0] == 0 and v1[0] != 0 or v2[1] == 0 and v1[1] != 0: return False
            elif v2[0] != 0 and v2[1] != 0:
                if v1[0]/v2[0]!=v1[1]/v2[1]:
                    return False
        return True                
# @lc code=end


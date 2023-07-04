#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        i = 0
        j = 1
        while i < len(target):
            if target[i] == j:
                output.append("Push")
                i+=1
                j+=1
            else:
                output.append("Push")
                output.append("Pop")
                j+=1
        return output   
# @lc code=end


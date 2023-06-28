#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = [0]
        for i in range(len(gain)):
            temp.append(temp[i]+gain[i])
        return max(temp)
# @lc code=end


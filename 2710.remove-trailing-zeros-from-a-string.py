#
# @lc app=leetcode id=2710 lang=python3
#
# [2710] Remove Trailing Zeros From a String
#

# @lc code=start
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i in range(1,len(num)+1):
            if num[-1] == "0": num=num[:-1]
            else: break
        return num 
# @lc code=end


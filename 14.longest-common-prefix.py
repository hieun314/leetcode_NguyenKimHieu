#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = strs[0]
        if len(strs) == 1: 
            return strs[0]
        for i in range(len(strs) - 1):
            str1 = temp
            str2 = strs[i+1]
            temp = ""
            for j in range (min(len(str1), len(str2))):
                if str1[j] != str2[j]:
                    break
                else: temp += str1[j]
        return temp

# @lc code=end


#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        strs = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        output = []
        for char in words:
            k = -1
            if char[0].lower() in strs[0]:
                k = 0
            elif char[0].lower() in strs[1]:
                k = 1
            elif char[0].lower() in strs[2]:
                k = 2
            for i in set(char):
                if i.lower() not in strs[k]:
                    k = -1
                    break
            if k != -1: output.append(char)
        return output     
# @lc code=end


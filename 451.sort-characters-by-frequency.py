#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        char_list = {}
        str = ""
        for char in set(s):
            char_list[char] = s.count(char)
        char_list = sorted(char_list.items(), key=lambda x: x[1], reverse= True)
        for i in char_list:
            str += i[0] * i[1]
        return str   
# @lc code=end


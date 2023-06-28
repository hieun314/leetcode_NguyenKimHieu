#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_list = {}
        start = 0
        max_length = 0
        for end, char in enumerate(s):
            if char in char_list and char_list[char] >= start:
                start = char_list[char] + 1
            else:
                current_length = end - start + 1
                max_length = max(max_length, current_length)
            char_list[char] = end
        return max_length
# @lc code=end


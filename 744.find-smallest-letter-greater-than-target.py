#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for char in letters:
            if round(ord(char)) > round(ord(target)):
                return char
        return letters[0]
# @lc code=end


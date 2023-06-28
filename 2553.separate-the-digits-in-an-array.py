#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
#

# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        temp = []
        for i in nums:
            i = str(i)
            for char in i:
                temp.append(int(char))
        return temp 
# @lc code=end


#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1 = 0
        s2 = 0
        for num in nums:
            s1 += num
            while num > 0:
                s2 += num%10
                num //= 10
        return abs(s1 - s2)   
# @lc code=end


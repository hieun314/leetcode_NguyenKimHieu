#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                k -= 1
                i -=1
            i += 1
        return k
# @lc code=end


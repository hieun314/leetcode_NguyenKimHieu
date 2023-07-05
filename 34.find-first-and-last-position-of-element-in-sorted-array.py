#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        tmp = [-1,-1]
        if target not in nums: return tmp
        tmp[0] = nums.index(target)
        for i in range(tmp[0],len(nums)):
            if nums[i] != target:
                break
            tmp[1] = i
        return tmp   
# @lc code=end


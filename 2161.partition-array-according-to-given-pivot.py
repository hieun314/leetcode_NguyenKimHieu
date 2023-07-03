#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#

# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        i = 0
        while i < len(nums):
            if nums[i] > pivot:
                right.append(nums[i])
            elif nums[i] == pivot:
                right.insert(0,nums[i])
            else: left.append(nums[i])
            i += 1
        left.extend(right)
        return left        
# @lc code=end


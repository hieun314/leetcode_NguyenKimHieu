#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        if len(nums1)%2 != 1: return (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2
        return float(nums1[len(nums1)//2])
# @lc code=end


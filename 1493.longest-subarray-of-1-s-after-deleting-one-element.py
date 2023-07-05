#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums: return len(nums) - 1
        start = 0
        mid = nums.index(0)
        count = 0
        max_length = mid - start
        for end, num in enumerate(nums):
            if num == 0: count += 1
            if count == 2:
                count -= 1
                start,mid = mid+1,end
            else:
                print(start,end)
                tmp = end - start
                max_length = max(max_length,tmp)
        return max_length
# @lc code=end


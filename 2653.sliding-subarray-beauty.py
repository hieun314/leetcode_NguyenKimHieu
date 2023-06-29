#
# @lc app=leetcode id=2653 lang=python3
#
# [2653] Sliding Subarray Beauty
#

# @lc code=start
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        output = []
        tmp = [0] * 51
        for i in range(len(nums)):
            if nums[i] > 0: nums[i] = 0
        for i in range(51):
            tmp[-i-1]=nums[:k].count(-i)
        for i in range(k,len(nums)+1):
            count = 0
            for j in range(len(tmp)):
                count += tmp[j]
                if count >= x:
                    output.append(-50+j)
                    break
            if i < len(nums):
                tmp[nums[i]-1] += 1
                tmp[nums[i-k]-1] -= 1
        return output
# @lc code=end


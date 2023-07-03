#
# @lc app=leetcode id=2293 lang=python3
#
# [2293] Min Max Game
#

# @lc code=start
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        k = 0
        i = 0
        newnums=[]
        while len(nums) != 1:
            if k == 0:
                newnums.append(min(nums[i],nums[i+1]))
                k = 1
            elif k == 1:
                newnums.append(max(nums[i],nums[i+1]))
                k = 0
            i += 2
            if i >= len(nums):
                i = 0
                nums = newnums
                newnums = []
        return nums[0]  
# @lc code=end

